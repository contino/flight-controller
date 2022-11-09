import boto3
import structlog
from typing import List, Optional
import time


from .metric_sink import MetricSink
from src.entities.projects import (
    ProjectLeadTime,
    ProjectAssignedLeadTime
)

TIMESTREAM_DATABASE_NAME = "core_flight_controller_db"
TIMESTREAM_TABLE_NAME = "event_time_series"

logger = structlog.get_logger(__name__)



class TimeStreamMetricSink(MetricSink):
    def __init__(self) -> None:
        ## time stream client
        self.timestreamClient = boto3.client('timestream-write')

    def store_metrics(self, metrics: List[str]) -> Optional[Exception]:
        logger.msg(f"Writing records for metrics {metrics}")
        current_time = round(time.time()*1000)
        records = []
        for metric in metrics:
            dimensions = [
                {'Name': 'project_id', 'Value': metric.project_id},
                {'Name': 'az', 'Value': 'az1'},
                {'Name': 'hostname', 'Value': 'host1'}
            ]
            project_metric = {
                'Dimensions': dimensions,
                'MeasureValue': str(metric.lead_time),
                'MeasureValueType': 'DOUBLE',
                'Time': str(current_time)
            }

            if isinstance(metric, ProjectLeadTime):
                project_metric["MeasureName"]="project_lead_time"
            elif isinstance(metric, ProjectAssignedLeadTime):
                project_metric["MeasureName"]="project_assign_time"

            records.append(project_metric)

        try:
            if len(records)>0:
                result = self.timestreamClient.write_records(DatabaseName=TIMESTREAM_DATABASE_NAME, TableName=TIMESTREAM_TABLE_NAME,
                                                    Records=records, CommonAttributes={})
                logger.msg(f"WriteRecords Status: {result['ResponseMetadata']['HTTPStatusCode']}")
        except self.timestreamClient.exceptions.RejectedRecordsException as err:
            logger.error(f"rejected records: {err}")
            return err
        except Exception as err:
            logger.error(f"Error: {err}")
            return err
