from datetime import datetime
import json
import os
from typing import List, Optional, Union
from uuid import UUID

import boto3
from boto3.dynamodb.conditions import Key
import structlog

from src.drivers.event_sink import EventSink
from src.drivers.event_source import EventSource
from src.entities.events import Event, EVENT_CLASSES


logger = structlog.get_logger(__name__)


class DynamoEventSink(EventSink):
    def __init__(self) -> None:
        TABLE_NAME = os.environ.get("DYNAMO_TABLE_NAME")
        dynamo_db_resource = boto3.resource("dynamodb")
        self.dynamo_db_table = dynamo_db_resource.Table(TABLE_NAME)

    def store_events(self, events: List[Event]) -> Optional[Exception]:
        try:
            # do deduplication before batch save
            with self.dynamo_db_table.batch_writer(
                overwrite_by_pkeys=["aggregate_id", "event_id"]
            ) as batch:
                for event in events:
                    value = {
                        "aggregate_id": event.aggregate_id,
                        "event_id": str(event.event_id),
                        "event_type": event.event_type,
                        "aggregate_type": event.aggregate_type,
                        "aggregate_version": event.aggregate_version,
                        "event_version": event.event_version,
                        "payload": event.payload.json(by_alias=True),
                        "datetime": int(round(datetime.utcnow().timestamp())),
                    }
                    batch.put_item(Item=value)
        except Exception as err:
            return err


class DynamoEventSource(EventSource):
    def __init__(self) -> None:
        TABLE_NAME = os.environ.get("DYNAMO_TABLE_NAME")
        dynamo_db_resource = boto3.resource("dynamodb")
        self.dynamo_db_table = dynamo_db_resource.Table(TABLE_NAME)

    def _sort_events(self, event: Event) -> int:
        return event.aggregate_version

    def get_events_for_aggregate(self, aggregate_id: str) -> Union[Exception, List[Event]]:
        try:
            response = self.dynamo_db_table.query(
                KeyConditionExpression=Key("aggregate_id").eq(aggregate_id)
            )

            events: List[Event] = []

            for item in response["Items"]:
                event_type = item["event_type"]
                if event_type in EVENT_CLASSES:
                    event_class, payload_class = EVENT_CLASSES[event_type]
                    payload = payload_class(**json.loads(item["payload"]))
                    event = event_class(
                        aggregate_id=item["aggregate_id"],
                        aggregate_type=item["aggregate_type"],
                        aggregate_version=int(item["aggregate_version"]),
                        event_id=UUID(item["event_id"]),
                        event_version=int(item["event_version"]),
                        payload=payload,
                    )
                    events.append(event)

            events.sort(key=self._sort_events)

            return events
        except Exception as err:
            return err
