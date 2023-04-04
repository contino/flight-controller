from typing import List, Tuple

from src.entities.accounts import (
    AccountCreated,
    AccountLeadTime,
    AccountRequested,
)
from src.entities.events import Event


def handle_account_created(
    event: Event, aggregate_events: List[Event]
) -> Tuple[AccountCreated, List[AccountLeadTime]]:
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
    event: Event, aggregate_events: List[Event]
) -> Tuple[AccountRequested, List]:
    return (event, [])
