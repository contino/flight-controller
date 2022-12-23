from time import sleep
from typing import Any
from uuid import uuid4
from behave import given, when, then
from datetime import datetime
import json

import boto3

eventBridge = boto3.client("events")
timeStream = boto3.client("timestream-query")


@given("a project has been requested")
def request_project(context: Any) -> None:
    context.aggregate_id = str(uuid4())
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
def create_project(context: Any) -> None:
    sleep(1)
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
def lead_time_stored(context: Any) -> None:
    sleep(2)
    query = f"select * from core_timestream_db.metrics_table where project_id = '{context.aggregate_id}'"
    result = timeStream.query(QueryString=query)
    print(query)
    print(result)
    assert len(result["Rows"]) == 1
