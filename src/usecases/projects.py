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



def handle_project_requested(
    event: Event, aggregate_events: List[Event]
) -> Tuple[ProjectRequested, List]:
    return (event, [])


def handle_project_assigned(
    event: Event, aggregate_events: List[Event]
) -> Tuple[ProjectAssigned, List[ProjectAssignedLeadTime]]:
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
    event: Event, aggregate_events: List[Event]
) -> Tuple[ProjectCreated, List[ProjectLeadTime]]:
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
