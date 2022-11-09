from time import sleep
from behave import given, when, then
from datetime import datetime
import json

import boto3

publisher = boto3.client("events")


@given("a project has been requested")
def request_project(context):
    context.correlation_id = "behaveTest"
    context.requested_time = int(round(datetime.utcnow().timestamp()))
    publisher.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test project request Event",
                f"Detail": '{"event_type": "ProjectRequested","correlation_id":{context.correlation_id},"time":{context.requested_time}}',
                "EventBusName": "MainEventBus",
            }
        ]
    )


@given("a project has been assigned")
def assing_project(context):
    context.correlation_id = "behaveTest"
    publisher.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test project assign Event",
                f"Detail": '{"event_type": "ProjectRequested","correlation_id":{context.correlation_id},"time":{context.requested_time}}',
                "EventBusName": "MainEventBus",
            }
        ]
    )


@when("the project has been created")
def assing_project(context):
    context.correlation_id = "behaveTest"
    publisher.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test project assign Event",
                f"Detail": '{"event_type": "ProjectCreated","correlation_id":{context.correlation_id},"time":{context.requested_time}}',
                "EventBusName": "MainEventBus",
            }
        ]
    )


@then("the lead time is stored correctly")
def lead_time_stored(context):
    sleep(1)
    # TODO get metric results
    assert True
