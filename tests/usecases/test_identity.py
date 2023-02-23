from datetime import datetime
from uuid import uuid4
import pytest

from src.usecases.identity import handle_identity_created
from src.entities.identity import (
    IdentityCreatedPayload,
    IdentityCreated,
    IdentityLeadTime,
    IdentityRequested,
    IdentityRequestedPayload,
)

identityRequested = IdentityRequested(
    aggregate_id="test-identity",
    aggregate_type="Account",
    aggregate_version=1,
    event_id=uuid4(),
    event_version=1,
    payload=IdentityRequestedPayload(
        "test-identity", int(round(datetime(2022, 8, 2, 10, 0, 0).timestamp()))
    ),
)

identityCreated = IdentityCreated(
    aggregate_id="test-identity",
    aggregate_type="Account",
    aggregate_version=2,
    event_id=uuid4(),
    event_version=1,
    payload=IdentityCreatedPayload(
        "test-identity", int(round(datetime(2022, 8, 2, 12, 0, 0).timestamp()))
    ),
)


@pytest.fixture
def lead_time():
    return handle_identity_created(identityRequested, identityCreated)


def test_create_identity_returns_correct_type(lead_time):
    assert isinstance(lead_time, IdentityLeadTime)


def test_create_identity_calculates_lead_time_correctly(lead_time):
    assert lead_time.lead_time == 7200
