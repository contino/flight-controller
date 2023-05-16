#!/usr/bin/env python

import json

import boto3
from cdktf import App, S3Backend, TerraformStack
from cdktf_cdktf_provider_aws import data_aws_secretsmanager_secret_version, data_aws_ssm_parameter
from cdktf_cdktf_provider_aws.provider import AwsProvider
from constructs import Construct
from dynamo_db_component import DynamoDBcomponent
from event_bridge_component import EventBridgeComponent
from grafana_dashboard_component import GrafanaDashboardComponent
from grafana_lambda_with_permissions_component import GrafanaLambdaComponent
from imports.grafana.provider import GrafanaProvider
from lambda_rotation_component import RotationComponent
from lambda_with_permissions_component import LambdaWithPermissionsComponent
from managed_grafana_component import GrafanaWithPermissionsComponent
from timestream_database_component import TimeStreamDBcomponent


class AwsCore(TerraformStack):
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
        self.grafana_lambda_name = "grafana_api_key_rotator"

        # create dynamodb
        dynamodb_component = DynamoDBcomponent(
            self, "event_table", self.dynamotable_name
        )
        # create timestream data base
        timestream_component = TimeStreamDBcomponent(
            self, "time_stream", self.timestream_db_name
        )
        # create lambda function
        lambda_component = LambdaWithPermissionsComponent(
            self,
            "lambda_function",
            self.lambda_name,
            dynamodb_component.table,
            timestream_component.timestream_table,
            dynamodb_component.key.arn
        )
        # create event bridge
        eventbridge_component = EventBridgeComponent(
            self, "event_bridge", self.event_bridge_name, lambda_component.lambda_func
        )

        # Create Grafana workspace
        grafana_workspace = GrafanaWithPermissionsComponent(
            self,
            "grafana_workspace",
            self.grafana_workspace_name,
        )

        # Create lambda function to rotate Grafana key 
        grafana_lambda_component = GrafanaLambdaComponent(
            self, "grafana_function", self.grafana_lambda_name, grafana_workspace.grafana_workspace, grafana_workspace.api_kms_key.arn, grafana_workspace.workspace_id_kms_key.arn
        )

        # Create rotation rules to trigger every 29 days
        rotation_component = RotationComponent(
            self, "rotation", grafana_workspace.grafana_key ,grafana_lambda_component.lambda_func
        )

class AwsGrafana(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        
        AwsProvider(self, "AWS")
        
        api_key = data_aws_secretsmanager_secret_version.DataAwsSecretsmanagerSecretVersion(
            self,
            "api_key",
            secret_id="flight-controller/grafana-api-key",               # Secret name stored in AWS Secrets Manager
        )

        workspace_id = data_aws_ssm_parameter.DataAwsSsmParameter(
            self,
            "workspace_id",
            name="/flight-controller/grafana-workspace-id"
        )
        
        GrafanaProvider(
            self,
            "Grafana",
            auth=api_key.secret_string,
            url="https://"
            + workspace_id.value
            + ".grafana-workspace.ap-southeast-2.amazonaws.com/",
        )

        # Load the dashboard configuration from a JSON file
        with open("dashboard.json", "r") as file:
            data = json.load(file)

        # Create Grafana dashboard
        GrafanaDashboardComponent(
            self,
            "grafana_dashboard",
            data
        )


app = App()

core_stack = AwsCore(app, "aws_core")

grafana_dashboard_stack = AwsGrafana(app, "aws_grafana_dashboard")

account_id = boto3.client("sts").get_caller_identity()["Account"]

S3Backend(
    core_stack,
    bucket=f"{account_id}-apac-flight-controller-aws",
    key="infra_tf_cdk/terraform.tfstate",
    dynamodb_table=f"{account_id}-apac-flight-controller-aws",
)

S3Backend(
    grafana_dashboard_stack,
    bucket=f"{account_id}-apac-flight-controller-aws",
    key="grafana/terraform.tfstate",
    dynamodb_table=f"{account_id}-apac-flight-controller-aws",
)

app.synth()