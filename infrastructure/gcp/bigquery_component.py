from constructs import Construct
import json
from cdktf_cdktf_provider_google import (
    bigquery_table, 
    bigquery_dataset, 
    service_account,
)

class BigQueryComponent(Construct):
    def __init__(
        self, 
        scope: Construct, 
        id: str, 
        project_id: str, 
        location: str, 
        event_table: str, 
        metric_table: str, 
        cloudrun_account: service_account.ServiceAccount):
        
        super().__init__(scope, id)
    
        
        self.event_dataset = bigquery_dataset.BigqueryDataset(
            self,
            "event_dataset",
            dataset_id=event_table,
            location=location,
            project=project_id,
        )
        
        self.event_table = bigquery_table.BigqueryTable(
            self,
            "event_table",
            dataset_id=self.event_dataset.dataset_id,
            table_id="events_data",
            project=project_id,
            schema=json.dumps([
                {
                    "name": "event_id",
                    "type": "STRING",
                    "mode": "REQUIRED"
                },
                {
                    "name": "event_type",
                    "type": "STRING",
                    "mode": "REQUIRED"
                },
                {
                    "name": "aggregate_id",
                    "type": "STRING",
                    "mode": "REQUIRED"
                },
                {
                    "name": "aggregate_type",
                    "type": "STRING",
                    "mode": "REQUIRED"
                },
                {
                    "name": "aggregate_version",
                    "type": "INT64",
                    "mode": "REQUIRED"
                },
                {
                    "name": "event_version",
                    "type": "INT64",
                    "mode": "REQUIRED"
                },
                {
                    "name": "payload",
                    "type": "JSON",
                    "mode": "REQUIRED"
                },
                {
                    "name": "timestamp",
                    "type": "TIMESTAMP",
                    "mode": "REQUIRED"
                }
            ]),
            deletion_protection=False,
        )

        self.metric_dataset = bigquery_dataset.BigqueryDataset(
            self,
            "metric_dataset",
            dataset_id=metric_table,
            location=location,
            project=project_id,
        )

        self.metric_table = bigquery_table.BigqueryTable(
            self,
            "metric_table",
            dataset_id=self.metric_dataset.dataset_id,
            table_id="metrics_data",
            project=project_id,
            schema=json.dumps([
                {
                    "name": "aggregate_id",
                    "type": "STRING",
                    "mode": "REQUIRED"
                },
                {
                    "name": "guardrail_id",
                    "type": "STRING",
                    "mode": "REQUIRED"
                },
                {
                    "name": "container_id",
                    "type": "STRING",
                    "mode": "REQUIRED"
                },
                {
                    "name": "measure_name",
                    "type": "STRING",
                    "mode": "REQUIRED"
                },
                {
                    "name": "time",
                    "type": "TIMESTAMP",
                    "mode": "REQUIRED"
                },
                {
                    "name": "measure_value",
                    "type": "INT64",
                    "mode": "REQUIRED"
                },
            ]),
            deletion_protection=False,
        )