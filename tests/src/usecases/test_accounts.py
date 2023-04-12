from time import time
from uuid import uuid4

from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountLeadTime,
    AccountRequested,
    AccountRequestedPayload,
)
from src.usecases.accounts import handle_account_created, handle_account_requested

requested_aggregate_event = AccountRequested(
    aggregate_id=str(uuid4()),
    event_id=str(uuid4()),
    aggregate_version=1,
    payload=AccountRequestedPayload(timestamp=int(time())),
)

requested_event = AccountRequested(
    aggregate_id=requested_aggregate_event.aggregate_id,
    event_id=str(uuid4()),
    aggregate_version=1,
    payload=AccountRequestedPayload(timestamp=int(time())),
)


def test_handle_account_requested_returns_correct_event_type():
    assert isinstance(
        handle_account_requested(requested_event, [])[0], AccountRequested
    )


def test_handle_account_requested_returns_no_metrics():
    assert len(handle_account_requested(requested_event, [])[1]) == 0


def test_handle_account_created_returns_correct_event_type():
    created_event = AccountCreated(
        aggregate_id=requested_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        aggregate_version=2,
        payload=AccountCreatedPayload(timestamp=int(requested_aggregate_event.payload.timestamp + 10))
    )
    assert isinstance(
        handle_account_created(created_event, [requested_aggregate_event])[0],
        AccountCreated,
    )


def test_handle_account_created_returns_correct_metric_type():
    created_event = AccountCreated(
        aggregate_id=requested_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        aggregate_version=2,
        payload=AccountCreatedPayload(timestamp=int(requested_aggregate_event.payload.timestamp + 10))
    )
    assert isinstance(
        handle_account_created(created_event, [requested_aggregate_event])[1][0],
        AccountLeadTime,
    )


def test_handle_account_created_calculates_lead_time_correctly():
    created_event = AccountCreated(
        aggregate_id=requested_aggregate_event.aggregate_id,
        event_id=str(uuid4()),
        aggregate_version=2,
        payload=AccountCreatedPayload(timestamp=int(requested_aggregate_event.payload.timestamp + 10))
    )
    assert (
        handle_account_created(created_event, [requested_aggregate_event])[1][
            0
        ].metric_value
        == 10
    )
