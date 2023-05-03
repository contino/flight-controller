import json
import os
from datetime import datetime
from typing import List, Optional, Union
from uuid import UUID, uuid4

from google.cloud import bigquery

from src.drivers.event_sink import EventSink
from src.drivers.event_source import EventSource
from src.drivers.metric_sink import MetricSink
from src.entities.events import EVENT_CLASSES, Event
from src.entities.metrics import Metric


class BigQueryMetricSink(MetricSink):
    def __init__(self) -> None:
        self.TABLE_NAME = os.environ.get("BIGQUERY_METRICS_TABLE")
        self.client = bigquery.Client()

    def store_metrics(self, metrics: List[Metric]) -> Optional[Exception]:
        try:
            for metric in metrics:
                columns = f"aggregate_id, measure_name, time, measure_value"
                if hasattr(metric, "dimensions"):
                    for dimension in metric.dimensions.dimension_names:
                        columns += f", {dimension}"
                values = (
                    f"'{metric.aggregate_id}','{metric.metric_type}','{datetime.utcnow()}', {metric.metric_value}"
                )
                if hasattr(metric, "dimensions"):
                    for dimension in metric.dimensions.dimension_names:
                        values += f", '{getattr(metric.dimensions, dimension)}'"

                query = f"""
                INSERT `{self.TABLE_NAME}` ({columns})
                VALUES ({values})
                """

                response = self.client.query(query).result()
                self.client.close()
            return None
        except Exception as err:
            return err


class BigQueryEventSink(EventSink):
    def __init__(self) -> None:
        self.TABLE_NAME = os.environ.get("BIGQUERY_EVENTS_TABLE")
        self.client = bigquery.Client()

    def store_events(self, events: List[Event]) -> Optional[Exception]:
        try:
            values = ""
            for event in events:
                values += f"('{event.event_id}','{event.event_type}','{event.aggregate_id}','{event.aggregate_type}',{event.aggregate_version},{event.event_version},SAFE.PARSE_JSON('{json.dumps(event.payload.__dict__)}'),'{datetime.utcnow()}'),"
            values = values[:-1]

            query = f"""
            INSERT `{self.TABLE_NAME}`
            VALUES {values}
            """
            response = self.client.query(query).result()
            self.client.close()
            return None
        except Exception as err:
            return err


class BigQueryEventSource(EventSource):
    def __init__(self) -> None:
        self.TABLE_NAME = os.environ.get("BIGQUERY_EVENTS_TABLE")
        self.client = bigquery.Client()

    def get_events_for_aggregate(self, aggregate_id: str) -> Union[Exception, List[Event]]:
        try:
            query = f"""
            SELECT *
            FROM `{self.TABLE_NAME}`
            WHERE aggregate_id = '{aggregate_id}'
            ORDER BY aggregate_version ASC
            """
            events: List[Event] = []

            for row in self.client.query(query).result():
                event_type = row[1]
                if event_type in EVENT_CLASSES:
                    event_class, payload_class = EVENT_CLASSES[event_type]
                    payload = payload_class(**json.loads(row[6]))
                    event = event_class(
                        aggregate_id=row[2],
                        aggregate_type=row[3],
                        aggregate_version=int(row[4]),
                        event_id=UUID(row[0]),
                        event_version=int(row[5]),
                        payload=payload,
                    )
                    events.append(event)
            self.client.close()
            return events
        except Exception as err:
            return err
