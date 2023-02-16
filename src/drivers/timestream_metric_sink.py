import boto3
import structlog
from typing import List, Optional
import time

from .metric_sink import MetricSink
from src.entities.metrics import Metric
from src.entities.compliance import ResourceComplianceLeadTime
from src.entities.patch import PatchCompliancePercentage
from src.entities.projects import ProjectLeadTime, ProjectAssignedLeadTime
from src.entities.accounts import AccountLeadTime
from src.entities.guardrail import (
    GuardrailActivationCount,
    GuardrailMaxActivation,
    GuardrailLeadTime
)


TIMESTREAM_DATABASE_NAME = "core_timestream_db"
TIMESTREAM_TABLE_NAME = "metrics_table"

logger = structlog.get_logger(__name__)


class TimeStreamMetricSink(MetricSink):
    def __init__(self) -> None:
        self.timestreamClient = boto3.client("timestream-write")

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
                "Time": str(current_time),
            }
            if isinstance(metric, ProjectLeadTime):
                record["MeasureName"] = "project_lead_time"
                record["MeasureValue"] = str(metric.lead_time)
            elif isinstance(metric, ProjectAssignedLeadTime):
                record["MeasureName"] = "project_assign_time"
                record["MeasureValue"] = str(metric.lead_time)
            elif isinstance(metric, ResourceComplianceLeadTime):
                record["MeasureName"] = "resource_compliance_lead_time"
                record["MeasureValue"] = str(metric.lead_time)
            elif isinstance(metric, AccountLeadTime):
                record["MeasureName"] = "account_lead_time"
                record["MeasureValue"] = str(metric.lead_time)
            elif isinstance(metric, PatchCompliancePercentage):
                record["MeasureName"] = "patch_compliance_percentage"
                record["MeasureValue"] = str(metric.percentage)
            elif isinstance(metric, GuardrailActivationCount):
                record["Dimensions"].append({"Name": "guardrail_id", "Value": metric.guardrail_id})
                record["MeasureName"] = "guardrail_activation_count"
                record["MeasureValue"] = str(metric.count)
            elif isinstance(metric, GuardrailMaxActivation):
                record["Dimensions"].append({"Name": "guardrail_id", "Value": metric.guardrail_id})
                record["MeasureName"] = "guardrail_max_activation"
                record["MeasureValue"] = str(metric.count)
            elif isinstance(metric, GuardrailLeadTime):
                record["Dimensions"].append({"Name": "guardrail_id", "Value": metric.guardrail_id})
                record["MeasureName"] = "guardrail_lead_time"
                record["MeasureValue"] = str(metric.lead_time)

            records.append(record)

        try:
            if len(records) > 0:
                result = self.timestreamClient.write_records(
                    DatabaseName=TIMESTREAM_DATABASE_NAME,
                    TableName=TIMESTREAM_TABLE_NAME,
                    Records=records,
                    CommonAttributes={},
                )
                logger.msg(
                    f"WriteRecords Status: {result['ResponseMetadata']['HTTPStatusCode']}"
                )
        except self.timestreamClient.exceptions.RejectedRecordsException as err:
            logger.error(f"rejected records: {err.response['RejectedRecords']}")
            return err
        except Exception as err:
            logger.error(f"Error: {err}")
            return err
