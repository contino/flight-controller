from dataclasses import dataclass
from typing import Literal

from .base import BaseEvent, BaseMetric


@dataclass
class PatchRunSummaryPayload:
    failed_instances: str
    successful_instances: str


@dataclass
class PatchRunSummary(BaseEvent):
    payload: PatchRunSummaryPayload
    eventVersion: int
    eventType: Literal["PatchRunSummary"] = "PatchRunSummary"


@dataclass
class PatchCompliancePercentage(BaseMetric):
    percentage: float