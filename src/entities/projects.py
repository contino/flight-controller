from typing import Literal

from pydantic import BaseModel

from src.entities.base import BaseEvent, BaseMetric


# Event
class ProjectRequestedPayload(BaseModel):
    timestamp: float


class ProjectRequested(BaseEvent):
    aggregate_type = "Account"
    event_version = 1
    payload: ProjectRequestedPayload
    event_type: Literal["project_requested"] = "project_requested"


class ProjectAssignedPayload(BaseModel):
    timestamp: float


class ProjectAssigned(BaseEvent):
    aggregate_type = "Account"
    event_version = 1
    payload: ProjectAssignedPayload
    event_type: Literal["project_assigned"] = "project_assigned"


class ProjectCreatedPayload(BaseModel):
    timestamp: float


class ProjectCreated(BaseEvent):
    aggregate_type = "Account"
    event_version = 1
    payload: ProjectCreatedPayload
    event_type: Literal["project_created"] = "project_created"


# Event Metrics
class ProjectLeadTime(BaseMetric):
    metric_type: Literal["project_lead_time"] = "project_lead_time"


class ProjectAssignedLeadTime(BaseMetric):
    metric_type: Literal["project_assigned_lead_time"] = "project_assigned_lead_time"
