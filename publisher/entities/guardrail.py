from dataclasses import dataclass
from typing import Literal

from publisher.entities.base import BaseEvent


@dataclass
class GuardrailActivated(BaseEvent):
    guardrail_id: str
    time: int
    event_type: Literal["guardrail_activated"] = "guardrail_activated"


@dataclass
class GuardrailPassed(BaseEvent):
    guardrail_id: str
    time: int
    event_type: Literal["guardrail_passed"] = "guardrail_passed"