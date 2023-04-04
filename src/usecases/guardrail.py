from typing import List, Union, Dict, Tuple
from uuid import uuid4

from src.entities.events import Event
from src.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivationCount,
    GuardrailExtraDimensions,
    GuardrailLeadTime,
    GuardrailMaxActivation,
    GuardrailPassed,
)


def handle_guardrail_activated(
    event: Event, aggregate_events: List[Event]
) -> Tuple[GuardrailActivated, List[GuardrailActivationCount]]:
    guardrail_activation_count = 1
    for aggregate_event in aggregate_events:
        if isinstance(aggregate_event, GuardrailActivated) and aggregate_event.payload.guardrail_id == event.payload.guardrail_id:
            guardrail_activation_count += 1
    return (
        event,
        [
            GuardrailActivationCount(
                aggregate_id=event.aggregate_id,
                dimensions=GuardrailExtraDimensions(
                    dimension_names=["guardrail_id"],
                    guardrail_id=event.payload.guardrail_id,
                ),
                metric_value=guardrail_activation_count,
            )
        ],
    )


def handle_guardrail_passed(
    event: Event, aggregate_events: List[Event]
) -> Tuple[GuardrailPassed, List[Union[GuardrailLeadTime, GuardrailMaxActivation]]]:
    last_compliant_event = 0
    activations_since_last_pass = 0
    for i, aggregate_event in enumerate(aggregate_events):
        if isinstance(aggregate_event, GuardrailPassed) and aggregate_event.payload.guardrail_id == event.payload.guardrail_id:
            last_compliant_event = i
            activations_since_last_pass = 0
        elif isinstance(aggregate_event, GuardrailActivated) and aggregate_event.payload.guardrail_id == event.payload.guardrail_id:
            activations_since_last_pass += 1
    for aggregate_event in aggregate_events[last_compliant_event:]:
        if isinstance(aggregate_event, GuardrailActivated) and aggregate_event.payload.guardrail_id == event.payload.guardrail_id:
            return (
                event,
                [
                    GuardrailLeadTime(
                        aggregate_id=event.aggregate_id,
                        dimensions=GuardrailExtraDimensions(
                            dimension_names=["guardrail_id"],
                            guardrail_id=event.payload.guardrail_id,
                        ),
                        metric_value=(
                            event.payload.timestamp - aggregate_event.payload.timestamp
                        ),
                    ),
                    GuardrailMaxActivation(
                        aggregate_id=event.aggregate_id,
                        dimensions=GuardrailExtraDimensions(
                            dimension_names=["guardrail_id"],
                            guardrail_id=event.payload.guardrail_id,
                        ),
                        metric_value=activations_since_last_pass,
                    ),
                ],
            )
    return (event, [])
