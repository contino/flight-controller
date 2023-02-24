from datetime import datetime
import random
import string
from uuid import UUID, uuid4

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
    GuardrailPassedPayload
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


@pytest.mark.integration
def test_retrieves_project_events_from_dynamodb():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    event = ProjectRequested(
        aggregate_id=aggregate_id,
        aggregate_type="Project",
        aggregate_version=1,
        event_id=uuid4(),
        event_version=1,
        payload=ProjectRequestedPayload(
            aggregate_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    event_2 = ProjectCreated(
        aggregate_id=aggregate_id,
        aggregate_type="Project",
        aggregate_version=2,
        event_id=uuid4(),
        event_version=1,
        payload=ProjectCreatedPayload(
            aggregate_id, int(round(datetime.utcnow().timestamp()))
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
        aggregate_type="Resource",
        aggregate_version=1,
        event_id=uuid4(),
        event_version=1,
        payload=ResourceFoundCompliantPayload(
            container_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    event_2 = ResourceFoundNonCompliant(
        aggregate_id=aggregate_id,
        aggregate_type="Resource",
        aggregate_version=2,
        event_id=uuid4(),
        event_version=1,
        payload=ResourceFoundNonCompliantPayload(
            container_id, int(round(datetime.utcnow().timestamp()))
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
        aggregate_type="Account",
        aggregate_version=1,
        event_id=uuid4(),
        event_version=1,
        payload=PatchRunSummaryPayload(
            "i-adslkjfds,i-89dsfkjdkfj", "i-peoritdsfl"
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
        aggregate_type="Account",
        aggregate_version=1,
        event_id=uuid4(),
        event_version=1,
        payload=AccountRequestedPayload(
            aggregate_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    event_2 = AccountCreated(
        aggregate_id=aggregate_id,
        aggregate_type="Account",
        aggregate_version=2,
        event_id=uuid4(),
        event_version=1,
        payload=AccountCreatedPayload(
            aggregate_id, int(round(datetime.utcnow().timestamp()))
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
        aggregate_type="Resource",
        aggregate_version=1,
        event_id=uuid4(),
        event_version=1,
        payload=GuardrailPassedPayload(
            guardrail_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    event_2 = GuardrailActivated(
        aggregate_id=aggregate_id,
        aggregate_type="Resource",
        aggregate_version=2,
        event_id=uuid4(),
        event_version=1,
        payload=GuardrailActivatedPayload(
            guardrail_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    sink = DynamoEventSink()
    sink.store_events([event, event_2])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(aggregate_id)
    
    assert got == [event, event_2]


