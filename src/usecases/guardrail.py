from typing import List, Union, Dict, Tuple
from uuid import uuid4

from src.entities.events import Event
from src.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivationCount,
    GuardrailActivatedPayload,
    GuardrailExtraDimensions,
    GuardrailLeadTime,
    GuardrailMaxActivation,
    GuardrailPassed,
    GuardrailPassedPayload,
)


def _convert_payload_to_event(
    event: Dict, aggregate_version: int
) -> Union[GuardrailActivated, GuardrailPassed]:
    if event["event_type"] == "guardrail_passed":
        return GuardrailPassed(
            aggregate_id=event["aggregate_id"],
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            payload=GuardrailPassedPayload(
                guardrail_id=event["guardrail_id"], timestamp=int(event["time"])
            ),
        )
    elif event["event_type"] == "guardrail_activated":
        return GuardrailActivated(
            aggregate_id=event["aggregate_id"],
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            payload=GuardrailActivatedPayload(
                guardrail_id=event["guardrail_id"], timestamp=int(event["time"])
            ),
        )


def handle_guardrail_activated(
    event: Dict, aggregate_events: List[Event]
) -> Tuple[GuardrailActivated, List[GuardrailActivationCount]]:
    event = _convert_payload_to_event(event, len(aggregate_events))
    guardrail_activation_count = 1
    for aggregate_event in aggregate_events:
        if isinstance(aggregate_event, GuardrailActivated):
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
    event: Dict, aggregate_events: List[Event]
) -> Tuple[GuardrailPassed, List[Union[GuardrailLeadTime, GuardrailMaxActivation]]]:
    event = _convert_payload_to_event(event, len(aggregate_events))
    last_compliant_event = 0
    for i, aggregate_event in enumerate(aggregate_events):
        if isinstance(aggregate_event, GuardrailPassed):
            last_compliant_event = i
    for aggregate_event in aggregate_events[last_compliant_event:]:
        if isinstance(aggregate_event, GuardrailActivated):
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
                        metric_value=len(aggregate_events[last_compliant_event + 1 :])
                        if last_compliant_event > 0
                        else len(aggregate_events[last_compliant_event:]),
                    ),
                ],
            )
    return (event, [])
