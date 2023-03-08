from typing import Dict, List, Tuple, Union
from uuid import uuid4
from src.entities.events import Event
from src.entities.identity import (
    IdentityCreated,
    IdentityCreatedPayload,
    IdentityLeadTime,
    IdentityRequested,
    IdentityRequestedPayload,
)


def _convert_payload_to_event(
    event: Dict, aggregate_version: int
) -> Union[IdentityRequested, IdentityCreated]:
    if event["event_type"] == "identity_requested":
        return IdentityRequested(
            aggregate_id=event["aggregate_id"],
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=IdentityRequestedPayload(
                timestamp=int(event["time"]), account_id=event["account_id"]
            ),
        )
    elif event["event_type"] == "identity_created":
        return IdentityCreated(
            aggregate_id=event["aggregate_id"],
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=IdentityCreatedPayload(
                timestamp=int(event["time"]), account_id=event["account_id"]
            ),
        )


def handle_identity_requested(
    event: Dict, aggregate_events: List[Event]
) -> Tuple[IdentityRequested, List]:
    event = _convert_payload_to_event(event, len(aggregate_events))
    return (event, [])


def handle_identity_created(
    event: Dict, aggregate_events: List[Event]
) -> Tuple[IdentityRequested, List]:
    event = _convert_payload_to_event(event, len(aggregate_events))
    return (
        event,
        [
            IdentityLeadTime(
                aggregate_id=event.aggregate_id,
                metric_value=(
                    event.payload.timestamp - aggregate_events[0].payload.timestamp
                ),
            )
        ],
    )
