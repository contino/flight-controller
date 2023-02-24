import random
import string

import pytest

from src.drivers.timestream_metric_sink import TimeStreamMetricSink
from src.entities.accounts import AccountLeadTime
from src.entities.compliance import ResourceComplianceLeadTime
from src.entities.guardrail import (
    GuardrailActivationCount,
    GuardrailLeadTime,
    GuardrailMaxActivation,
)
from src.entities.patch import PatchCompliancePercentage
from src.entities.projects import ProjectLeadTime


@pytest.mark.integration
def test_store_metrics_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
    assert (
        sink.store_metrics(
            [
                ProjectLeadTime(aggregate_id, lead_time),
            ]
        )
        is None
    )


@pytest.mark.integration
def test_store_resource_compliance_lead_time_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
    assert (
        sink.store_metrics(
            [
                ResourceComplianceLeadTime(aggregate_id, lead_time),
            ]
        )
        is None
    )


@pytest.mark.integration
def test_store_patch_compliance_percentage_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    patch_percentage = random.randint(0, 100)
    sink = TimeStreamMetricSink()
    assert (
        sink.store_metrics(
            [
                PatchCompliancePercentage(aggregate_id, patch_percentage),
            ]
        )
        is None
    )


@pytest.mark.integration
def test_store_resource_account_lead_time_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
    assert (
        sink.store_metrics(
            [
                AccountLeadTime(aggregate_id, lead_time=lead_time),
            ]
        )
        is None
    )


@pytest.mark.integration
def test_store_gaurdrail_activation_count_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    count = random.randint(0, 100)
    sink = TimeStreamMetricSink()
    assert (
        sink.store_metrics(
            [
                GuardrailActivationCount(aggregate_id, guardrail_id, count),
            ]
        )
        is None
    )


@pytest.mark.integration
def test_store_gaurdrail_max_activation_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    count = random.randint(0, 100)
    sink = TimeStreamMetricSink()
    assert (
        sink.store_metrics(
            [
                GuardrailMaxActivation(aggregate_id, guardrail_id, count),
            ]
        )
        is None
    )


@pytest.mark.integration
def test_store_gaurdrail_lead_time_does_not_return_error():
    aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
    assert (
        sink.store_metrics(
            [
                GuardrailLeadTime(aggregate_id, guardrail_id, lead_time),
            ]
        )
        is None
    )