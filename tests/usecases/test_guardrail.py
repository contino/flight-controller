from time import time
from uuid import uuid4


from src.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivatedPayload,
    GuardrailPassed,
    GuardrailPassedPayload,
    GuardrailActivationCount,
    GuardrailMaxActivation,
    GuardrailLeadTime

)
from src.usecases.guardrail import (
    handle_guardrail_activated,
    handle_guardrail_passed
)

event = GuardrailActivated(
    uuid4(),
    "Resource",
    1,
    uuid4(),
    1,
    GuardrailActivatedPayload(guardrail_id=uuid4(), timestamp=int(time())),
)

compliant_event = GuardrailPassed(
    event.aggregateId,
    "Resource",
    2,
    uuid4(),
    1,
    GuardrailPassedPayload(
        guardrail_id=uuid4(), timestamp=(event.payload.timestamp + 10)
    ),
)


def test_guardrail_activatied_returns_activation_count():
    assert isinstance(handle_guardrail_activated(event, []), GuardrailActivationCount) 


def test_guardrail_activatied_returns_correct_activation_count():
    assert handle_guardrail_activated(event, []).count == 1


def test_guardrail_passed_with_no_history_returns_none():
    assert handle_guardrail_passed(event, []) is None


def test_guardrail_passed_with_history_returns_lead_time():
    assert isinstance(
        handle_guardrail_passed(compliant_event, [event])[0],
        GuardrailLeadTime,
    )


def test_guardrail_passed_with_history_returns_correct_lead_time():
    assert handle_guardrail_passed(compliant_event, [event])[0].lead_time == 10


def test_guardrail_passed_with_multiple_history_events_returns_correct_lead_time():
    second_event = GuardrailActivated(
        event.aggregateId,
        "Resource",
        2,
        uuid4(),
        1,
        GuardrailActivatedPayload(
            guardrail_id=uuid4(), timestamp=(event.payload.timestamp + 5)
        ),
    )
    assert (
        handle_guardrail_passed(compliant_event, [event, second_event])[0].lead_time == 10
    )


def test_guardrail_passed_returns_correct_lead_time_from_oldest_pertinent_non_compliant():
    second_event = GuardrailPassed(
        event.aggregateId,
        "Resource",
        2,
        uuid4(),
        1,
        GuardrailActivatedPayload(
            guardrail_id=uuid4(), timestamp=(event.payload.timestamp + 4)
        ),
    )
    third_event = GuardrailActivated(
        event.aggregateId,
        "Resource",
        2,
        uuid4(),
        1,
        GuardrailActivatedPayload(
            guardrail_id=uuid4(), timestamp=(event.payload.timestamp + 5)
        ),
    )
    assert (
        handle_guardrail_passed(
            compliant_event, [event, second_event, third_event]
        )[0].lead_time
        == 5
    )

def test_guardrail_passed_with_history_returns_max_activations():
    assert isinstance(
        handle_guardrail_passed(compliant_event, [event])[1],
        GuardrailMaxActivation,
    )

def test_guardrail_passed_with_history_returns_correct_max_activation():
    assert handle_guardrail_passed(compliant_event, [event])[1].count == 1

def test_guardrail_passed_with_multiple_history_events_returns_max_activation():
    second_event = GuardrailActivated(
        event.aggregateId,
        "Resource",
        2,
        uuid4(),
        1,
        GuardrailActivatedPayload(
            guardrail_id=uuid4(), timestamp=(event.payload.timestamp + 5)
        ),
    )
    assert (
        handle_guardrail_passed(compliant_event, [event, second_event])[1].count == 2
    )

def test_guardrail_passed_returns_correct_max_activation_from_last_pertinent_non_compliant():
    second_event = GuardrailPassed(
        event.aggregateId,
        "Resource",
        2,
        uuid4(),
        1,
        GuardrailActivatedPayload(
            guardrail_id=uuid4(), timestamp=(event.payload.timestamp + 4)
        ),
    )
    third_event = GuardrailActivated(
        event.aggregateId,
        "Resource",
        2,
        uuid4(),
        1,
        GuardrailActivatedPayload(
            guardrail_id=uuid4(), timestamp=(event.payload.timestamp + 6)
        ),
    )
    fourth_event = GuardrailActivated(
        event.aggregateId,
        "Resource",
        2,
        uuid4(),
        1,
        GuardrailActivatedPayload(
            guardrail_id=uuid4(), timestamp=(event.payload.timestamp + 8)
        ),
    )
    assert (
        handle_guardrail_passed(
            compliant_event, [event, second_event, third_event, fourth_event]
        )[1].count
        == 2
    )