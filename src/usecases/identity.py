from typing import List, Tuple, Union

from src.entities.events import Event
from src.entities.identity import (
    IdentityLeadTime,
    IdentityRequested,
)


def handle_identity_requested(
    event: Event, aggregate_events: List[Event]
) -> Tuple[IdentityRequested, List]:
    return (event, [])


def handle_identity_created(
    event: Event, aggregate_events: List[Event]
) -> Tuple[IdentityRequested, List]:
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
