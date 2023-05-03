import os
import random
import string

import pytest

from src.drivers.timestream_metric_sink import TimeStreamMetricSink
from src.entities.accounts import AccountLeadTime
from src.entities.compliance import (
    ResourceComplianceExtraDimensions,
    ResourceComplianceLeadTime,
)
from src.entities.guardrail import (
    GuardrailActivationCount,
    GuardrailExtraDimensions,
    GuardrailLeadTime,
    GuardrailMaxActivation,
)
from src.entities.identity import IdentityLeadTime
from src.entities.patch import PatchCompliancePercentage
from src.entities.projects import ProjectLeadTime


@pytest.fixture(autouse=True)
def set_env_vars():
    os.environ["TIMESTREAM_DATABASE_NAME"] = "core_timestream_db"
    os.environ["TIMESTREAM_TABLE_NAME"] = "metrics_table"


@pytest.mark.aws
@pytest.mark.integration
def test_returns_error_on_non_existent_database():
    os.environ["TIMESTREAM_DATABASE_NAME"] = "does_not_exist"
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
    assert isinstance(
        sink.store_metrics(
            [
                ProjectLeadTime(aggregate_id=aggregate_id, metric_value=lead_time),
            ]
        ),
        Exception,
    )


@pytest.mark.aws
@pytest.mark.integration
def test_store_metrics_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
    assert (
        sink.store_metrics(
            [
                ProjectLeadTime(aggregate_id=aggregate_id, metric_value=lead_time),
            ]
        )
        is None
    )


@pytest.mark.aws
@pytest.mark.integration
def test_store_resource_compliance_lead_time_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    container_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
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


@pytest.mark.aws
@pytest.mark.integration
def test_store_patch_compliance_percentage_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    patch_percentage = random.randint(0, 100)
    sink = TimeStreamMetricSink()
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


@pytest.mark.aws
@pytest.mark.integration
def test_store_resource_account_lead_time_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
    assert (
        sink.store_metrics(
            [
                AccountLeadTime(aggregate_id=aggregate_id, metric_value=lead_time),
            ]
        )
        is None
    )


@pytest.mark.aws
@pytest.mark.integration
def test_store_guardrail_activation_count_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    count = random.randint(0, 100)
    sink = TimeStreamMetricSink()
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


@pytest.mark.aws
@pytest.mark.integration
def test_store_guardrail_max_activation_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    count = random.randint(0, 100)
    sink = TimeStreamMetricSink()
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


@pytest.mark.aws
@pytest.mark.integration
def test_store_guardrail_lead_time_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
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


@pytest.mark.aws
@pytest.mark.integration
def test_store_identity_lead_time_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
    assert (
        sink.store_metrics(
            [
                IdentityLeadTime(aggregate_id=aggregate_id, metric_value=lead_time),
            ]
        )
        is None
    )
