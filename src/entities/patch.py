from typing import Literal

from pydantic import BaseModel

from src.entities.base import BaseEvent, BaseMetric


# Events
class PatchRunSummaryPayload(BaseModel):
    timestamp: float
    failed_instances: str
    successful_instances: str


class PatchRunSummary(BaseEvent):
    aggregate_type: Literal["Account"] = "Account"
    event_version: Literal[1] = 1
    payload: PatchRunSummaryPayload
    event_type: Literal["patch_run_summary"] = "patch_run_summary"


# Event Metrics
class PatchCompliancePercentage(BaseMetric):
    metric_type: Literal["patch_compliance_percentage"] = "patch_compliance_percentage"
