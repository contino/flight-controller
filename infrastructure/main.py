#!/usr/bin/env python

import os

import boto3
from cdktf import App, S3Backend, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from constructs import Construct
from dynamo_db_component import DynamoDBcomponent
from event_bridge_component import EventBridgeComponent
from grafana_dashboard_component import GrafanaDashboardComponent
from imports.grafana.provider import GrafanaProvider
from lambda_with_permissions_component import LambdaWithPermissionsComponent
from managed_grafana_component import GrafanaWithPermissionsComponent
from timestream_database_component import TimeStreamDBcomponent


class MyStack(TerraformStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
    ):
        super().__init__(scope, id)

        AwsProvider(self, "AWS")

        self.dynamotable_name = "event_sourcing_table"
        self.lambda_name = "producer_lambda_function_cdktf"
        self.event_bridge_name = "main_lambda_bus_cdktf"
        self.timestream_db_name = "core_timestream_db"
        self.grafana_workspace_name = "grafana_dashboard"

        # create dynamodb
        dynamoDBcomponent = DynamoDBcomponent(
            self, "event_table", self.dynamotable_name
        )
        # create timestream data base
        timeStreamComponent = TimeStreamDBcomponent(
            self, "time_stream", self.timestream_db_name
        )
        # create lambda function
        lambdaComponent = LambdaWithPermissionsComponent(
            self,
            "lambda_function",
            self.lambda_name,
            dynamoDBcomponent.table,
            timeStreamComponent.timestream_table,
        )
        # create event bridge
        eventBridgeComponent = EventBridgeComponent(
            self, "event_bridge", self.event_bridge_name, lambdaComponent.lambda_func
        )

        # Create Grafana workspace
        grafanaWorkspace = GrafanaWithPermissionsComponent(
            self,
            "grafana_workspace",
            self.grafana_workspace_name,
        )

        self.grafana_workspace_id = grafanaWorkspace.grafana_workspace.id


class Grafana(TerraformStack):
    def __init__(self, scope: Construct, id: str, workspace_id: str):
        super().__init__(scope, id)
        GrafanaProvider(
            self,
            "Grafana",
            auth=os.environ["GRAFANA_API_KEY"],
            url="https://"
            + workspace_id
            + ".grafana-workspace.ap-southeast-2.amazonaws.com/",
        )

        # Create Grafana dashboard
        GrafanaDashboardComponent(
            self,
            "grafana_dashboard",
        )


app = App()
stack = MyStack(
    app,
    "infra_tf_cdk",
)
grafana_stack = Grafana(app, "grafana", stack.grafana_workspace_id)

account_id = boto3.client("sts").get_caller_identity()["Account"]

S3Backend(
    stack,
    bucket=f"{account_id}-apac-flight-controller-aws",
    key="infra_tf_cdk/terraform.tfstate",
    dynamodb_table=f"{account_id}-apac-flight-controller-aws",
)

S3Backend(
    grafana_stack,
    bucket=f"{account_id}-apac-flight-controller-aws",
    key="grafana/terraform.tfstate",
    dynamodb_table=f"{account_id}-apac-flight-controller-aws",
)

app.synth()
