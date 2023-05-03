import json
import random
import string
from datetime import datetime
from time import sleep

import boto3
from behave import then, when
from google.cloud import bigquery, pubsub_v1


@when("patch run summary is complete for {cloud}")
def received_summary(context, cloud):
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))

    if cloud == "aws":
        context.event_bridge = boto3.client("events")
        context.time_stream = boto3.client("timestream-query")
        response = context.event_bridge.put_events(
            Entries=[
                {
                    "Source": "contino.custom",
                    "DetailType": "Test Patch Summary Event",
                    "Detail": json.dumps(
                        {
                            "event_type": "patch_run_summary",
                            "aggregate_id": f"{context.aggregate_id}",
                            "timestamp": f"{requested_time}",
                            "failed_instances": "i-adslkjfds,i-89dsfkjdkfj",
                            "successful_instances": "i-peoritdsfl",
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
                    "event_type": "patch_run_summary",
                    "aggregate_id": f"{context.aggregate_id}",
                    "timestamp": f"{requested_time}",
                    "failed_instances": "i-adslkjfds,i-89dsfkjdkfj",
                    "successful_instances": "i-peoritdsfl",
                }
            ).encode("utf-8"),
        ).result()


@then("the compliance percentage is stored correctly for {cloud}")
def compliance_percentage_stored(context, cloud):
    sleep(10)

    if cloud == "aws":
        result = context.time_stream.query(
            QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = 'patch_compliance_percentage'"
        )
        assert len(result["Rows"]) == 1

    elif cloud == "gcp":
        query = f"""
        SELECT *
        FROM `contino-squad0-fc.metric_sourcing_table.metrics_data`
        WHERE aggregate_id = '{context.aggregate_id}' AND measure_name = 'patch_compliance_percentage'
        """
        got = context.bigquery_client.query(query).result()
        rows = []
        for row in got:
            rows.append(row)
        context.bigquery_client.close()
        assert len(rows) >= 1
