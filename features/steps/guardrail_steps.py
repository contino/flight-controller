from time import sleep
from behave import given, then, when
from datetime import datetime
import json
import random
import string
import boto3

event_bridge = boto3.client("events")
time_stream = boto3.client("timestream-query")


def guardrail_activated(context):
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    context.guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))
    event_bridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test guardrail activated event",
                "Detail": json.dumps(
                    {
                        "event_type": "guardrail_activated",
                        "guardrail_id": f"{context.guardrail_id}",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )


@given("a guardrail has been activated")
def given_guardrail_activated(context):
    guardrail_activated(context)


@when("a guardrail has been activated")
def when_guardrail_activated(context):
    guardrail_activated(context)


@when("a guardrail passes")
def guardrail_passes(context):
    sleep(3)
    requested_time = int(round(datetime.utcnow().timestamp()))
    event_bridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test guardrail passed event",
                "Detail": json.dumps(
                    {
                        "event_type": "guardrail_passed",
                        "guardrail_id": f"{context.guardrail_id}",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )


@then("the activation count is stored correctly")
def metric_stored(context):
    sleep(2)
    result = time_stream.query(
        QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = 'guardrail_activation_count'"
    )
    assert len(result["Rows"]) == 1


@then("the guardrail lead time is stored correctly")
def metric_stored(context):
    sleep(2)
    result = time_stream.query(
        QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = 'guardrail_lead_time'"
    )
    assert len(result["Rows"]) == 1


@then("the max activation count is stored correctly")
def metric_stored(context):
    sleep(2)
    result = time_stream.query(
        QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = 'guardrail_max_activation'"
    )
    assert len(result["Rows"]) == 1
