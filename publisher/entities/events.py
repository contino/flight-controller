from typing import Literal, Union

from publisher.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivatedDetail,
    GuardrailPassed,
    GuardrailPassedDetail,
)


Event = Union[
    GuardrailPassed,
    GuardrailActivated
    ]


Event_Type = Union[
    Literal["guardrail_passed"],
    Literal["guardrail_activated"]
]


Detail = Union[
    GuardrailActivatedDetail,
    GuardrailPassedDetail
]


EVENT_CLASSES = {
    "guardrail_activated": GuardrailActivated,
    "guardrail_passed": GuardrailPassed
}
