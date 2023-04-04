from time import time
from uuid import uuid4

from src.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivationCount,
    GuardrailActivatedPayload,
    GuardrailLeadTime,
    GuardrailMaxActivation,
    GuardrailPassed,
    GuardrailPassedPayload,
)
from src.usecases.guardrail import handle_guardrail_activated, handle_guardrail_passed

activated_aggregate_event = GuardrailActivated(
    aggregate_id=str(uuid4()),
    event_id=str(uuid4()),
    aggregate_version=1,
    payload=GuardrailActivatedPayload(guardrail_id=str(uuid4()), timestamp=int(time())),
)

activated_event = GuardrailActivated(
    aggregate_id=activated_aggregate_event.aggregate_id,
    event_id=str(uuid4()),
    aggregate_version=1,
    payload=GuardrailActivatedPayload(guardrail_id=activated_aggregate_event.payload.guardrail_id, timestamp=activated_aggregate_event.payload.timestamp + 5),
)

passed_event = GuardrailPassed(
    aggregate_id=activated_aggregate_event.aggregate_id,
    event_id=str(uuid4()),
    aggregate_version=1,
    payload=GuardrailPassedPayload(guardrail_id=activated_aggregate_event.payload.guardrail_id, timestamp=activated_aggregate_event.payload.timestamp + 10),
)


def test_guardrail_activated_returns_correct_event_type():
    assert isinstance(
        handle_guardrail_activated(activated_event, [])[0], GuardrailActivated
    )


def test_guardrail_activated_returns_activation_count():
    assert isinstance(
        handle_guardrail_activated(activated_event, [])[1][0], GuardrailActivationCount
    )


def test_guardrail_activated_returns_correct_activation_count():
    activated_event.aggregate_version = 2
    assert (
        handle_guardrail_activated(activated_event, [activated_aggregate_event])[1][
            0
        ].metric_value
        == 2
    )


def test_guardrail_activated_with_different_guardrail_ids_returns_correct_activation_count():
    second_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=2,
        payload=GuardrailActivatedPayload(
            guardrail_id=str(uuid4()),
            timestamp=int(activated_aggregate_event.payload.timestamp + 5),
        ),
    )
    activated_event.aggregate_version = 3
    assert (
        handle_guardrail_activated(activated_event, [activated_aggregate_event, second_activated_aggregate_event])[1][
            0
        ].metric_value
        == 2
    )


def test_guardrail_passed_with_no_history_returns_correct_event_type():
    assert isinstance(handle_guardrail_passed(passed_event, [])[0], GuardrailPassed)


def test_guardrail_passed_with_no_history_returns_no_metrics():
    assert len(handle_guardrail_passed(passed_event, [])[1]) == 0


def test_guardrail_passed_with_history_of_passes_returns_no_metrics():
    passed_aggregate_event = GuardrailPassed(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_passed",
        aggregate_version=1,
        payload=GuardrailPassedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 5),
        ),
    )
    passed_event.aggregate_version = 2
    assert len(handle_guardrail_passed(passed_event, [passed_aggregate_event])[1]) == 0


def test_guardrail_passed_with_history_of_other_guardrail_ids_returns_no_metrics():
    passed_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=1,
        payload=GuardrailActivatedPayload(
            guardrail_id=str(uuid4()),
            timestamp=int(activated_aggregate_event.payload.timestamp + 5),
        ),
    )
    passed_event.aggregate_version = 2
    assert len(handle_guardrail_passed(passed_event, [passed_aggregate_event])[1]) == 0


def test_guardrail_passed_with_history_returns_lead_time():
    passed_event.aggregate_version = 2
    assert isinstance(
        handle_guardrail_passed(passed_event, [activated_aggregate_event])[1][0],
        GuardrailLeadTime,
    )


def test_guardrail_passed_with_history_returns_correct_lead_time():
    passed_event.aggregate_version = 2
    assert (
        handle_guardrail_passed(passed_event, [activated_aggregate_event])[1][
            0
        ].metric_value
        == 10
    )


def test_guardrail_passed_with_different_guardrail_ids_with_history_returns_correct_lead_time():
    second_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=2,
        payload=GuardrailActivatedPayload(
            guardrail_id=str(uuid4()),
            timestamp=int(activated_aggregate_event.payload.timestamp + 5),
        ),
    )
    third_passed_aggregate_event = GuardrailPassed(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_passed",
        aggregate_version=3,
        payload=GuardrailPassedPayload(
            guardrail_id=second_activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 7),
        ),
    )
    passed_event.aggregate_version = 4
    assert (
        handle_guardrail_passed(passed_event, [activated_aggregate_event, second_activated_aggregate_event, third_passed_aggregate_event])[1][
            0
        ].metric_value
        == 10
    )


