from time import time
from uuid import uuid4

import pytest

from publisher.drivers.event_bridge import EventBridge
from publisher.entities.events import (
    GuardrailActivated,
    GuardrailPassed,
)

EVENT_SINK = EventBridge()
AGGREGATE_ID = str(uuid4())
ALTERNATE_ID = str(uuid4())
CURRENT_TIME = int(time())

EVENTS = [
    GuardrailActivated(
        aggregate_id = AGGREGATE_ID,
        guardrail_id = ALTERNATE_ID,
        time = CURRENT_TIME,
    ),
    GuardrailPassed(
        aggregate_id = AGGREGATE_ID,
        guardrail_id = ALTERNATE_ID,
        time = CURRENT_TIME,
    ),
]

DOZEN_EVENTS = [
    GuardrailActivated(
        aggregate_id = AGGREGATE_ID,
        guardrail_id = ALTERNATE_ID,
        time = CURRENT_TIME,
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
def test_event_bridge_returns_exception_on_no_events():
    assert isinstance(EVENT_SINK.send_events([]), Exception)
