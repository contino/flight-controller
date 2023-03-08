from typing import List, Dict, Tuple, Union
from uuid import uuid4

from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountLeadTime,
    AccountRequested,
    AccountRequestedPayload,
)
from src.entities.events import Event


def _convert_payload_to_event(
    event: Dict, aggregate_version: int
) -> Union[AccountCreated, AccountRequested]:
    if event["event_type"] == "account_requested":
        return AccountRequested(
            aggregate_id=event["aggregate_id"],
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=AccountRequestedPayload(timestamp=int(event["time"])),
        )
    elif event["event_type"] == "account_created":
        return AccountCreated(
            aggregate_id=event["aggregate_id"],
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=AccountCreatedPayload(timestamp=int(event["time"])),
        )


def handle_account_created(
    event: Dict, aggregate_events: List[Event]
) -> Tuple[AccountCreated, List[AccountLeadTime]]:
    event = _convert_payload_to_event(event, len(aggregate_events))
    if aggregate_events:
        return (
            event,
            [
                AccountLeadTime(
                    aggregate_id=event.aggregate_id,
                    metric_value=(
                        event.payload.timestamp - aggregate_events[0].payload.timestamp
                    ),
                )
            ],
        )
    return (event, [])


def handle_account_requested(
    event: Dict, aggregate_events: List[Event]
) -> Tuple[AccountRequested, List]:
    event = _convert_payload_to_event(event, len(aggregate_events))
    return (event, [])
