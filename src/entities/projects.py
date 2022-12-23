from dataclasses import dataclass
from typing import Literal

from .base import BaseEvent


@dataclass
class ProjectRequestedPayload:
    project_id: str
    requested_time: float


@dataclass
class ProjectRequested(BaseEvent):
    payload: ProjectRequestedPayload
    eventVersion: int
    eventType: Literal["ProjectRequested"] = "ProjectRequested"

@dataclass
class ProjectAssignedPayload:
    project_id: str
    assigned_time: float


@dataclass
class ProjectAssigned(BaseEvent):
    payload: ProjectAssignedPayload
    eventVersion: int
    eventType: Literal["ProjectAssigned"] = "ProjectAssigned"


@dataclass
class ProjectCreatedPayload:
    project_id: str
    created_time: float


@dataclass
class ProjectCreated(BaseEvent):
    payload: ProjectCreatedPayload
    eventVersion: int
    eventType: Literal["ProjectCreated"] = "ProjectCreated"


@dataclass
class ProjectLeadTime:
    project_id: str
    lead_time: float

@dataclass
class ProjectAssignedLeadTime:
    project_id: str
    lead_time: float

