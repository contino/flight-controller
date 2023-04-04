from typing import Dict, List, Tuple, Union
from uuid import uuid4

from src.entities.events import Event, EVENT_CLASSES
from src.entities.metrics import Metric
from src.usecases.event_functions import EVENT_FUNCTIONS

def _convert_payload_to_event(
    payload: Dict, aggregate_version: int
) -> Event:
    try:
        event_type = payload["event_type"]
        aggregate_id = payload["aggregate_id"]
        event_payload = payload.copy()
        for key in ["event_type", "aggregate_id"]:
            event_payload.pop(key, None)
        event_class, payload_class = EVENT_CLASSES[event_type]
        return event_class(
            aggregate_id=aggregate_id,
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            payload=payload_class(**event_payload)
        )
    except Exception as err:
        return err

def handle_event(
    payload: Dict, aggregate_events: List[Event]
) -> Union[Exception, Tuple[Event, List[Metric]]]:
    if "event_type" in payload:
        event_type = payload["event_type"]
        if event_type in EVENT_CLASSES:
            event = _convert_payload_to_event(payload, len(aggregate_events))
            if event_type in EVENT_FUNCTIONS:
                event, metrics = EVENT_FUNCTIONS[event_type](
                    event, aggregate_events
                )
                return (event, metrics)
            else:
                return Exception(f"No event type function defined: {event_type}")
        else:
            return Exception(f"Unknown event type {event_type}")
    return Exception("Malformed event with no event_type")
