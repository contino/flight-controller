import random
import string
from datetime import datetime
from uuid import UUID, uuid4

import pytest

from src.drivers.dynamo_event_sink_source import DynamoEventSink, DynamoEventSource

from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
)

from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountRequested,
    AccountRequestedPayload,
)


@pytest.mark.integration
def test_retrieves_project_events_from_dynamodb():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    projectRequested = ProjectRequested(
        aggregateId=aggregate_id,
        aggregateType="Project",
        aggregateVersion=1,
        eventId=uuid4(),
        eventVersion=1,
        payload=ProjectRequestedPayload(
            aggregate_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    projectCreated = ProjectCreated(
        aggregateId=aggregate_id,
        aggregateType="Project",
        aggregateVersion=2,
        eventId=uuid4(),
        eventVersion=1,
        payload=ProjectCreatedPayload(
            aggregate_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    sink = DynamoEventSink()
    sink.store_events([projectRequested, projectCreated])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(projectRequested.aggregateId)

    assert got == [projectRequested, projectCreated]


@pytest.mark.integration
def test_retrieves_account_events_from_dynamodb():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    accountRequested = AccountRequested(
        aggregateId=aggregate_id,
        aggregateType="Account",
        aggregateVersion=1,
        eventId=uuid4(),
        eventVersion=1,
        payload=AccountRequestedPayload(
            aggregate_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    accountCreated = AccountCreated(
        aggregateId=aggregate_id,
        aggregateType="Account",
        aggregateVersion=2,
        eventId=uuid4(),
        eventVersion=1,
        payload=AccountCreatedPayload(
            aggregate_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    sink = DynamoEventSink()
    sink.store_events([accountRequested, accountCreated])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(accountRequested.aggregateId)

    assert got == [accountRequested, accountCreated]
import random
import string
from datetime import datetime
from uuid import UUID, uuid4

import pytest

from src.drivers.dynamo_event_sink_source import DynamoEventSink, DynamoEventSource
from src.entities.compliance import (
    ResourceFoundCompliant,
    ResourceFoundCompliantPayload,
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
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
    projectRequested = ProjectRequested(
        aggregateId=aggregate_id,
        aggregateType="Project",
        aggregateVersion=1,
        eventId=uuid4(),
        eventVersion=1,
        payload=ProjectRequestedPayload(
            aggregate_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    projectCreated = ProjectCreated(
        aggregateId=aggregate_id,
        aggregateType="Project",
        aggregateVersion=2,
        eventId=uuid4(),
        eventVersion=1,
        payload=ProjectCreatedPayload(
            aggregate_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    sink = DynamoEventSink()
    sink.store_events([projectRequested, projectCreated])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(projectRequested.aggregateId)

    assert got == [projectRequested, projectCreated]


@pytest.mark.integration
def test_retrieves_compliance_events_from_dynamodb():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    container_id = "".join(random.choices(string.ascii_letters, k=12))
    event = ResourceFoundCompliant(
        aggregateId=aggregate_id,
        aggregateType="Resource",
        aggregateVersion=1,
        eventId=uuid4(),
        eventVersion=1,
        payload=ResourceFoundCompliantPayload(
            container_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    event_2 = ResourceFoundNonCompliant(
        aggregateId=aggregate_id,
        aggregateType="Resource",
        aggregateVersion=2,
        eventId=uuid4(),
        eventVersion=1,
        payload=ResourceFoundNonCompliantPayload(
            container_id, int(round(datetime.utcnow().timestamp()))
        ),
    )
    sink = DynamoEventSink()
    sink.store_events([event, event_2])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(aggregate_id)

    assert got == [event, event_2]
