from dataclasses import dataclass
from typing import Literal

from .base import BaseEvent, BaseMetric


@dataclass
class ProjectRequestedPayload:
    project_id: str
    requested_time: float


@dataclass
class ProjectRequested(BaseEvent):
    payload: ProjectRequestedPayload
    eventType: Literal["ProjectRequested"] = "ProjectRequested"


@dataclass
class ProjectAssignedPayload:
    project_id: str
    assigned_time: float


@dataclass
class ProjectAssigned(BaseEvent):
    payload: ProjectAssignedPayload
    eventType: Literal["ProjectAssigned"] = "ProjectAssigned"


@dataclass
class ProjectCreatedPayload:
    project_id: str
    created_time: float


@dataclass
class ProjectCreated(BaseEvent):
    payload: ProjectCreatedPayload
    eventType: Literal["ProjectCreated"] = "ProjectCreated"


@dataclass
class ProjectLeadTime(BaseMetric):
    lead_time: float
    metricType: Literal["ProjectLeadTime"] = "ProjectLeadTime"


@dataclass
class ProjectAssignedLeadTime(BaseMetric):
    lead_time: float
    metricType: Literal["ProjectAssignedLeadTime"] = "ProjectAssignedLeadTime"
