from time import time
from uuid import uuid4

import pytest

from publisher.drivers.event_bridge import EventBridge
from publisher.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivatedDetail,
    GuardrailPassed,
    GuardrailPassedDetail,
)

EVENT_SINK = EventBridge()
AGGREGATE_ID = str(uuid4())
ALTERNATE_ID = str(uuid4())
CURRENT_TIME = int(time())

EVENTS = [
    GuardrailActivated(
        detail_type = "Test Custom Guardrail Activated Event",
        source = "contino.custom",
        detail = GuardrailActivatedDetail(
            aggregate_id = AGGREGATE_ID,
            guardrail_id = ALTERNATE_ID,
            time = CURRENT_TIME,
        )
    ),
    GuardrailPassed(
        detail_type = "Test Custom Guardrail Activated Event",
        source = "contino.custom",
        detail = GuardrailPassedDetail(
            aggregate_id = AGGREGATE_ID,
            guardrail_id = ALTERNATE_ID,
            time = CURRENT_TIME,
        )
    ),
]

DOZEN_EVENTS = [
    GuardrailActivated(
        detail_type = "Test Custom Guardrail Activated Event",
        source = "contino.custom",
        detail = GuardrailActivatedDetail(
            aggregate_id = AGGREGATE_ID,
            guardrail_id = ALTERNATE_ID,
            time = CURRENT_TIME,
        )
    ) for i in range(12)
]


@pytest.mark.integration
def test_event_bridge_returns_response():
    assert isinstance(EVENT_SINK.send_events(EVENTS), str)


@pytest.mark.integration
def test_event_bridge_returns_no_exception():
    assert not isinstance(EVENT_SINK.send_events(EVENTS), Exception)


@pytest.mark.integration
def test_event_bridge_handles_more_then_10_events():
    assert not isinstance(EVENT_SINK.send_events(DOZEN_EVENTS), Exception)


@pytest.mark.integration
def test_event_bridge_handles_no_event_returns_exception():
    assert isinstance(EVENT_SINK.send_events([]), Exception)