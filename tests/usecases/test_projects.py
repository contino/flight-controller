from datetime import datetime
from uuid import uuid4

from src.usecases.projects import handle_project_created
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectLeadTime,
    ProjectRequestedPayload,
    ProjectRequested,
)

projectRequested = ProjectRequested(
    aggregateId="test-project",
    aggregateType="Project",
    aggregateVersion=1,
    eventId=uuid4(),
    eventVersion=1,
    payload=ProjectRequestedPayload(
        "test-project", datetime(2022, 8, 2, 10, 0, 0).timestamp()
    ),
)
projectCreated = ProjectCreated(
    aggregateId="test-project",
    aggregateType="Project",
    aggregateVersion=2,
    eventId=uuid4(),
    eventVersion=1,
    payload=ProjectCreatedPayload(
        "test-project", datetime(2022, 8, 2, 11, 0, 0).timestamp()
    ),
)


def test_create_project_returns_correct_type():
    assert isinstance(
        handle_project_created(projectRequested, projectCreated), ProjectLeadTime
    )


def test_create_project_calculates_lead_time_correctly():
    assert handle_project_created(projectRequested, projectCreated).lead_time == 3600
