from dataclasses import dataclass
from typing import Literal

from src.entities.base import BaseEvent, BaseMetric


@dataclass
class ProjectRequestedPayload:
    project_id: str
    requested_time: float


@dataclass
class ProjectRequested(BaseEvent):
    payload: ProjectRequestedPayload
    event_type: Literal["project_requested"] = "project_requested"


@dataclass
class ProjectAssignedPayload:
    project_id: str
    assigned_time: float


@dataclass
class ProjectAssigned(BaseEvent):
    payload: ProjectAssignedPayload
    event_type: Literal["project_assigned"] = "project_assigned"


@dataclass
class ProjectCreatedPayload:
    project_id: str
    created_time: float


@dataclass
class ProjectCreated(BaseEvent):
    payload: ProjectCreatedPayload
    event_type: Literal["project_created"] = "project_created"


@dataclass
class ProjectLeadTime(BaseMetric):
    lead_time: float
    metric_type: Literal["project_lead_time"] = "project_lead_time"


@dataclass
class ProjectAssignedLeadTime(BaseMetric):
    lead_time: float
    metric_type: Literal["project_assigned_leadTime"] = "project_assigned_lead_time"
