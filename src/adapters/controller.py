from typing import Any, List, Tuple, Union

from src.entities.events import Event
from src.entities.metrics import Metric
from src.usecases.event_functions import EVENT_FUNCTIONS


def handle_event(
    payload: Any, aggregate_events: List[Event]
) -> Union[Exception, Tuple[Event, List[Metric]]]:
    if "event_type" in payload:
        if payload["event_type"] in EVENT_FUNCTIONS:
            event, metrics = EVENT_FUNCTIONS[payload["event_type"]](
                payload, aggregate_events
            )
            return (event, metrics)
        else:
            return Exception(f"Unknown event type {payload['event_type']}")
    return Exception("Malformed event with no event_type")
