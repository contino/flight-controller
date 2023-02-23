from time import sleep
from behave import given, when, then
from datetime import datetime
import json
import random
import string
import boto3

from src.entities.identity import IdentityLeadTime

eventBridge = boto3.client("events")
timeStream = boto3.client("timestream-query")


@given("an identity has been requested")
def request_identity(context):
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))

    response = eventBridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test identity request Event",
                "Detail": json.dumps(
                    {
                        "event_type": "identity_requested",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )

    assert response["FailedEntryCount"] == 0


@when("the identity has been created")
def created_identity(context):
    sleep(3)
    requested_time = int(round(datetime.utcnow().timestamp()))
    eventBridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test identity create Event",
                "Detail": json.dumps(
                    {
                        "event_type": "identity_created",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )


@then("the identity created lead time is stored correctly")
def lead_time_stored(context):
    sleep(2)
    result = timeStream.query(
        QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = '{IdentityLeadTime.metric_type}'"
    )
    assert len(result["Rows"]) == 1
