from datetime import datetime
from uuid import uuid4
import pytest

from src.usecases.projects import handle_project_created, handle_project_assigned
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectAssigned,
    ProjectAssignedPayload,
    ProjectRequestedPayload,
    ProjectRequested,
    ProjectLeadTime,
    ProjectAssignedLeadTime
)

projectRequested = ProjectRequested(
    aggregateId="test-project",
    aggregateType="Project",
    aggregateVersion=1,
    eventId=uuid4(),
    eventVersion=1,
    payload=ProjectRequestedPayload(
        "test-project", int(round(datetime(2022, 8, 2, 10, 0, 0).timestamp()))
    ),
)

projectAssigned = ProjectAssigned(
    aggregateId="test-project",
    aggregateType="Project",
    aggregateVersion=1,
    eventId=uuid4(),
    eventVersion=1,
    payload=ProjectAssignedPayload(
        "test-project", int(round(datetime(2022, 8, 2, 11, 0, 0).timestamp()))
    ),
)

projectCreated = ProjectCreated(
    aggregateId="test-project",
    aggregateType="Project",
    aggregateVersion=2,
    eventId=uuid4(),
    eventVersion=1,
    payload=ProjectCreatedPayload(
        "test-project", int(round(datetime(2022, 8, 2, 12, 0, 0).timestamp()))
    ),
)

@pytest.fixture
def project_created():
    return handle_project_created(projectRequested, projectCreated)

@pytest.fixture
def project_assigned():
    return handle_project_assigned(projectRequested, projectAssigned)


def test_create_project_returns_correct_type(project_created):
    assert isinstance(
        project_created, ProjectLeadTime
    )


def test_create_project_calculates_lead_time_correctly(project_created):
    assert project_created.lead_time == 7200

def test_assign_project_returns_correct_type(project_assigned):
    assert isinstance(
        project_assigned, ProjectAssignedLeadTime
    )


def test_assign_project_calculates_lead_time_correctly(project_assigned):
    assert project_assigned.lead_time == 3600
