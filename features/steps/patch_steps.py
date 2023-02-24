from time import sleep
from behave import given, when, then
from datetime import datetime
import json
import random
import string
import boto3

from src.entities.patch import PatchCompliancePercentage

event_bridge = boto3.client("events")
time_stream = boto3.client("timestream-query")


@when("patch run summary is complete")
def received_summary(context):
    sleep(3)
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))
    event_bridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test Patch Summary Event",
                "Detail": json.dumps(
                    {
                        "event_type": "patch_run_summary",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                        "failed_instances": "i-adslkjfds,i-89dsfkjdkfj",
                        "successful_instances": "i-peoritdsfl",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )


@then("the compliance percentage is stored correctly")
def compliance_percentage_stored(context):
    sleep(2)
    result = time_stream.query(
        QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = '{PatchCompliancePercentage.metric_type}'"
    )
    assert len(result["Rows"]) == 1