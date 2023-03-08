from datetime import datetime
from uuid import uuid4
import pytest

from src.usecases.identity import handle_identity_created, handle_identity_requested
from src.entities.identity import (
    IdentityCreatedPayload,
    IdentityCreated,
    IdentityLeadTime,
    IdentityRequested,
    IdentityRequestedPayload,
)

identity_requested = IdentityRequested(
    aggregate_id="test-identity",
    aggregate_version=1,
    event_id=uuid4(),
    event_version=1,
    payload=IdentityRequestedPayload(
        account_id="test-account",
        timestamp=int(round(datetime(2022, 8, 2, 10, 0, 0).timestamp())),
    ),
)

identity_created = IdentityCreated(
    aggregate_id="test-identity",
    aggregate_version=2,
    event_id=uuid4(),
    event_version=1,
    payload=IdentityCreatedPayload(
        account_id="test-account",
        timestamp=int(round(datetime(2022, 8, 2, 12, 0, 0).timestamp())),
    ),
)


requested_event = {
    "event_type": "identity_requested",
    "aggregate_id": identity_created.aggregate_id,
    "time": int(identity_requested.payload.timestamp),
    "account_id": "test-account",
}

created_event = {
    "event_type": "identity_created",
    "aggregate_id": identity_requested.aggregate_id,
    "time": int(identity_created.payload.timestamp),
    "account_id": "test-account",
}


@pytest.fixture
def lead_time():
    return handle_identity_created(created_event, [identity_requested])


def test_request_identity_returns_correct_type():
    assert isinstance(
        handle_identity_requested(requested_event, [])[0], IdentityRequested
    )


def test_create_identity_returns_correct_type(lead_time):
    assert isinstance(lead_time[1][0], IdentityLeadTime)


def test_create_identity_calculates_lead_time_correctly(lead_time):
    assert lead_time[1][0].metric_value == 7200
