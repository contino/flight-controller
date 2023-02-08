from datetime import datetime
from uuid import uuid4
import pytest

from src.usecases.accounts import handle_account_created, handle_account_assigned
from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountAssigned,
    AccountRequestedPayload,
    AccountRequested,
    AccountAssignedPayload,
    AccountLeadTime,
    AccountAssignedLeadTime,
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

accountAssigned = AccountAssigned(
    aggregateId="test-account",
    aggregateType="Account",
    aggregateVersion=1,
    eventId=uuid4(),
    eventVersion=1,
    payload=AccountAssignedPayload(
        "test-account", int(round(datetime(2022, 8, 2, 11, 0, 0).timestamp()))
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

@pytest.fixture
def account_assigned():
    return handle_account_assigned(accountRequested, accountAssigned)


def test_create_account_returns_correct_type(account_created):
    assert isinstance(
        account_created, AccountLeadTime
    )


def test_create_account_calculates_lead_time_correctly(account_created):
    assert account_created.lead_time == 7200

def test_assign_account_returns_correct_type(account_assigned):
    assert isinstance(
        account_assigned, AccountAssignedLeadTime
    )


def test_assign_account_calculates_lead_time_correctly(account_assigned):
    assert account_assigned.lead_time == 3600
