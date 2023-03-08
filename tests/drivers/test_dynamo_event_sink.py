from datetime import datetime
import os
import random
import string
from uuid import uuid4

import pytest

from src.drivers.dynamo_event_sink_source import DynamoEventSink, DynamoEventSource
from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountRequested,
    AccountRequestedPayload,
)
from src.entities.compliance import (
    ResourceFoundCompliant,
    ResourceFoundCompliantPayload,
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)
from src.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivatedPayload,
    GuardrailPassed,
    GuardrailPassedPayload,
)
from src.entities.identity import (
    IdentityCreated,
    IdentityCreatedPayload,
    IdentityRequested,
    IdentityRequestedPayload,
)
from src.entities.patch import (
    PatchRunSummary,
    PatchRunSummaryPayload,
)
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
)


@pytest.fixture(autouse=True)
def set_table_name():
    os.environ["DYNAMO_TABLE_NAME"] = "event_sourcing_table"


@pytest.mark.integration
def test_returns_error_on_non_existent_table():
    os.environ["DYNAMO_TABLE_NAME"] = "does_not_exist"
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    event = ProjectRequested(
        aggregate_id=aggregate_id,
        aggregate_version=1,
        event_id=uuid4(),
        payload=ProjectRequestedPayload(
            timestamp=int(round(datetime.utcnow().timestamp()))
        ),
    )
    sink = DynamoEventSink()

    assert isinstance(sink.store_events([event]), Exception)


@pytest.mark.integration
def test_retrieves_project_events_from_dynamodb():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    event = ProjectRequested(
        aggregate_id=aggregate_id,
        aggregate_version=1,
        event_id=uuid4(),
        payload=ProjectRequestedPayload(
            timestamp=int(round(datetime.utcnow().timestamp()))
        ),
    )
    event_2 = ProjectCreated(
        aggregate_id=aggregate_id,
        aggregate_version=2,
        event_id=uuid4(),
        payload=ProjectCreatedPayload(
            timestamp=int(round(datetime.utcnow().timestamp()))
        ),
    )
    sink = DynamoEventSink()
    sink.store_events([event, event_2])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(event.aggregate_id)

    assert got == [event, event_2]


@pytest.mark.integration
def test_retrieves_compliance_events_from_dynamodb():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    container_id = "".join(random.choices(string.ascii_letters, k=12))
    event = ResourceFoundCompliant(
        aggregate_id=aggregate_id,
        aggregate_version=1,
        event_id=uuid4(),
        payload=ResourceFoundCompliantPayload(
            container_id=container_id,
            timestamp=int(round(datetime.utcnow().timestamp())),
        ),
    )
    event_2 = ResourceFoundNonCompliant(
        aggregate_id=aggregate_id,
        aggregate_version=2,
        event_id=uuid4(),
        payload=ResourceFoundNonCompliantPayload(
            container_id=container_id,
            timestamp=int(round(datetime.utcnow().timestamp())),
        ),
    )
    sink = DynamoEventSink()
    sink.store_events([event, event_2])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(aggregate_id)

    assert got == [event, event_2]


@pytest.mark.integration
def test_retrieves_patch_events_from_dynamodb():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    event = PatchRunSummary(
        aggregate_id=aggregate_id,
        aggregate_version=1,
        event_id=uuid4(),
        payload=PatchRunSummaryPayload(
            successful_instances="i-adslkjfds,i-89dsfkjdkfj",
            failed_instances="i-peoritdsfl",
        ),
    )
    sink = DynamoEventSink()
    sink.store_events([event])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(aggregate_id)

    assert got == [event]


@pytest.mark.integration
def test_retrieves_account_events_from_dynamodb():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    event = AccountRequested(
        aggregate_id=aggregate_id,
        aggregate_version=1,
        event_id=uuid4(),
        payload=AccountRequestedPayload(
            timestamp=int(round(datetime.utcnow().timestamp()))
        ),
    )
    event_2 = AccountCreated(
        aggregate_id=aggregate_id,
        aggregate_version=2,
        event_id=uuid4(),
        payload=AccountCreatedPayload(
            timestamp=int(round(datetime.utcnow().timestamp()))
        ),
    )
    sink = DynamoEventSink()
    sink.store_events([event, event_2])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(aggregate_id)

    assert got == [event, event_2]


@pytest.mark.integration
def test_retrieves_guardrail_events_from_dynamodb():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    event = GuardrailPassed(
        aggregate_id=aggregate_id,
        aggregate_version=1,
        event_id=uuid4(),
        payload=GuardrailPassedPayload(
            guardrail_id=guardrail_id,
            timestamp=int(round(datetime.utcnow().timestamp())),
        ),
    )
    event_2 = GuardrailActivated(
        aggregate_id=aggregate_id,
        aggregate_version=2,
        event_id=uuid4(),
        payload=GuardrailActivatedPayload(
            guardrail_id=guardrail_id,
            timestamp=int(round(datetime.utcnow().timestamp())),
        ),
    )
    sink = DynamoEventSink()
    sink.store_events([event, event_2])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(aggregate_id)

    assert got == [event, event_2]


@pytest.mark.integration
def test_retrieves_identity_events_from_dynamodb():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    event = IdentityRequested(
        aggregate_id=aggregate_id,
        aggregate_version=1,
        event_id=uuid4(),
        payload=IdentityRequestedPayload(
            account_id=aggregate_id,
            timestamp=int(round(datetime.utcnow().timestamp())),
        ),
    )
    event_2 = IdentityCreated(
        aggregate_id=aggregate_id,
        aggregate_version=2,
        event_id=uuid4(),
        payload=IdentityCreatedPayload(
            account_id=aggregate_id,
            timestamp=int(round(datetime.utcnow().timestamp())),
        ),
    )
    sink = DynamoEventSink()
    sink.store_events([event, event_2])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(aggregate_id)

    assert got == [event, event_2]
