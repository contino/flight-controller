from dataclasses import dataclass
from typing import Literal

from src.entities.base import BaseEvent, BaseMetric

# Event
@dataclass
class GuardrailActivatedPayload:
    guardrail_id: str
    timestamp: float


@dataclass
class GuardrailActivated(BaseEvent):
    payload: GuardrailActivatedPayload
    event_type: Literal["guardrail_activated"] = "guardrail_activated"


@dataclass
class GuardrailPassedPayload:
    guardrail_id: str
    timestamp: float


@dataclass
class GuardrailPassed(BaseEvent):
    payload: GuardrailPassedPayload
    event_type: Literal["guardrail_passed"] = "guardrail_passed"


# Event Metrics
@dataclass
class GuardrailActivationCount(BaseMetric):
    guardrail_id: str
    count: int
    metric_type: Literal["guardrail_activation_count"] = "guardrail_activation_count"


@dataclass
class GuardrailMaxActivation(BaseMetric):
    guardrail_id: str
    count: int
    metric_type: Literal["guardrail_max_activation"] = "guardrail_max_activation"


@dataclass
class GuardrailLeadTime(BaseMetric):
    guardrail_id: str
    lead_time: float
    metric_type: Literal["guardrail_lead_time"] = "guardrail_lead_time"