from time import time
from uuid import uuid4

from src.entities.projects import (
    ProjectAssigned,
    ProjectAssignedLeadTime,
    ProjectCreated,
    ProjectLeadTime,
    ProjectRequestedPayload,
    ProjectRequested,
)
from src.usecases.projects import (
    handle_project_assigned,
    handle_project_created,
    handle_project_requested,
)

requested_aggregate_event = ProjectRequested(
    aggregate_id=str(uuid4()),
    event_id=str(uuid4()),
    event_type="project_requested",
    aggregate_version=1,
    event_version=1,
    payload=ProjectRequestedPayload(timestamp=int(time())),
)

created_event = {
    "event_type": "project_created",
    "aggregate_id": requested_aggregate_event.aggregate_id,
    "time": int(requested_aggregate_event.payload.timestamp + 10),
}

assigned_event = {
    "event_type": "project_assigned",
    "aggregate_id": requested_aggregate_event.aggregate_id,
    "time": int(requested_aggregate_event.payload.timestamp + 10),
}

requested_event = {
    "event_type": "project_requested",
    "aggregate_id": requested_aggregate_event.aggregate_id,
    "time": int(time()),
}


def test_handle_project_requested_returns_correct_event_type():
    assert isinstance(
        handle_project_requested(requested_event, [])[0], ProjectRequested
    )


def test_handle_project_requested_returns_no_metric():
    assert len(handle_project_requested(requested_event, [])[1]) == 0


def test_handle_project_assigned_returns_correct_event_type():
    assert isinstance(
        handle_project_assigned(assigned_event, [requested_aggregate_event])[0],
        ProjectAssigned,
    )


def test_handle_project_assigned_returns_correct_metric_type():
    assert isinstance(
        handle_project_assigned(assigned_event, [requested_aggregate_event])[1][0],
        ProjectAssignedLeadTime,
    )


def test_handle_project_assigned_returns_correct_metric_value():
    assert (
        handle_project_assigned(assigned_event, [requested_aggregate_event])[1][
            0
        ].metric_value
        == 10
    )


def test_handle_project_created_returns_correct_event_type():
    assert isinstance(
        handle_project_created(created_event, [requested_aggregate_event])[0],
        ProjectCreated,
    )


def test_handle_project_created_returns_correct_metric_type():
    assert isinstance(
        handle_project_created(created_event, [requested_aggregate_event])[1][0],
        ProjectLeadTime,
    )


def test_handle_project_created_returns_correct_metric_value():
    assert (
        handle_project_created(created_event, [requested_aggregate_event])[1][
            0
        ].metric_value
        == 10
    )
