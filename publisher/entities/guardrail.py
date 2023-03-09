from dataclasses import dataclass
from typing import Union, Literal

from publisher.entities.base import BaseEvent


@dataclass
class GuardrailActivatedDetail():
    aggregate_id: str
    guardrail_id: str
    time: int
    event_type: Literal["guardrail_activated"] = "guardrail_activated"

@dataclass
class GuardrailActivated(BaseEvent):
    source: str
    detail: GuardrailActivatedDetail
    event_bus_name: Literal["main_lambda_bus_cdktf"] = "main_lambda_bus_cdktf"

@dataclass
class GuardrailPassedDetail():
    aggregate_id: str
    guardrail_id: str
    time: int
    event_type: Literal["guardrail_passed"] = "guardrail_passed"

@dataclass
class GuardrailPassed(BaseEvent):
    source: str
    detail: GuardrailPassedDetail
    event_bus_name: Literal["main_lambda_bus_cdktf"] = "main_lambda_bus_cdktf"
