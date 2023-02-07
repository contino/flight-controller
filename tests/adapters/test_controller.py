import random
import string
from datetime import datetime
from uuid import uuid4

from src.adapters.controller import handle_event
from src.entities.compliance import (
    ResourceComplianceLeadTime,
    ResourceFoundCompliant,
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)
from src.entities.projects import (
    ProjectCreated,
    ProjectAssigned,
    ProjectCreatedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
    ProjectLeadTime,
    ProjectAssignedLeadTime,
)

aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
event_time = int(round(datetime.utcnow().timestamp()))
project_requested_payload = {
    "aggregate_id": aggregate_id,
    "time": event_time,
    "event_type": "ProjectRequested",
}

project_assigned_payload = {
    "aggregate_id": aggregate_id,
    "time": event_time,
    "event_type": "ProjectAssigned",
}

project_created_payload = {
    "aggregate_id": aggregate_id,
    "time": event_time,
    "event_type": "ProjectCreated",
}


def test_project_requested_returns_no_metrics():
    assert (
        handle_event(
            project_requested_payload,
            [],
        )[1]
        == []
    )


def test_project_requested_returns_correct_event():
    assert isinstance(
        handle_event(
            project_requested_payload,
            [],
        )[0],
        ProjectRequested,
    )


def test_project_created_returns_correct_event():
    requested_event = ProjectRequested(
        aggregate_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(aggregate_id, event_time),
    )
    assert isinstance(
        handle_event(
            project_created_payload,
            [requested_event],
        )[0],
        ProjectCreated,
    )


def test_project_assigned_returns_correct_event():
    requested_event = ProjectRequested(
        aggregate_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(aggregate_id, event_time),
    )
    assert isinstance(
        handle_event(
            project_assigned_payload,
            [requested_event],
        )[0],
        ProjectAssigned,
    )


def test_project_created_returns_lead_time():
    requested_event = ProjectRequested(
        aggregate_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(aggregate_id, event_time),
    )
    assert handle_event(project_created_payload, [requested_event])[1] == [
        ProjectLeadTime(aggregate_id, 0)
    ]


def test_project_assigned_returns_lead_time():
    requested_event = ProjectRequested(
        aggregate_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(aggregate_id, event_time),
    )
    assert handle_event(project_assigned_payload, [requested_event])[1] == [
        ProjectAssignedLeadTime(aggregate_id, 0)
    ]


def test_project_assigned_returns_lead_time_with_multiple_aggregates():
    requested_event = ProjectRequested(
        aggregate_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(aggregate_id, event_time),
    )

    created_event = ProjectCreated(
        aggregate_id,
        "Project",
        2,
        uuid4(),
        1,
        ProjectCreatedPayload(aggregate_id, event_time),
    )
    assert handle_event(project_assigned_payload, [created_event, requested_event])[
        1
    ] == [ProjectAssignedLeadTime(aggregate_id, 0)]


def test_project_created_handles_no_project_requested():
    assert isinstance(handle_event(project_created_payload, [])[0], ProjectCreated)


def test_project_assigned_handles_no_project_requested():
    assert isinstance(handle_event(project_assigned_payload, [])[0], ProjectAssigned)


def test_project_created_returns_no_metric_with_no_project_requested():
    assert handle_event(project_created_payload, [])[1] == []


def test_project_assigned_returns_no_metric_with_no_project_requested():
    assert handle_event(project_assigned_payload, [])[1] == []


def test_project_assigned_returns_no_metric_with_no_project_requested():
    assert handle_event(project_assigned_payload, [])[1] == []


def test_resource_non_compliant_returns_correct_type():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "container_id": "123456789012",
                "time": event_time,
                "event_type": "ResourceFoundNonCompliant",
            },
            [],
        )[0],
        ResourceFoundNonCompliant,
    )


def test_resource_non_compliant_returns_no_metric():
    assert (
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "container_id": "123456789012",
                "time": event_time,
                "event_type": "ResourceFoundNonCompliant",
            },
            [],
        )[1]
        == []
    )


def test_resource_compliant_returns_correct_type():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "container_id": "123456789012",
                "time": event_time,
                "event_type": "ResourceFoundCompliant",
            },
            [],
        )[0],
        ResourceFoundCompliant,
    )


def test_resource_compliant_returns_metric():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "container_id": "123456789012",
                "time": event_time,
                "event_type": "ResourceFoundCompliant",
            },
            [
                ResourceFoundNonCompliant(
                    aggregate_id,
                    "Resource",
                    1,
                    uuid4(),
                    1,
                    ResourceFoundNonCompliantPayload(
                        container_id="123456789012", timestamp=event_time
                    ),
                )
            ],
        )[1][0],
        ResourceComplianceLeadTime,
    )


def test_handles_unknown_event():
    assert isinstance(
        handle_event(
            {
                "requested_time": 1659656680.789246,
                "aggregate_id": "the-armitagency",
                "event_type": "NotAnEvent",
            },
            [],
        ),
        Exception,
    )


def test_handles_malformed_event():
    assert isinstance(
        handle_event(
            {
                "requested_time": 1659656680.789246,
                "aggregate_id": "the-armitagency",
            },
            [],
        ),
        Exception,
    )
