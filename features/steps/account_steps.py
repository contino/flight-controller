from time import sleep
from behave import given, when, then
from datetime import datetime
import json
import random
import string
import boto3

from src.entities.accounts import AccountLeadTime

event_bridge = boto3.client("events")
time_stream = boto3.client('timestream-query')


@given("an account has been requested")
def request_account(context):
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))

    response = event_bridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test account request Event",
                "Detail": json.dumps(
                    {
                        "event_type": "account_requested",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )

    assert response["FailedEntryCount"] == 0



@when("the account has been created")
def assing_account(context):
    sleep(3)
    requested_time = int(round(datetime.utcnow().timestamp()))
    event_bridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test account create Event",
                "Detail": json.dumps(
                    {
                        "event_type": "account_created",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )


@then("the account created lead time is stored correctly")
def lead_time_stored(context):
    sleep(2)
    result = time_stream.query(
        QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = '{AccountLeadTime.metric_type}'"
    )
    assert len(result["Rows"]) == 1