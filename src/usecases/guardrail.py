from typing import List, Optional, Union

from src.entities.events import Event

from src.entities.guardrail import (
    GuardrailPassed,
    GuardrailActivated,
    GuardrailActivationCount,
    GuardrailMaxActivation,
    GuardrailLeadTime
)


def handle_guardrail_activated(
    event: GuardrailActivated, events: List[Union[GuardrailActivated, GuardrailPassed]]
) -> Optional[GuardrailActivationCount]:
    gaurdrail_activation_count = 1
    for aggregate_event in events:
        if isinstance(aggregate_event, GuardrailActivated):
            gaurdrail_activation_count += 1
    return GuardrailActivationCount(
        event.aggregateId,
        event.payload.guardrail_id,
        gaurdrail_activation_count
    )

def handle_guardrail_passed(
    event: GuardrailPassed, events: List[Union[GuardrailActivated, GuardrailPassed]]
) -> List[Optional[Union[GuardrailLeadTime, GuardrailMaxActivation]]]:
    last_compliant_event = 0
    for i, aggregate_event in enumerate(events):
        if isinstance(aggregate_event, GuardrailPassed):
            last_compliant_event = i
    for aggregate_event in events[last_compliant_event:]:
        if isinstance(aggregate_event, GuardrailActivated):
            return [GuardrailLeadTime(
                event.aggregateId,
                event.payload.guardrail_id,
                (event.payload.timestamp - aggregate_event.payload.timestamp),
            ),
            GuardrailMaxActivation(
                event.aggregateId,
                event.payload.guardrail_id,
                len(events[last_compliant_event + 1:]) if last_compliant_event > 0 else len(events[last_compliant_event:]) 
            )
            ]
    return None
