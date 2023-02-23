from datetime import datetime
import json
import os
from typing import List, Optional
from uuid import UUID

import boto3
from boto3.dynamodb.conditions import Key
import structlog

from src.drivers.event_sink import EventSink
from src.drivers.event_source import EventSource
from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountRequested,
    AccountRequestedPayload,
)
from src.entities.compliance import (
    ResourceFoundCompliant,
    ResourceFoundCompliantPayload,
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)
from src.entities.guardrail import (
    GuardrailPassed,
    GuardrailPassedPayload,
    GuardrailActivated,
    GuardrailActivatedPayload,
)
from src.entities.events import Event
from src.entities.patch import PatchRunSummary, PatchRunSummaryPayload
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
)


from src.entities.identity import (
    IdentityCreated,
    IdentityCreatedPayload,
    IdentityRequested,
    IdentityRequestedPayload,
)

dynamo_db_resource = boto3.resource("dynamodb")
logger = structlog.get_logger(__name__)


class DynamoEventSink(EventSink):
    def __init__(self) -> None:
        TABLE_NAME = os.environ.get("DYNAMO_TABLE_NAME")
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
                        "payload": json.dumps(event.payload.__dict__),
                        "datetime": int(round(datetime.utcnow().timestamp())),
                    }
                    batch.put_item(Item=value)
        except Exception as err:
            logger.error(
                f"Couldn't add to table type of error is {type(err)} AND reason is {err} "
            )
            return err


class DynamoEventSource(EventSource):
    def __init__(self) -> None:
        TABLE_NAME = os.environ.get("DYNAMO_TABLE_NAME")
        self.dynamo_db_table = dynamo_db_resource.Table(TABLE_NAME)

    def _sort_events(self, event: Event) -> int:
        return event.aggregate_version

    def get_events_for_aggregate(self, aggregate_id: str) -> List[Event]:
        response = self.dynamo_db_table.query(
            KeyConditionExpression=Key("aggregate_id").eq(aggregate_id)
        )
        logger.msg(f"responses {response}")

        events: List[Event] = []
        for item in response["Items"]:
            if item["event_type"] == "project_requested":
                events.append(
                    ProjectRequested(
                        item["aggregate_id"],
                        item["aggregate_type"],
                        item["aggregate_version"],
                        UUID(item["event_id"]),
                        item["event_version"],
                        ProjectRequestedPayload(
                            json.loads(item["payload"])["project_id"],
                            int(json.loads(item["payload"])["requested_time"]),
                        ),
                        item["event_type"],
                    )
                )
            elif item["event_type"] == "project_created":
                events.append(
                    ProjectCreated(
                        item["aggregate_id"],
                        item["aggregate_type"],
                        item["aggregate_version"],
                        UUID(item["event_id"]),
                        item["event_version"],
                        ProjectCreatedPayload(
                            json.loads(item["payload"])["project_id"],
                            int(json.loads(item["payload"])["created_time"]),
                        ),
                        item["event_type"],
                    )
                )
            elif item["event_type"] == "resource_found_compliant":
                events.append(
                    ResourceFoundCompliant(
                        item["aggregate_id"],
                        item["aggregate_type"],
                        item["aggregate_version"],
                        UUID(item["event_id"]),
                        item["event_version"],
                        ResourceFoundCompliantPayload(
                            timestamp=int(json.loads(item["payload"])["timestamp"]),
                            container_id=json.loads(item["payload"])["container_id"],
                        ),
                        item["event_type"],
                    )
                )
            elif item["event_type"] == "resource_found_non_compliant":
                events.append(
                    ResourceFoundNonCompliant(
                        item["aggregate_id"],
                        item["aggregate_type"],
                        item["aggregate_version"],
                        UUID(item["event_id"]),
                        item["event_version"],
                        ResourceFoundNonCompliantPayload(
                            timestamp=int(json.loads(item["payload"])["timestamp"]),
                            container_id=json.loads(item["payload"])["container_id"],
                        ),
                        item["event_type"],
                    )
                )
            elif item["event_type"] == "patch_run_summary":
                events.append(
                    PatchRunSummary(
                        item["aggregate_id"],
                        item["aggregate_type"],
                        item["aggregate_version"],
                        UUID(item["event_id"]),
                        item["event_version"],
                        PatchRunSummaryPayload(
                            failed_instances=json.loads(item["payload"])[
                                "failed_instances"
                            ],
                            successful_instances=json.loads(item["payload"])[
                                "successful_instances"
                            ],
                        ),
                        item["event_type"],
                    )
                )

            elif item["event_type"] == "account_requested":
                events.append(
                    AccountRequested(
                        item["aggregate_id"],
                        item["aggregate_type"],
                        item["aggregate_version"],
                        UUID(item["event_id"]),
                        item["event_version"],
                        AccountRequestedPayload(
                            json.loads(item["payload"])["account_id"],
                            int(json.loads(item["payload"])["requested_time"]),
                        ),
                        item["event_type"],
                    )
                )
            elif item["event_type"] == "account_created":
                events.append(
                    AccountCreated(
                        item["aggregate_id"],
                        item["aggregate_type"],
                        item["aggregate_version"],
                        UUID(item["event_id"]),
                        item["event_version"],
                        AccountCreatedPayload(
                            json.loads(item["payload"])["account_id"],
                            int(json.loads(item["payload"])["created_time"]),
                        ),
                        item["event_type"],
                    )
                )
            elif item["event_type"] == "guardrail_passed":
                events.append(
                    GuardrailPassed(
                        item["aggregate_id"],
                        item["aggregate_type"],
                        item["aggregate_version"],
                        UUID(item["event_id"]),
                        item["event_version"],
                        GuardrailPassedPayload(
                            guardrail_id=json.loads(item["payload"])["guardrail_id"],
                            timestamp=int(json.loads(item["payload"])["timestamp"]),
                        ),
                        item["event_type"],
                    )
                )
            elif item["event_type"] == "guardrail_activated":
                events.append(
                    GuardrailActivated(
                        item["aggregate_id"],
                        item["aggregate_type"],
                        item["aggregate_version"],
                        UUID(item["event_id"]),
                        item["event_version"],
                        GuardrailActivatedPayload(
                            guardrail_id=json.loads(item["payload"])["guardrail_id"],
                            timestamp=int(json.loads(item["payload"])["timestamp"]),
                        ),
                        item["event_type"],
                    )
                )
            elif item["event_type"] == "identity_requested":
                events.append(
                    IdentityRequested(
                        item["aggregate_id"],
                        item["aggregate_type"],
                        item["aggregate_version"],
                        UUID(item["event_id"]),
                        item["event_version"],
                        IdentityRequestedPayload(
                            json.loads(item["payload"])["account_id"],
                            int(json.loads(item["payload"])["requested_time"]),
                        ),
                        item["event_type"],
                    )
                )
            elif item["event_type"] == "identity_created":
                events.append(
                    IdentityCreated(
                        item["aggregate_id"],
                        item["aggregate_type"],
                        item["aggregate_version"],
                        UUID(item["event_id"]),
                        item["event_version"],
                        IdentityCreatedPayload(
                            json.loads(item["payload"])["account_id"],
                            int(json.loads(item["payload"])["created_time"]),
                        ),
                        item["event_type"],
                    )
                )

        events.sort(key=self._sort_events)

        return events
