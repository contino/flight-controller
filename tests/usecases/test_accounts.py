from datetime import datetime
from uuid import uuid4
import pytest

from src.usecases.accounts import handle_account_created
from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountLeadTime,
    AccountRequested,
    AccountRequestedPayload,
)

accountRequested = AccountRequested(
    aggregateId="test-account",
    aggregateType="Account",
    aggregateVersion=1,
    eventId=uuid4(),
    eventVersion=1,
    payload=AccountRequestedPayload(
        "test-account", int(round(datetime(2022, 8, 2, 10, 0, 0).timestamp()))
    ),
)

accountCreated = AccountCreated(
    aggregateId="test-account",
    aggregateType="Account",
    aggregateVersion=2,
    eventId=uuid4(),
    eventVersion=1,
    payload=AccountCreatedPayload(
        "test-account", int(round(datetime(2022, 8, 2, 12, 0, 0).timestamp()))
    ),
)


@pytest.fixture
def account_created():
    return handle_account_created(accountRequested, accountCreated)


def test_create_account_returns_correct_type(account_created):
    assert isinstance(account_created, AccountLeadTime)


def test_create_account_calculates_lead_time_correctly(account_created):
    assert account_created.lead_time == 7200
