from dataclasses import dataclass
from typing import Literal

from src.entities.base import BaseEvent, BaseMetric


@dataclass
class PatchRunSummaryPayload:
    failed_instances: str
    successful_instances: str


@dataclass
class PatchRunSummary(BaseEvent):
    payload: PatchRunSummaryPayload
    event_type: Literal["patch_run_summary"] = "patch_run_summary"


@dataclass
class PatchCompliancePercentage(BaseMetric):
    percentage: float
    metric_type: Literal["patch_compliance_percentage"] = "patch_compliance_percentage"