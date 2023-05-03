from datetime import datetime
import os
import random
import string
from uuid import uuid4

import pytest

from src.drivers.bigquery import BigQueryEventSink, BigQueryEventSource, BigQueryMetricSink

from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountRequested,
    AccountRequestedPayload,
    AccountLeadTime
)
from src.entities.compliance import (
    ResourceFoundCompliant,
    ResourceFoundCompliantPayload,
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
    ResourceComplianceExtraDimensions,
    ResourceComplianceLeadTime,
)
from src.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivatedPayload,
    GuardrailPassed,
    GuardrailPassedPayload,
    GuardrailActivationCount,
    GuardrailExtraDimensions,
    GuardrailLeadTime,
    GuardrailMaxActivation,
)
from src.entities.identity import (
    IdentityCreated,
    IdentityCreatedPayload,
    IdentityRequested,
    IdentityRequestedPayload,
    IdentityLeadTime
)
from src.entities.patch import (
    PatchRunSummary,
    PatchRunSummaryPayload,
    PatchCompliancePercentage
)
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
    ProjectLeadTime
)

@pytest.fixture(autouse=True)
def set_table_name():
    os.environ["BIGQUERY_EVENTS_TABLE"] = "contino-squad0-fc.event_sourcing_table.events_data"
    os.environ["BIGQUERY_METRICS_TABLE"] = "contino-squad0-fc.metric_sourcing_table.metrics_data"


@pytest.mark.gcp
@pytest.mark.integration
def test_returns_error_on_non_existent_table():
    os.environ["BIGQUERY_EVENTS_TABLE"] = "does_not_exist"
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    event = ProjectRequested(
        aggregate_id=aggregate_id,
        aggregate_version=1,
        event_id=uuid4(),
        payload=ProjectRequestedPayload(
            timestamp=int(round(datetime.utcnow().timestamp()))
        ),
    )
    sink = BigQueryEventSink()

    assert isinstance(sink.store_events([event]), Exception)


@pytest.mark.gcp
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
    sink = BigQueryEventSink()
    sink.store_events([event, event_2])

    source =  BigQueryEventSource()
    
    got =  source.get_events_for_aggregate(event.aggregate_id)

    assert got == [event, event_2]


@pytest.mark.gcp
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
    sink = BigQueryEventSink()
    sink.store_events([event, event_2])

    source = BigQueryEventSource()

    got = source.get_events_for_aggregate(aggregate_id)

    assert got == [event, event_2]


@pytest.mark.gcp
@pytest.mark.integration
def test_retrieves_patch_events_from_dynamodb():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    event = PatchRunSummary(
        aggregate_id=aggregate_id,
        aggregate_version=1,
        event_id=uuid4(),
        payload=PatchRunSummaryPayload(
            timestamp=int(round(datetime.utcnow().timestamp())),
            successful_instances="i-adslkjfds,i-89dsfkjdkfj",
            failed_instances="i-peoritdsfl",
        ),
    )
    sink = BigQueryEventSink()
    sink.store_events([event])

    source = BigQueryEventSource()

    got = source.get_events_for_aggregate(aggregate_id)

    assert got == [event]


@pytest.mark.gcp
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
    sink = BigQueryEventSink()
    sink.store_events([event, event_2])

    source = BigQueryEventSource()

    got = source.get_events_for_aggregate(aggregate_id)

    assert got == [event, event_2]


@pytest.mark.gcp
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
    sink = BigQueryEventSink()
    sink.store_events([event, event_2])

    source = BigQueryEventSource()

    got = source.get_events_for_aggregate(aggregate_id)

    assert got == [event, event_2]


@pytest.mark.gcp
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
    sink = BigQueryEventSink()
    sink.store_events([event, event_2])

    source = BigQueryEventSource()

    got = source.get_events_for_aggregate(aggregate_id)

    assert got == [event, event_2]


# Big Query Store metrics Tests
@pytest.mark.gcp
@pytest.mark.integration
def test_returns_error_on_non_existent_database():
    os.environ["BIGQUERY_METRICS_TABLE"] = "does_not_exist"
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = BigQueryMetricSink()
    assert isinstance(
        sink.store_metrics(
            [
                ProjectLeadTime(aggregate_id=aggregate_id, metric_value=lead_time),
            ]
        ),
        Exception,
    )


@pytest.mark.gcp
@pytest.mark.integration
def test_store_metrics_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = BigQueryMetricSink()
    assert (
        sink.store_metrics(
            [
                ProjectLeadTime(aggregate_id=aggregate_id, metric_value=lead_time),
            ]
        )
        is None
    )


@pytest.mark.gcp
@pytest.mark.integration
def test_store_resource_compliance_lead_time_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    container_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = BigQueryMetricSink()
    assert (
        sink.store_metrics(
            [
                ResourceComplianceLeadTime(
                    aggregate_id=aggregate_id,
                    metric_value=lead_time,
                    dimensions=ResourceComplianceExtraDimensions(
                        dimension_names=["container_id"], container_id=container_id
                    ),
                ),
            ]
        )
        is None
    )


@pytest.mark.gcp
@pytest.mark.integration
def test_store_patch_compliance_percentage_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    patch_percentage = random.randint(0, 100)
    sink = BigQueryMetricSink()
    assert (
        sink.store_metrics(
            [
                PatchCompliancePercentage(
                    aggregate_id=aggregate_id, metric_value=patch_percentage
                ),
            ]
        )
        is None
    )


@pytest.mark.gcp
@pytest.mark.integration
def test_store_resource_account_lead_time_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = BigQueryMetricSink()
    assert (
        sink.store_metrics(
            [
                AccountLeadTime(aggregate_id=aggregate_id, metric_value=lead_time),
            ]
        )
        is None
    )


@pytest.mark.gcp
@pytest.mark.integration
def test_store_guardrail_activation_count_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    count = random.randint(0, 100)
    sink = BigQueryMetricSink()
    assert (
        sink.store_metrics(
            [
                GuardrailActivationCount(
                    aggregate_id=aggregate_id,
                    metric_value=count,
                    dimensions=GuardrailExtraDimensions(
                        dimension_names=["guardrail_id"], guardrail_id=guardrail_id
                    ),
                ),
            ]
        )
        is None
    )


@pytest.mark.gcp
@pytest.mark.integration
def test_store_guardrail_max_activation_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    count = random.randint(0, 100)
    sink = BigQueryMetricSink()
    assert (
        sink.store_metrics(
            [
                GuardrailMaxActivation(
                    aggregate_id=aggregate_id,
                    metric_value=count,
                    dimensions=GuardrailExtraDimensions(
                        dimension_names=["guardrail_id"], guardrail_id=guardrail_id
                    ),
                ),
            ]
        )
        is None
    )


@pytest.mark.gcp
@pytest.mark.integration
def test_store_guardrail_lead_time_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = BigQueryMetricSink()
    assert (
        sink.store_metrics(
            [
                GuardrailLeadTime(
                    aggregate_id=aggregate_id,
                    metric_value=lead_time,
                    dimensions=GuardrailExtraDimensions(
                        dimension_names=["guardrail_id"], guardrail_id=guardrail_id
                    ),
                ),
            ]
        )
        is None
    )


@pytest.mark.gcp
@pytest.mark.integration
def test_store_identity_lead_time_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = BigQueryMetricSink()
    assert (
        sink.store_metrics(
            [
                IdentityLeadTime(aggregate_id=aggregate_id, metric_value=lead_time),
            ]
        )
        is None
    )
