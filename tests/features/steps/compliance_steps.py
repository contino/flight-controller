import json
import random
import string
from datetime import datetime
from time import sleep

import boto3
from behave import given, then, when
from google.cloud import bigquery, pubsub_v1


@given("a resource has been found non compliant for {cloud}")
def found_non_compliant(context, cloud):
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))

    if cloud == "aws":
        context.event_bridge = boto3.client("events")
        context.time_stream = boto3.client("timestream-query")

        response = context.event_bridge.put_events(
            Entries=[
                {
                    "Source": "contino.custom",
                    "DetailType": "Test project request Event",
                    "Detail": json.dumps(
                        {
                            "event_type": "resource_found_non_compliant",
                            "container_id": "123456789012",
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
                    "event_type": "resource_found_non_compliant",
                    "container_id": "123456789012",
                    "aggregate_id": f"{context.aggregate_id}",
                    "timestamp": f"{requested_time}",
                }
            ).encode("utf-8"),
        ).result()

@when("the resource is found compliant for {cloud}")
def found_compliant(context, cloud):
    sleep(5)
    requested_time = int(round(datetime.utcnow().timestamp()))

    if cloud == "aws":
        response = context.event_bridge.put_events(
            Entries=[
                {
                    "Source": "contino.custom",
                    "DetailType": "Test project create Event",
                    "Detail": json.dumps(
                        {
                            "event_type": "resource_found_compliant",
                            "container_id": "123456789012",
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
                    "event_type": "resource_found_compliant",
                    "container_id": "123456789012",
                    "aggregate_id": f"{context.aggregate_id}",
                    "timestamp": f"{requested_time}",
                }
            ).encode("utf-8"),
        ).result()


@then("the compliance lead time is stored correctly for {cloud}")
def lead_time_stored(context, cloud):
    sleep(10)

    if cloud == "aws":
        result = context.time_stream.query(
            QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = 'resource_compliance_lead_time'"
        )
        assert len(result["Rows"]) == 1

    elif cloud == "gcp":
        query = f"""
        SELECT *
        FROM `contino-squad0-fc.metric_sourcing_table.metrics_data`
        WHERE aggregate_id = '{context.aggregate_id}' AND measure_name = 'resource_compliance_lead_time'
        """
        got = context.bigquery_client.query(query).result()
        rows = []
        for row in got:
            rows.append(row)
        context.bigquery_client.close()
        assert len(rows) >= 1
