from typing import Literal

from pydantic import BaseModel

from src.entities.base import BaseEvent, BaseMetric


# Events
class GuardrailActivatedPayload(BaseModel):
    guardrail_id: str
    timestamp: float


class GuardrailActivated(BaseEvent):
    aggregate_type = "Resource"
    event_version = 1
    payload: GuardrailActivatedPayload
    event_type: Literal["guardrail_activated"] = "guardrail_activated"


class GuardrailPassedPayload(BaseModel):
    guardrail_id: str
    timestamp: float


class GuardrailPassed(BaseEvent):
    aggregate_type = "Resource"
    event_version = 1
    payload: GuardrailPassedPayload
    event_type: Literal["guardrail_passed"] = "guardrail_passed"


# Event Metrics
class GuardrailExtraDimensions(BaseModel):
    dimension_names: list[Literal["guardrail_id"]]
    guardrail_id: str


class GuardrailActivationCount(BaseMetric):
    dimensions: GuardrailExtraDimensions
    metric_type: Literal["guardrail_activation_count"] = "guardrail_activation_count"


class GuardrailMaxActivation(BaseMetric):
    dimensions: GuardrailExtraDimensions
    metric_type: Literal["guardrail_max_activation"] = "guardrail_max_activation"


class GuardrailLeadTime(BaseMetric):
    dimensions: GuardrailExtraDimensions
    metric_type: Literal["guardrail_lead_time"] = "guardrail_lead_time"
