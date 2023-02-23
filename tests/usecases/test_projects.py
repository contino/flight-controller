from datetime import datetime
from uuid import uuid4

import pytest

from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectLeadTime,
    ProjectRequestedPayload,
    ProjectRequested,
)
from src.usecases.projects import handle_project_created

event = ProjectRequested(
    aggregate_id="test-project",
    aggregate_type="Project",
    aggregate_version=1,
    event_id=uuid4(),
    event_version=1,
    payload=ProjectRequestedPayload(
        "test-project", int(round(datetime(2022, 8, 2, 10, 0, 0).timestamp()))
    ),
)

created_event = ProjectCreated(
    aggregate_id="test-project",
    aggregate_type="Project",
    aggregate_version=2,
    event_id=uuid4(),
    event_version=1,
    payload=ProjectCreatedPayload(
        "test-project", int(round(datetime(2022, 8, 2, 12, 0, 0).timestamp()))
    ),
)


@pytest.fixture
def ProjectCreated():
    return handle_project_created(event, created_event)


def test_create_project_returns_correct_type(ProjectCreated):
    assert isinstance(ProjectCreated, ProjectLeadTime)


def test_create_project_calculates_lead_time_correctly(ProjectCreated):
    assert ProjectCreated.lead_time == 7200
