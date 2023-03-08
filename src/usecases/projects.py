from typing import List, Dict, Union, Tuple
from uuid import uuid4

from src.entities.events import Event
from src.entities.projects import (
    ProjectAssigned,
    ProjectAssignedLeadTime,
    ProjectAssignedPayload,
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectLeadTime,
    ProjectRequested,
    ProjectRequestedPayload,
)


def _convert_payload_to_event(
    event: Dict, aggregate_version: int
) -> Union[ProjectAssigned, ProjectCreated, ProjectRequested]:
    if event["event_type"] == "project_assigned":
        return ProjectAssigned(
            aggregate_id=event["aggregate_id"],
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=ProjectAssignedPayload(timestamp=int(event["time"])),
        )
    elif event["event_type"] == "project_created":
        return ProjectCreated(
            aggregate_id=event["aggregate_id"],
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=ProjectCreatedPayload(timestamp=int(event["time"])),
        )
    elif event["event_type"] == "project_requested":
        return ProjectRequested(
            aggregate_id=event["aggregate_id"],
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=ProjectRequestedPayload(timestamp=int(event["time"])),
        )


def handle_project_requested(
    event: Dict, aggregate_events: List[Event]
) -> Tuple[ProjectRequested, List]:
    event = _convert_payload_to_event(event, len(aggregate_events))
    return (event, [])


def handle_project_assigned(
    event: Dict, aggregate_events: List[Event]
) -> Tuple[ProjectAssigned, List[ProjectAssignedLeadTime]]:
    event = _convert_payload_to_event(event, len(aggregate_events))
    if aggregate_events:
        return (
            event,
            [
                ProjectAssignedLeadTime(
                    aggregate_id=event.aggregate_id,
                    metric_value=(
                        event.payload.timestamp - aggregate_events[0].payload.timestamp
                    ),
                )
            ],
        )
    return (event, [])


def handle_project_created(
    event: Dict, aggregate_events: List[Event]
) -> Tuple[ProjectCreated, List[ProjectLeadTime]]:
    event = _convert_payload_to_event(event, len(aggregate_events))
    if aggregate_events:
        return (
            event,
            [
                ProjectLeadTime(
                    aggregate_id=event.aggregate_id,
                    metric_value=(
                        event.payload.timestamp - aggregate_events[0].payload.timestamp
                    ),
                )
            ],
        )
    return (event, [])
