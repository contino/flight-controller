import os
import time
from typing import List, Optional

import boto3
import structlog

from src.drivers.metric_sink import MetricSink
from src.entities.metrics import Metric

logger = structlog.get_logger(__name__)


class TimeStreamMetricSink(MetricSink):
    def __init__(self) -> None:
        self.database_name = os.environ.get("TIMESTREAM_DATABASE_NAME")
        self.table_name = os.environ.get("TIMESTREAM_TABLE_NAME")
        self.timestream_client = boto3.client("timestream-write")

    def store_metrics(self, metrics: List[Metric]) -> Optional[Exception]:
        logger.msg(f"Writing records for metrics {metrics}")
        current_time = round(time.time() * 1000)
        records = []
        for metric in metrics:
            dimensions = [
                {"Name": "aggregate_id", "Value": metric.aggregate_id},
            ]
            if hasattr(metric, "dimensions"):
                dimensions += [
                    {"Name": dimension, "Value": getattr(metric.dimensions, dimension)}
                    for dimension in metric.dimensions.dimension_names
                ]
            record = {
                "Dimensions": dimensions,
                "MeasureValueType": "DOUBLE",
                "MeasureName": metric.metric_type,
                "Time": str(current_time),
                "MeasureValue": str(metric.metric_value),
            }

            records.append(record)

        try:
            if len(records) > 0:
                result = self.timestream_client.write_records(
                    DatabaseName=self.database_name,
                    TableName=self.table_name,
                    Records=records,
                    CommonAttributes={},
                )
                logger.msg(
                    f"WriteRecords Status: {result['ResponseMetadata']['HTTPStatusCode']}"
                )
        except Exception as err:
            logger.error(f"Error: {err}")
            return err
