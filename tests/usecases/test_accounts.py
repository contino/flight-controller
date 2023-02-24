from datetime import datetime
from uuid import uuid4

import pytest

from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountLeadTime,
    AccountRequested,
    AccountRequestedPayload,
)
from src.usecases.accounts import handle_account_created


event = AccountRequested(
    aggregate_id="test-account",
    aggregate_type="Account",
    aggregate_version=1,
    event_id=uuid4(),
    event_version=1,
    payload=AccountRequestedPayload(
        "test-account", int(round(datetime(2022, 8, 2, 10, 0, 0).timestamp()))
    ),
)

created_event = AccountCreated(
    aggregate_id="test-account",
    aggregate_type="Account",
    aggregate_version=2,
    event_id=uuid4(),
    event_version=1,
    payload=AccountCreatedPayload(
        "test-account", int(round(datetime(2022, 8, 2, 12, 0, 0).timestamp()))
    ),
)


@pytest.fixture
def AccountCreated():
    return handle_account_created(event, created_event)


def test_create_account_returns_correct_type(AccountCreated):
    assert isinstance(AccountCreated, AccountLeadTime)


def test_create_account_calculates_lead_time_correctly(AccountCreated):
    assert AccountCreated.lead_time == 7200
