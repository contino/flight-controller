from typing import Any, Dict, List, Tuple, Union
from uuid import uuid4


from src.entities.events import Event, EventType
from src.entities.metrics import Metric
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectAssigned,
    ProjectAssignedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
)

from src.usecases.projects import handle_project_created, handle_project_assigned


def _convert_payload_to_event(
    payload: Dict[str, Any], event_type: EventType, aggregateVersion: int
) -> Event:
    if event_type == "ProjectRequested":
        return ProjectRequested(
            aggregateId=payload["correlation_id"],
            aggregateType="Project",
            aggregateVersion=aggregateVersion + 1,
            eventId=str(uuid4()),
            eventVersion=1,
            payload=ProjectRequestedPayload(
                payload["correlation_id"],
                int(payload["time"])
            ),
        )
    elif event_type == "ProjectAssigned":
        return ProjectAssigned(
            aggregateId=payload["correlation_id"],
            aggregateType="Project",
            aggregateVersion=aggregateVersion + 1,
            eventId=str(uuid4()),
            eventVersion=1,
            payload=ProjectAssignedPayload(
                payload["correlation_id"],
                int(payload["time"])
            ),
        )
    elif event_type == "ProjectCreated":
        return ProjectCreated(
            aggregateId=payload["correlation_id"],
            aggregateType="Project",
            aggregateVersion=aggregateVersion + 1,
            eventId=str(uuid4()),
            eventVersion=1,
            payload=ProjectCreatedPayload(
                payload["correlation_id"],
                int(payload["time"])
            ),
        )


def handle_event(
    payload: Any, aggregate_events: List[Event]
) -> Union[Exception, Tuple[Event, List[Metric]]]:
    if "event_type" in payload:
        event = _convert_payload_to_event(
                payload, payload["event_type"], len(aggregate_events)
        )
        if isinstance(event, ProjectRequested):
            return (event,[])
        elif payload["event_type"] in ["ProjectCreated","ProjectAssigned"]:
            metrics = []
            for aggregate_event in aggregate_events:
                if payload["event_type"] == "ProjectCreated" and isinstance(aggregate_event, ProjectRequested):
                    metrics.append(handle_project_created(aggregate_event, event))
                elif payload["event_type"] == "ProjectAssigned" and isinstance(aggregate_event, ProjectRequested):
                    metrics.append(handle_project_assigned(aggregate_event, event))
            return (event, metrics)
        else:
            return Exception(f"Unknown Event type {payload['event_type']}")
    return Exception("Malformed event with no event_type")
