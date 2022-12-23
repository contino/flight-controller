import boto3
from boto3.dynamodb.conditions import Key
import structlog
from typing import List, Optional
from datetime import datetime
from uuid import UUID
import json
import os



from .event_sink import EventSink
from .event_source import EventSource
from src.entities.events import Event
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectAssigned,
    ProjectAssignedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
)



TABLE_NAME = os.environ.get("DYNAMO_TABLE_NAME","event_sourcing_table")
# TODO fix the test environment variable 
# did not work https://github.com/MobileDynasty/pytest-env
#TABLE_NAME = os.environ.get("DYNAMO_TABLE_NAME")

dynamoDbResource = boto3.resource('dynamodb')
logger = structlog.get_logger(__name__)


class DynamoEventSink(EventSink):
    def __init__(self) -> None:
        self.dynamoDbTable = dynamoDbResource.Table(TABLE_NAME)

    
    def store_events(self, events: List[Event]) -> Optional[Exception]:
        try:
        # do deduplication before batch save
            with self.dynamoDbTable.batch_writer(overwrite_by_pkeys=['aggregateId', 'eventId']) as batch:
                for event in events:
                    value = {
                        'aggregateId': event.aggregateId,
                        'eventId':str(event.eventId),
                        'eventType': event.eventType,
                        'aggregateType': event.aggregateType,
                        'aggregateVersion':event.aggregateVersion,
                        'eventVersion': event.eventVersion,
                        'payload': json.dumps(event.payload.__dict__),
                        'datetime': int(round(datetime.utcnow().timestamp()))
                    }
                    batch.put_item(Item=value)
        except Exception as err:
            logger.error(f"Couldn't add to table type of error is {type(err)} AND reason is {err} ")
            return err

class DynamoEventSource(EventSource):
    def __init__(self) -> None:
        self.dynamoDbTable = dynamoDbResource.Table(TABLE_NAME)

    def get_events_for_aggregate(self, aggregate_id: str) -> List[Event]:
        response = self.dynamoDbTable.query(
            KeyConditionExpression=Key('aggregateId').eq(aggregate_id)
        )
        logger.msg(f"responses {response}")

        events: List[Event] = []
        for item in response['Items']:
            if item["eventType"] == "ProjectRequested":
                events.append(
                    ProjectRequested(
                        item["aggregateId"],
                        item["aggregateType"],
                        item["aggregateVersion"],
                        UUID(item["eventId"]),
                        item["eventVersion"],
                        ProjectRequestedPayload(
                            json.loads(item["payload"])["project_id"],
                            int(json.loads(item["payload"])["requested_time"])
                        ),
                        item["eventType"]
                    ))
            elif item["eventType"] == "ProjectAssigned":
                events.append(
                    ProjectAssigned(
                        item["aggregateId"],
                        item["aggregateType"],
                        item["aggregateVersion"],
                        UUID(item["eventId"]),
                        item["eventVersion"],
                        ProjectAssignedPayload(
                            json.loads(item["payload"])["project_id"],
                            int(json.loads(item["payload"])["assigned_time"])
                        ),
                        item["eventType"]
                    )
                )
            elif item["eventType"] == "ProjectCreated":
                events.append(
                    ProjectCreated(
                        item["aggregateId"],
                        item["aggregateType"],
                        item["aggregateVersion"],
                        UUID(item["eventId"]),
                        item["eventVersion"],
                        ProjectCreatedPayload(
                            json.loads(item["payload"])["project_id"],
                            int(json.loads(item["payload"])["created_time"])
                        ),
                        item["eventType"]
                    )
                )
        return events
