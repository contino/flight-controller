from datetime import datetime
import json
import random
import string
from uuid import uuid4

from google.cloud import bigquery
import pytest

from src.drivers.bigquery import (
    BigQueryEventSink,
    BigQueryEventSource,
    BigQueryMetricSink,
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
    project_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = BigQueryMetricSink()
    assert sink.store_metrics([ProjectLeadTime(project_id, lead_time)]) is None


@pytest.mark.integration
def test_stores_metric_in_bigquery():
    project_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = BigQueryMetricSink()
    sink.store_metrics([ProjectLeadTime(project_id, lead_time)])

    query = f"""
    SELECT lead_time
    FROM `flight_controller.project_lead_times`
    WHERE project_id = '{project_id}'
  """

    got = client.query(query).result()
    rows = 0
    for _ in got:
        rows += 1

    assert rows == 1


@pytest.mark.integration
def test_stores_lead_time_correctly():
    project_id = "".join(random.choices(string.ascii_letters, k=12))
    lead_time = random.randint(0, 7200)
    sink = BigQueryMetricSink()
    sink.store_metrics([ProjectLeadTime(project_id, lead_time)])

    query = f"""
    SELECT lead_time
    FROM `flight_controller.project_lead_times`
    WHERE project_id = '{project_id}'
  """
    got = client.query(query).result()

    for row in got:
        assert row[0] == lead_time
        break


@pytest.mark.integration
def test_store_events_does_not_return_error():
    project_id = "".join(random.choices(string.ascii_letters, k=12))
    projectRequested = ProjectRequested(
        aggregateId=project_id,
        aggregateType="Project",
        aggregateVersion=1,
        eventId=uuid4(),
        eventVersion=1,
        payload=ProjectRequestedPayload(project_id, datetime.utcnow().timestamp()),
    )
    sink = BigQueryEventSink()
    assert sink.store_events([projectRequested]) is None


@pytest.mark.integration
def test_stores_events_in_bigquery():
    project_id = "".join(random.choices(string.ascii_letters, k=12))
    projectRequested = ProjectRequested(
        aggregateId=project_id,
        aggregateType="Project",
        aggregateVersion=1,
        eventId=uuid4(),
        eventVersion=1,
        payload=ProjectRequestedPayload(project_id, datetime.utcnow().timestamp()),
    )
    sink = BigQueryEventSink()
    sink.store_events([projectRequested])

    query = f"""
    SELECT *
    FROM `flight_controller.events`
    WHERE event_id = '{projectRequested.eventId}'
  """

    got = client.query(query).result()
    rows = 0
    for _ in got:
        rows += 1

    assert rows == 1


@pytest.mark.integration
def test_stores_event_correctly_in_bigquery():
    project_id = "".join(random.choices(string.ascii_letters, k=12))
    projectRequested = ProjectRequested(
        aggregateId=project_id,
        aggregateType="Project",
        aggregateVersion=1,
        eventId=uuid4(),
        eventVersion=1,
        payload=ProjectRequestedPayload(project_id, datetime.utcnow().timestamp()),
    )

    want = [
        project_id,
        "Project",
        1,
        str(projectRequested.eventId),
        "ProjectRequested",
        1,
        json.dumps(projectRequested.payload.__dict__).replace(" ", ""),
    ]
    sink = BigQueryEventSink()
    sink.store_events([projectRequested])

    query = f"""
    SELECT aggregate_id, aggregate_type, aggregate_version, event_id, event_type, event_version, payload
    FROM `flight_controller.events`
    WHERE event_id = '{projectRequested.eventId}'
  """

    got = client.query(query).result()
    for row in got:
        print(row)
        for i, item in enumerate(row):
            assert item == want[i]


@pytest.mark.integration
def test_retrieves_aggregate_event_from_bigquery():
    project_id = "".join(random.choices(string.ascii_letters, k=12))
    projectRequested = ProjectRequested(
        aggregateId=project_id,
        aggregateType="Project",
        aggregateVersion=1,
        eventId=uuid4(),
        eventVersion=1,
        payload=ProjectRequestedPayload(project_id, datetime.utcnow().timestamp()),
    )
    sink = BigQueryEventSink()
    sink.store_events([projectRequested])

    source = BigQueryEventSource()

    got = source.get_events_for_aggregate(projectRequested.aggregateId)

    assert len(got) == 1


@pytest.mark.integration
def test_retrieves_aggregate_events_from_bigquery():
    project_id = "".join(random.choices(string.ascii_letters, k=12))
    projectRequested = ProjectRequested(
        aggregateId=project_id,
        aggregateType="Project",
        aggregateVersion=1,
        eventId=uuid4(),
        eventVersion=1,
        payload=ProjectRequestedPayload(project_id, datetime.utcnow().timestamp()),
    )
    projectCreated = ProjectCreated(
        aggregateId=project_id,
        aggregateType="Project",
        aggregateVersion=2,
        eventId=uuid4(),
        eventVersion=1,
        payload=ProjectCreatedPayload(project_id, datetime.utcnow().timestamp()),
    )
    sink = BigQueryEventSink()
    sink.store_events([projectRequested, projectCreated])

    source = BigQueryEventSource()

    got = source.get_events_for_aggregate(projectRequested.aggregateId)

    assert got == [projectRequested, projectCreated]
