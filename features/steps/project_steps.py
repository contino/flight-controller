from time import sleep
from behave import given, when, then
from datetime import datetime
import json
import random
import string
import boto3

event_bridge = boto3.client("events")
time_stream = boto3.client("timestream-query")
aggregate_id = "behaveTest"


@given("a project has been requested")
def request_project(context):
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))

    event_bridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test project request Event",
                "Detail": json.dumps(
                    {
                        "event_type": "project_requested",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )


@when("the project has been created")
def create_project(context):
    sleep(3)
    requested_time = int(round(datetime.utcnow().timestamp()))
    event_bridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test project create Event",
                "Detail": json.dumps(
                    {
                        "event_type": "project_created",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )


@then("the lead time is stored correctly")
def lead_time_stored(context):
    sleep(2)
    result = time_stream.query(
        QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = 'project_lead_time'"
    )
    assert len(result["Rows"]) == 1
