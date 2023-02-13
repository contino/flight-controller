import pytest
import random

from src.drivers.timestream_metric_sink import TimeStreamMetricSink

from src.entities.projects import ProjectLeadTime
from src.entities.compliance import ResourceComplianceLeadTime
from src.entities.accounts import AccountLeadTime
from src.entities.patch import PatchCompliancePercentage

@pytest.mark.integration
def test_store_metrics_does_not_return_error():
    aggregate_id = "testMetric"
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
    aggregate_id = "testMetric"
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
    aggregate_id = "testMetric"
    patch_compliance_percentage = random.randint(0, 100)
    sink = TimeStreamMetricSink()
    assert (
        sink.store_metrics(
            [
                PatchCompliancePercentage(aggregate_id, patch_compliance_percentage),
            ]
        )
        is None
    )


@pytest.mark.integration
def test_store_resource_account_lead_time_does_not_return_error():
    aggregate_id = "testMetric"
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