from time import sleep
from behave import given, when, then
from datetime import datetime
import json

import boto3

eventBridge = boto3.client("events")
timeStream = boto3.client('timestream-query')
aggregate_id = "behaveTest"


@given("an account has been requested")
def request_account(context):
    requested_time = int(round(datetime.utcnow().timestamp()))

    eventBridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test account request Event",
                "Detail": json.dumps(
                    {
                        "event_type": "AccountRequested",
                        "aggregate_id": f"{aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus",
            }
        ]
    )


@given("an account has been assigned")
def assing_account(context):
    sleep(3)
    requested_time = int(round(datetime.utcnow().timestamp()))
    eventBridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test account assign Event",
                "Detail": json.dumps(
                    {
                        "event_type": "AccountAssigned",
                        "aggregate_id": f"{aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus",
            }
        ]
    )


@when("the account has been created")
def assing_account(context):
    sleep(3)
    requested_time = int(round(datetime.utcnow().timestamp()))
    eventBridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test account create Event",
                "Detail": json.dumps(
                    {
                        "event_type": "ProjectCreated",
                        "aggregate_id": f"{aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus",
            }
        ]
    )


@then("the lead time is stored correctly")
def lead_time_stored(context):
    sleep(2)
    result = timeStream.query(QueryString='select * from core_timestream_db.metrics_table where time > ago(10s) order by time desc')
    print(result)
    assert len(result["Rows"]) == 1
