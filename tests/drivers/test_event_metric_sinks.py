from datetime import datetime
import json
import random
import string
from uuid import uuid4, UUID

from google.cloud import bigquery
import pytest

from src.drivers.dynamo_event_sink_source import (
    DynamoEventSink,
    DynamoEventSource
)

from src.drivers.timestream_metric_sink import (
    TimeStreamMetricSink
)

from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectLeadTime,
    ProjectRequestedPayload,
    ProjectRequested,
)

@pytest.mark.integration
def get_big_query_client():
    client = bigquery.Client()


@pytest.mark.integration
def test_store_metrics_does_not_return_error():
    correlation_id = "testMetric"
    lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
    assert sink.store_metrics([ProjectLeadTime(correlation_id, lead_time)]) is None


@pytest.mark.integration
def test_retrieves_aggregate_events_from_bigquery():
    correlation_id = "testEvent"
    eventId = "73333023-5fbe-4ad5-aaf9-dcd9a245dae3"
    eventId2 = "73333023-5fbe-4ad5-aaf9-dcd9a245dae4"
    projectRequested = ProjectRequested(
        aggregateId=correlation_id,
        aggregateType="Project",
        aggregateVersion=1,
        eventId=UUID(eventId),
        eventVersion=1,
        payload=ProjectRequestedPayload(correlation_id, datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")),
    )
    projectCreated = ProjectCreated(
        aggregateId=correlation_id,
        aggregateType="Project",
        aggregateVersion=2,
        eventId=UUID(eventId2),
        eventVersion=1,
        payload=ProjectCreatedPayload(correlation_id, datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")),
    )
    sink = DynamoEventSink()
    sink.store_events([projectRequested, projectCreated])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(projectRequested.aggregateId)

    assert got == [projectRequested, projectCreated]
