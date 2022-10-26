from typing import Any, Dict, List, Tuple, Union
from uuid import uuid4

from src.entities.events import Event, EventType
from src.entities.metrics import Metric
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
)
from src.usecases.projects import handle_project_created


def _convert_payload_to_event(
    payload: Dict[str, Any], event_type: EventType, aggregateVersion: int
) -> Event:
    if event_type == "ProjectRequested":
        return ProjectRequested(
            aggregateId=payload["project_id"],
            aggregateType="Project",
            aggregateVersion=aggregateVersion + 1,
            eventId=uuid4(),
            eventVersion=1,
            payload=ProjectRequestedPayload(
                payload["project_id"],
                payload["requested_time"],
            ),
        )
    else:
        return ProjectCreated(
            aggregateId=payload["project_id"],
            aggregateType="Project",
            aggregateVersion=aggregateVersion + 1,
            eventId=uuid4(),
            eventVersion=1,
            payload=ProjectCreatedPayload(
                payload["project_id"],
                payload["created_time"],
            ),
        )


def handle_event(
    payload: Any, aggregate_events: List[Event]
) -> Union[Exception, Tuple[Event, List[Metric]]]:
    if "event_type" in payload:
        if payload["event_type"] == "ProjectRequested":
            return (
                _convert_payload_to_event(
                    payload, payload["event_type"], len(aggregate_events)
                ),
                [],
            )
        elif payload["event_type"] == "ProjectCreated":
            event = _convert_payload_to_event(
                payload, payload["event_type"], len(aggregate_events)
            )
            for aggregate_event in aggregate_events:
                if isinstance(aggregate_event, ProjectRequested):
                    return (
                        event,
                        [handle_project_created(aggregate_event, event)],
                    )
            return (event, [])
        else:
            return Exception(f"Unknown event type: {payload['event_type']}")
    return Exception("Malformed event with no event_type")
