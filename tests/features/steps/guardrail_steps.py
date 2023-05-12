import json
import random
import string
from datetime import datetime
from time import sleep

import boto3
from behave import given, then, when
from google.cloud import bigquery, pubsub_v1


def guardrail_activated(context, cloud):
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    context.guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))

    if cloud == "aws":
        context.event_bridge = boto3.client("events")
        context.time_stream = boto3.client("timestream-query")

        response = context.event_bridge.put_events(
            Entries=[
                {
                    "Source": "contino.custom",
                    "DetailType": "Test guardrail activated event",
                    "Detail": json.dumps(
                        {
                            "event_type": "guardrail_activated",
                            "guardrail_id": f"{context.guardrail_id}",
                            "aggregate_id": f"{context.aggregate_id}",
                            "timestamp": f"{requested_time}",
                        }
                    ),
                    "EventBusName": "main_lambda_bus_cdktf",
                }
            ]
        )
        assert response["FailedEntryCount"] == 0

    elif cloud == "gcp":
        context.bigquery_client = bigquery.Client()
        context.publisher = pubsub_v1.PublisherClient()
        context.topic_path = context.publisher.topic_path(project="contino-squad0-fc", topic="flight-controller")

        context.publisher.publish(
            context.topic_path,
            json.dumps(
                {
                    "event_type": "guardrail_activated",
                    "guardrail_id": f"{context.guardrail_id}",
                    "aggregate_id": f"{context.aggregate_id}",
                    "timestamp": f"{requested_time}",
                }
            ).encode("utf-8"),
        ).result()


@given("a guardrail has been activated for {cloud}")
def given_guardrail_activated(context, cloud):
    guardrail_activated(context, cloud)


@when("a guardrail has been activated for {cloud}")
def when_guardrail_activated(context, cloud):
    guardrail_activated(context, cloud)


@when("a guardrail passes for {cloud}")
def guardrail_passes(context, cloud):
    sleep(5)
    requested_time = int(round(datetime.utcnow().timestamp()))

    if cloud == "aws":
        response = context.event_bridge.put_events(
            Entries=[
                {
                    "Source": "contino.custom",
                    "DetailType": "Test guardrail passed event",
                    "Detail": json.dumps(
                        {
                            "event_type": "guardrail_passed",
                            "guardrail_id": f"{context.guardrail_id}",
                            "aggregate_id": f"{context.aggregate_id}",
                            "timestamp": f"{requested_time}",
                        }
                    ),
                    "EventBusName": "main_lambda_bus_cdktf",
                }
            ]
        )
        assert response["FailedEntryCount"] == 0

    elif cloud == "gcp":
        context.publisher.publish(
            context.topic_path,
            json.dumps(
                {
                    "event_type": "guardrail_passed",
                    "guardrail_id": f"{context.guardrail_id}",
                    "aggregate_id": f"{context.aggregate_id}",
                    "timestamp": f"{requested_time}",
                }
            ).encode("utf-8"),
        ).result()


@then("the activation count is stored correctly for {cloud}")
def metric_stored(context, cloud):
    sleep(15)

    if cloud == "aws":
        result = context.time_stream.query(
            QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = 'guardrail_activation_count'"
        )
        assert len(result["Rows"]) == 1

    elif cloud == "gcp":
        query = f"""
        SELECT *
        FROM `contino-squad0-fc.metric_sourcing_table.metrics_data`
        WHERE aggregate_id = '{context.aggregate_id}' AND measure_name = 'guardrail_activation_count'
        """
        got = context.bigquery_client.query(query).result()
        rows = []
        for row in got:
            rows.append(row)
        context.bigquery_client.close()
        assert len(rows) >= 1


@then("the guardrail lead time is stored correctly for {cloud}")
def metric_stored(context, cloud):
    sleep(15)

    if cloud == "aws":
        result = context.time_stream.query(
            QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = 'guardrail_lead_time'"
        )
        assert len(result["Rows"]) == 1

    elif cloud == "gcp":
        query = f"""
        SELECT *
        FROM `contino-squad0-fc.metric_sourcing_table.metrics_data`
        WHERE aggregate_id = '{context.aggregate_id}' AND measure_name = 'guardrail_lead_time'
        """
        got = context.bigquery_client.query(query).result()
        rows = []
        for row in got:
            rows.append(row)
        context.bigquery_client.close()
        assert len(rows) >= 1


@then("the max activation count is stored correctly for {cloud}")
def metric_stored(context, cloud):
    sleep(15)

    if cloud == "aws":
        result = context.time_stream.query(
            QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = 'guardrail_max_activation'"
        )
        assert len(result["Rows"]) == 1

    elif cloud == "gcp":
        query = f"""
        SELECT *
        FROM `contino-squad0-fc.metric_sourcing_table.metrics_data`
        WHERE aggregate_id = '{context.aggregate_id}' AND measure_name = 'guardrail_max_activation'
        """
        got = context.bigquery_client.query(query).result()
        rows = []
        for row in got:
            rows.append(row)
        context.bigquery_client.close()
        assert len(rows) >= 1
