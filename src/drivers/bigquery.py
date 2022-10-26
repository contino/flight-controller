from datetime import datetime
import json
from typing import List, Optional, Union
from uuid import UUID, uuid4

from google.cloud import bigquery
from src.drivers.event_source import EventSource
from src.entities.events import Event
from src.entities.metrics import Metric
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
)

from .metric_sink import MetricSink
from .event_sink import EventSink


class BigQueryMetricSink(MetricSink):
    def store_metrics(self, metrics: List[Metric]) -> Optional[Exception]:
        if metrics:
            client = bigquery.Client()
            values = ""
            for metric in metrics:
                values += (
                    f"('{metric.project_id}',{metric.lead_time},'{datetime.utcnow()}'),"
                )
            values = values[:-1]
            query = f"""
        INSERT `flight_controller.project_lead_times`
        VALUES {values}
        """

            print(query)

            client.query(query).result()

        return None


class BigQueryEventSink(EventSink):
    def store_events(self, events: List[Event]) -> Optional[Exception]:
        client = bigquery.Client()
        values = ""
        for event in events:
            values += f"('{event.eventId}','{event.eventType}','{event.aggregateId}','{event.aggregateType}',{event.aggregateVersion},{event.eventVersion},SAFE.PARSE_JSON('{json.dumps(event.payload.__dict__)}'),'{datetime.utcnow()}'),"
        values = values[:-1]

        query = f"""
      INSERT `flight_controller.events`
      VALUES {values}
    """

        print(query)

        client.query(query).result()

        return None


class BigQueryEventSource(EventSource):
    def get_events_for_aggregate(self, aggregate_id: str) -> List[Event]:
        client = bigquery.Client()
        query = f"""
        SELECT aggregate_id, aggregate_type, aggregate_version, event_id, event_version, payload, event_type
        FROM `flight_controller.events`
        WHERE aggregate_id = '{aggregate_id}'
        ORDER BY aggregate_version ASC
        """

        print(query)

        events: List[Event] = []

        for row in client.query(query).result():
            payload = json.loads(row[5])
            if row[6] == "ProjectRequested":
                events.append(
                    ProjectRequested(
                        row[0],
                        row[1],
                        row[2],
                        UUID(row[3]),
                        row[4],
                        ProjectRequestedPayload(
                            payload["project_id"],
                            payload["requested_time"],
                        ),
                        row[6],
                    )
                )
            if row[6] == "ProjectCreated":
                events.append(
                    ProjectCreated(
                        row[0],
                        row[1],
                        row[2],
                        UUID(row[3]),
                        row[4],
                        ProjectCreatedPayload(
                            payload["project_id"],
                            payload["created_time"],
                        ),
                        row[6],
                    )
                )

        return events
