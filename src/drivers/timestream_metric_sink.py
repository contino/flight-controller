import time
from typing import List, Optional

import boto3
import structlog

from src.entities.metrics import Metric
from src.entities.projects import ProjectAssignedLeadTime, ProjectLeadTime

from .metric_sink import MetricSink

TIMESTREAM_DATABASE_NAME = "core_timestream_db"
TIMESTREAM_TABLE_NAME = "metrics_table"

logger = structlog.get_logger(__name__)


class TimeStreamMetricSink(MetricSink):
    def __init__(self) -> None:
        self.timestream = boto3.client("timestream-write")

    def store_metrics(self, metrics: List[Metric]) -> Optional[Exception]:
        logger.msg(f"Writing records for metrics {metrics}")
        current_time = round(time.time() * 1000)
        records = []
        for metric in metrics:
            dimensions = [
                {"Name": "project_id", "Value": metric.project_id},
                {"Name": "az", "Value": "az1"},
                {"Name": "hostname", "Value": "host1"},
            ]
            project_metric = {
                "Dimensions": dimensions,
                "MeasureValue": str(metric.lead_time),
                "MeasureValueType": "DOUBLE",
                "Time": str(current_time),
            }

            if isinstance(metric, ProjectLeadTime):
                project_metric["MeasureName"] = "project_lead_time"
            elif isinstance(metric, ProjectAssignedLeadTime):
                project_metric["MeasureName"] = "project_assign_time"

            records.append(project_metric)

        try:
            if len(records) > 0:
                result = self.timestream.write_records(
                    DatabaseName=TIMESTREAM_DATABASE_NAME,
                    TableName=TIMESTREAM_TABLE_NAME,
                    Records=records,
                    CommonAttributes={},
                )
                logger.msg(
                    f"WriteRecords Status: {result['ResponseMetadata']['HTTPStatusCode']}"
                )
        except self.timestream.exceptions.RejectedRecordsException as err:
            logger.error(f"rejected records: {err}")
            return err
        except Exception as err:
            logger.error(f"Error: {err}")
            return err
