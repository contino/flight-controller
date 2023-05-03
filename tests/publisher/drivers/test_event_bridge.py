from time import time
from uuid import uuid4

import pytest

from publisher.drivers.event_bridge import EventBridge
from publisher.entities.events import (
    GuardrailActivated,
    GuardrailPassed,
)


AGGREGATE_ID = str(uuid4())
ALTERNATE_ID = str(uuid4())
CURRENT_TIME = int(time())

EVENTS = [
    GuardrailActivated(
        aggregate_id = AGGREGATE_ID,
        guardrail_id = ALTERNATE_ID,
        timestamp = CURRENT_TIME,
    ),
    GuardrailPassed(
        aggregate_id = AGGREGATE_ID,
        guardrail_id = ALTERNATE_ID,
        timestamp = CURRENT_TIME,
    ),
]

DOZEN_EVENTS = [
    GuardrailActivated(
        aggregate_id = AGGREGATE_ID,
        guardrail_id = ALTERNATE_ID,
        timestamp = CURRENT_TIME,
    ) for i in range(12)
]


@pytest.mark.aws
@pytest.mark.integration
def test_event_bridge_returns_response():
    event_sink = EventBridge()
    assert isinstance(event_sink.send_events(EVENTS), str)


@pytest.mark.aws
@pytest.mark.integration
def test_event_bridge_returns_no_exception():
    event_sink = EventBridge()
    assert not isinstance(event_sink.send_events(EVENTS), Exception)


@pytest.mark.aws
@pytest.mark.integration
def test_event_bridge_handles_more_then_10_events():
    event_sink = EventBridge()
    assert not isinstance(event_sink.send_events(DOZEN_EVENTS), Exception)


@pytest.mark.aws
@pytest.mark.integration
def test_event_bridge_returns_exception_on_no_events():
    event_sink = EventBridge()
    assert isinstance(event_sink.send_events([]), Exception)
