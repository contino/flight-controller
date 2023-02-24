from typing import List, Optional
import time

import boto3
import structlog

from src.drivers.metric_sink import MetricSink
from src.entities.metrics import Metric
from src.entities.accounts import AccountLeadTime
from src.entities.compliance import ResourceComplianceLeadTime
from src.entities.guardrail import (
    GuardrailActivationCount,
    GuardrailMaxActivation,
    GuardrailLeadTime
)
from src.entities.patch import PatchCompliancePercentage
from src.entities.projects import ProjectLeadTime, ProjectAssignedLeadTime


TIMESTREAM_DATABASE_NAME = "core_timestream_db"
TIMESTREAM_TABLE_NAME = "metrics_table"

logger = structlog.get_logger(__name__)


class TimeStreamMetricSink(MetricSink):
    def __init__(self) -> None:
        self.timestream_client = boto3.client("timestream-write")

    def store_metrics(self, metrics: List[Metric]) -> Optional[Exception]:
        logger.msg(f"Writing records for metrics {metrics}")
        current_time = round(time.time() * 1000)
        records = []
        for metric in metrics:
            dimensions = [
                {"Name": "aggregate_id", "Value": metric.aggregate_id},
            ]
            record = {
                "Dimensions": dimensions,
                "MeasureValueType": "DOUBLE",
                "MeasureName": metric.metric_type,
                "Time": str(current_time),
            }
            if isinstance(metric, ProjectLeadTime):
                record["MeasureValue"] = str(metric.lead_time)
            elif isinstance(metric, ProjectAssignedLeadTime):
                record["MeasureValue"] = str(metric.lead_time)
            elif isinstance(metric, ResourceComplianceLeadTime):
                record["MeasureValue"] = str(metric.lead_time)
            elif isinstance(metric, AccountLeadTime):
                record["MeasureValue"] = str(metric.lead_time)
            elif isinstance(metric, PatchCompliancePercentage):
                record["MeasureValue"] = str(metric.percentage)
            elif isinstance(metric, GuardrailActivationCount):
                record["Dimensions"].append({"Name": "guardrail_id", "Value": metric.guardrail_id})
                record["MeasureValue"] = str(metric.count)
            elif isinstance(metric, GuardrailMaxActivation):
                record["Dimensions"].append({"Name": "guardrail_id", "Value": metric.guardrail_id})
                record["MeasureValue"] = str(metric.count)
            elif isinstance(metric, GuardrailLeadTime):
                record["Dimensions"].append({"Name": "guardrail_id", "Value": metric.guardrail_id})
                record["MeasureValue"] = str(metric.lead_time)

            records.append(record)

        try:
            if len(records) > 0:
                result = self.timestream_client.write_records(
                    DatabaseName=TIMESTREAM_DATABASE_NAME,
                    TableName=TIMESTREAM_TABLE_NAME,
                    Records=records,
                    CommonAttributes={},
                )
                logger.msg(
                    f"WriteRecords Status: {result['ResponseMetadata']['HTTPStatusCode']}"
                )
        except self.timestream_client.exceptions.RejectedRecordsException as err:
            logger.error(f"rejected records: {err.response['RejectedRecords']}")
            return err
        except Exception as err:
            logger.error(f"Error: {err}")
            return err
