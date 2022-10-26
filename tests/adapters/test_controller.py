import json
import random
import string
from datetime import datetime
from uuid import uuid4

from src.adapters.controller import handle_event
from src.entities.projects import (
    ProjectCreated,
    ProjectLeadTime,
    ProjectRequested,
    ProjectRequestedPayload,
)

project_id = "".join(random.choices(string.ascii_letters, k=12))

project_requested_payload = {
    "project_id": project_id,
    "requested_time": datetime.utcnow().timestamp(),
    "event_type": "ProjectRequested",
}

project_created_payload = {
    "project_id": project_id,
    "created_time": datetime.utcnow().timestamp(),
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
        project_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(project_id, datetime.utcnow().timestamp()),
    )
    assert isinstance(
        handle_event(
            project_created_payload,
            [requested_event],
        )[0],
        ProjectCreated,
    )


def test_project_created_returns_lead_time():
    requested_event = ProjectRequested(
        project_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(project_id, datetime.utcnow().timestamp()),
    )
    assert handle_event(project_created_payload, [requested_event])[1] == [
        ProjectLeadTime(
            project_id,
            project_created_payload["created_time"]
            - requested_event.payload.requested_time,
        )
    ]


def test_project_created_handles_no_project_requested():
    assert isinstance(handle_event(project_created_payload, [])[0], ProjectCreated)


def test_project_created_returns_no_metric_with_no_project_requested():
    assert handle_event(project_created_payload, [])[1] == []


def test_project_handles_unknown_event():
    assert isinstance(
        handle_event(
            {
                "requested_time": 1659656680.789246,
                "project_id": "the-armitagency",
                "event_type": "NotAnEvent",
            },
            [],
        ),
        Exception,
    )


def test_project_handles_malformed_event():
    assert isinstance(
        handle_event(
            {
                "requested_time": 1659656680.789246,
                "project_id": "the-armitagency",
            },
            [],
        ),
        Exception,
    )
