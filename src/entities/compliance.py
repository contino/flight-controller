from dataclasses import dataclass
from typing import Literal

from src.entities.base import BaseEvent, BaseMetric


@dataclass
class ResourceFoundNonCompliantPayload:
    container_id: str
    timestamp: float


@dataclass
class ResourceFoundNonCompliant(BaseEvent):
    payload: ResourceFoundNonCompliantPayload
    event_type: Literal["resource_found_non_compliant"] = "resource_found_non_compliant"


@dataclass
class ResourceFoundCompliantPayload:
    container_id: str
    timestamp: float


@dataclass
class ResourceFoundCompliant(BaseEvent):
    payload: ResourceFoundCompliantPayload
    event_type: Literal["resource_found_compliant"] = "resource_found_compliant"


@dataclass
class ResourceComplianceLeadTime(BaseMetric):
    lead_time: float
    metric_type: Literal["resource_compliance_lead_time"] = "resource_compliance_lead_time"