def test_guardrail_passed_with_multiple_history_events_returns_correct_lead_time():
    second_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=2,
        payload=GuardrailActivatedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 5),
        ),
    )
    passed_event.aggregate_version = 3
    assert (
        handle_guardrail_passed(
            passed_event, [activated_aggregate_event, second_activated_aggregate_event]
        )[1][0].metric_value
        == 10
    )


def test_guardrail_passed_returns_correct_lead_time_from_oldest_pertinent_activated():
    second_passed_aggregate_event = GuardrailPassed(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_passed",
        aggregate_version=2,
        payload=GuardrailPassedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 4),
        ),
    )
    third_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=3,
        payload=GuardrailActivatedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 5),
        ),
    )
    passed_event.aggregate_version = 4
    assert (
        handle_guardrail_passed(
            passed_event,
            [
                activated_aggregate_event,
                second_passed_aggregate_event,
                third_activated_aggregate_event,
            ],
        )[1][0].metric_value
        == 5
    )


def test_guardrail_passed_with_history_returns_max_activations():
    passed_event.aggregate_version = 2
    assert isinstance(
        handle_guardrail_passed(passed_event, [activated_aggregate_event])[1][1],
        GuardrailMaxActivation,
    )


def test_guardrail_passed_with_history_returns_correct_max_activation():
    passed_event.aggregate_version = 2
    assert (
        handle_guardrail_passed(passed_event, [activated_aggregate_event])[1][
            1
        ].metric_value
        == 1
    )


def test_guardrail_passed_with_different_guardrail_ids_with_history_returns_correct_max_activation():
    second_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=2,
        payload=GuardrailActivatedPayload(
            guardrail_id=str(uuid4()),
            timestamp=int(activated_aggregate_event.payload.timestamp + 5),
        ),
    )
    third_passed_aggregate_event = GuardrailPassed(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_passed",
        aggregate_version=2,
        payload=GuardrailPassedPayload(
            guardrail_id=second_activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 7),
        ),
    )
    passed_event.aggregate_version = 4
    assert (
        handle_guardrail_passed(passed_event, [activated_aggregate_event, second_activated_aggregate_event, third_passed_aggregate_event])[1][
            1
        ].metric_value
        == 1
    )


def test_guardrail_passed_with_multiple_history_events_returns_max_activation():
    second_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=2,
        payload=GuardrailActivatedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 5),
        ),
    )
    passed_event.aggregate_version = 3
    assert (
        handle_guardrail_passed(
            passed_event, [activated_aggregate_event, second_activated_aggregate_event]
        )[1][1].metric_value
        == 2
    )


def test_guardrail_passed_returns_correct_max_activation_from_last_pertinent_activated():
    second_passed_aggregate_event = GuardrailPassed(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_passed",
        aggregate_version=2,
        payload=GuardrailPassedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 4),
        ),
    )
    third_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=3,
        payload=GuardrailActivatedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 5),
        ),
    )
    fourth_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=4,
        payload=GuardrailActivatedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 6),
        ),
    )
    passed_event.aggregate_version = 5
    assert (
        handle_guardrail_passed(
            passed_event,
            [
                activated_aggregate_event,
                second_passed_aggregate_event,
                third_activated_aggregate_event,
                fourth_activated_aggregate_event,
            ],
        )[1][1].metric_value
        == 2
    )


def test_guardrail_passed_returns_correct_max_activation_from_last_pertinent_activated_with_first_aggregate_being_passed():
    passed_aggregate_event = GuardrailPassed(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_passed",
        aggregate_version=1,
        payload=GuardrailPassedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 4),
        ),
    )
    second_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=2,
        payload=GuardrailActivatedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 5),
        ),
    )
    third_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=3,
        payload=GuardrailActivatedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 6),
        ),
    )
    passed_event.aggregate_version = 4
    assert (
        handle_guardrail_passed(
            passed_event,
            [
                passed_aggregate_event,
                second_activated_aggregate_event,
                third_activated_aggregate_event,
            ],
        )[1][1].metric_value
        == 2
    )


def test_guardrail_passed_with_history_returns_correct_max_activation_from_last_pertinent_activated_with_a_max_less_then_previous():
    second_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=2,
        payload=GuardrailActivatedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 2),
        ),
    )
    third_passed_aggregate_event = GuardrailPassed(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_passed",
        aggregate_version=3,
        payload=GuardrailPassedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 4),
        ),
    )
    fourth_activated_aggregate_event = GuardrailActivated(
        aggregate_id=activated_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        event_type="guardrail_activated",
        aggregate_version=4,
        payload=GuardrailActivatedPayload(
            guardrail_id=activated_aggregate_event.payload.guardrail_id,
            timestamp=int(activated_aggregate_event.payload.timestamp + 6),
        ),
    )
    passed_event.aggregate_version = 5
    assert (
        handle_guardrail_passed(
            passed_event,
            [
                activated_aggregate_event,
                second_activated_aggregate_event,
                third_passed_aggregate_event,
                fourth_activated_aggregate_event,

            ],
        )[1][1].metric_value
        == 1
    )
