import json
import random
import string
from datetime import datetime
from time import sleep

import boto3
from behave import given, then, when
from google.cloud import bigquery, pubsub_v1


@given("an identity has been requested for {cloud}")
def request_identity(context, cloud):
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    context.account_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))

    if cloud == "aws":
        context.event_bridge = boto3.client("events")
        context.time_stream = boto3.client("timestream-query")

        response = context.event_bridge.put_events(
            Entries=[
                {
                    "Source": "contino.custom",
                    "DetailType": "Test identity request Event",
                    "Detail": json.dumps(
                        {
                            "event_type": "identity_requested",
                            "aggregate_id": f"{context.aggregate_id}",
                            "timestamp": f"{requested_time}",
                            "account_id": f"{context.account_id}",
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
                    "event_type": "identity_requested",
                    "aggregate_id": f"{context.aggregate_id}",
                    "timestamp": f"{requested_time}",
                    "account_id": f"{context.account_id}",
                }
            ).encode("utf-8"),
        ).result()


@when("the identity has been created for {cloud}")
def created_identity(context, cloud):
    sleep(5)
    requested_time = int(round(datetime.utcnow().timestamp()))

    if cloud == "aws":
        response = context.event_bridge.put_events(
            Entries=[
                {
                    "Source": "contino.custom",
                    "DetailType": "Test identity create Event",
                    "Detail": json.dumps(
                        {
                            "event_type": "identity_created",
                            "aggregate_id": f"{context.aggregate_id}",
                            "timestamp": f"{requested_time}",
                            "account_id": f"{context.account_id}",
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
                    "event_type": "identity_created",
                    "aggregate_id": f"{context.aggregate_id}",
                    "timestamp": f"{requested_time}",
                    "account_id": f"{context.account_id}",
                }
            ).encode("utf-8"),
        ).result()


@then("the identity created lead time is stored correctly for {cloud}")
def lead_time_stored(context, cloud):
    sleep(10)

    if cloud == "aws":
        result = context.time_stream.query(
            QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = 'identity_lead_time'"
        )
        assert len(result["Rows"]) == 1

    elif cloud == "gcp":
        query = f"""
        SELECT *
        FROM `contino-squad0-fc.metric_sourcing_table.metrics_data`
        WHERE aggregate_id = '{context.aggregate_id}' AND measure_name = 'identity_lead_time'
        """
        got = context.bigquery_client.query(query).result()
        rows = []
        for row in got:
            rows.append(row)
        context.bigquery_client.close()
        assert len(rows) >= 1
