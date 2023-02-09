from datetime import datetime
import random
from uuid import UUID
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
    ProjectRequestedPayload,
    ProjectRequested,
    ProjectLeadTime,
    ProjectAssignedLeadTime
)




@pytest.mark.integration
def test_store_metrics_does_not_return_error():
    aggregate_id = "testMetric"
    lead_time = random.randint(0, 7200)
    assigned_lead_time = random.randint(0, 7200)
    sink = TimeStreamMetricSink()
    assert sink.store_metrics([ProjectAssignedLeadTime(aggregate_id, assigned_lead_time), ProjectLeadTime(aggregate_id, lead_time)]) is None


@pytest.mark.integration
def test_retrieves_aggregate_events_from_dynamodb():
    aggregate_id = "testEvent"
    eventId = "73333023-5fbe-4ad5-aaf9-dcd9a245dae3"
    eventId2 = "73333023-5fbe-4ad5-aaf9-dcd9a245dae4"
    projectRequested = ProjectRequested(
        aggregateId=aggregate_id,
        aggregateType="Project",
        aggregateVersion=1,
        eventId=UUID(eventId),
        eventVersion=1,
        payload=ProjectRequestedPayload(aggregate_id, int(round(datetime.utcnow().timestamp()))),
    )
    projectCreated = ProjectCreated(
        aggregateId=aggregate_id,
        aggregateType="Project",
        aggregateVersion=2,
        eventId=UUID(eventId2),
        eventVersion=1,
        payload=ProjectCreatedPayload(aggregate_id, int(round(datetime.utcnow().timestamp()))),
    )
    sink = DynamoEventSink()
    sink.store_events([projectRequested, projectCreated])

    source = DynamoEventSource()

    got = source.get_events_for_aggregate(projectRequested.aggregateId)

    assert got == [projectRequested, projectCreated]
