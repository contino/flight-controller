from dataclasses import dataclass
from typing import Literal

from .base import BaseEvent, BaseMetric

# Event
@dataclass
class GuardrailActivatedPayload:
    guardrail_id: str
    timestamp: float


@dataclass
class GuardrailActivated(BaseEvent):
    payload: GuardrailActivatedPayload
    eventVersion: int
    eventType: Literal["GuardrailActivated"] = "GuardrailActivated"


@dataclass
class GuardrailPassedPayload:
    guardrail_id: str
    timestamp: float


@dataclass
class GuardrailPassed(BaseEvent):
    payload: GuardrailPassedPayload
    eventVersion: int
    eventType: Literal["GuardrailPassed"] = "GuardrailPassed"


# Event Metrics
@dataclass
class GuardrailActivationCount(BaseMetric):
    guardrail_id: str
    count: int


@dataclass
class GuardrailMaxActivation(BaseMetric):
    guardrail_id: str
    count: int


@dataclass
class GuardrailLeadTime(BaseMetric):
    guardrail_id: str
    lead_time: float