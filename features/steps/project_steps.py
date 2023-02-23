from time import sleep
from behave import given, when, then
from datetime import datetime
import json
import random
import string
import boto3

from src.entities.projects import ProjectLeadTime

eventBridge = boto3.client("events")
timeStream = boto3.client("timestream-query")
aggregate_id = "behaveTest"


@given("a project has been requested")
def request_project(context):
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))

    eventBridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test project request Event",
                "Detail": json.dumps(
                    {
                        "event_type": "ProjectRequested",
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
    eventBridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test project create Event",
                "Detail": json.dumps(
                    {
                        "event_type": "ProjectCreated",
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
    result = timeStream.query(
        QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = '{ProjectLeadTime.metricType}'"
    )
    assert len(result["Rows"]) == 1
