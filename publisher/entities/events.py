from typing import Literal, Union

from publisher.entities.guardrail import (
    GuardrailActivated,
    GuardrailPassed,
)


Event = Union[
    GuardrailPassed,
    GuardrailActivated
    ]


Event_Type = Union[
    Literal["guardrail_passed"],
    Literal["guardrail_activated"]
]


EVENT_CLASSES = {
    "guardrail_activated": GuardrailActivated,
    "guardrail_passed": GuardrailPassed
}
