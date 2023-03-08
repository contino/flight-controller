from typing import Literal

from pydantic import BaseModel

from src.entities.base import BaseEvent, BaseMetric


# Events
class ResourceFoundNonCompliantPayload(BaseModel):
    container_id: str
    timestamp: float


class ResourceFoundNonCompliant(BaseEvent):
    aggregate_type = "Resource"
    event_version = 1
    payload: ResourceFoundNonCompliantPayload
    event_type: Literal["resource_found_non_compliant"] = "resource_found_non_compliant"


class ResourceFoundCompliantPayload(BaseModel):
    container_id: str
    timestamp: float


class ResourceFoundCompliant(BaseEvent):
    aggregate_type = "Resource"
    event_version = 1
    payload: ResourceFoundCompliantPayload
    event_type: Literal["resource_found_compliant"] = "resource_found_compliant"


# Metrics
class ResourceComplianceExtraDimensions(BaseModel):
    dimension_names: list[Literal["container_id"]]
    container_id: str


class ResourceComplianceLeadTime(BaseMetric):
    dimensions: ResourceComplianceExtraDimensions
    metric_type: Literal[
        "resource_compliance_lead_time"
    ] = "resource_compliance_lead_time"
