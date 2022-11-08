from time import sleep
from behave import given, when, then
import random
import string
from datetime import datetime
import json

from google.cloud import pubsub_v1, bigquery

publisher = pubsub_v1.PublisherClient()
bigquery_client = bigquery.Client()

topic_path = publisher.topic_path(project="contino-squad0-fc", topic="topic")


@given("a project has been requested")
def request_project(context):
    context.correlation_id = "".join(random.choices(string.ascii_letters, k=12))
    context.project_number = str(random.randint(100000000000, 999999999999))
    context.requested_time = datetime.utcnow().timestamp()
    publisher.publish(
        topic_path,
        json.dumps(
            {
                "event_type": "ProjectRequested",
                "requested_time": context.requested_time,
                "correlation_id": context.correlation_id,
                "project_number": context.project_number,
            }
        ).encode("utf-8"),
    ).result()


@when("the project has been created")
def create_project(context):
    sleep(5)
    context.created_time = datetime.utcnow().timestamp()
    publisher.publish(
        topic_path,
        json.dumps(
            {
                "event_type": "ProjectCreated",
                "created_time": context.created_time,
                "correlation_id": context.correlation_id,
                "project_number": context.project_number,
            }
        ).encode("utf-8"),
    ).result()


@then("the lead time is stored correctly")
def lead_time_stored(context):
    sleep(10)
    query = f"""
    SELECT lead_time
    FROM `flight_controller.project_lead_times`
    WHERE correlation_id = '{context.correlation_id}'
    """
    print(query)
    got = bigquery_client.query(query).result()

    rows = []
    for row in got:
        rows.append(row)

    assert len(rows) >= 1

    assert rows[0][0] == context.created_time - context.requested_time
