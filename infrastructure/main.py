#!/usr/bin/env python

from constructs import Construct
from cdktf import App, TerraformStack, S3Backend, TerraformOutput

from cdktf_cdktf_provider_aws.provider import AwsProvider
from imports.grafana.provider import GrafanaProvider

from dynamo_db_component import DynamoDBcomponent
from lambda_with_permissions_component import LambdaWithPermissionsComponent
from event_bridge_component import EventBridgeComponent
from timestream_database_component import TimeStreamDBcomponent
from managed_grafana_component import GrafanaWithPermissionsComponent
from grafana_dashboard_component import GrafanaDashboardComponent
from managed_grafana_component import grafana_workspace_api_key


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
        # create lambda function
        lambdaComponent = LambdaWithPermissionsComponent(
            self, "lambda_function", self.lambda_name, dynamoDBcomponent.table
        )
        # create event bridge
        eventBridgeComponent = EventBridgeComponent(
            self, "event_bridge", self.event_bridge_name, lambdaComponent.lambda_func
        )
        # create timestream data base
        timeStreamComponent = TimeStreamDBcomponent(
            self, "time_stream", self.timestream_db_name
        )
        # Create Grafana workspace
        grafanaWorkspace = GrafanaWithPermissionsComponent(
            self, "grafana_workspace", self.grafana_workspace_name
        )

        GrafanaProvider(
            self,
            "Grafana",
            auth=grafanaWorkspace.api_key,
            # auth="eyJrIjoiU3oxcThrMGJaWktRWTBpeGVtcjc4NlRGOGJidnA1Tk8iLCJuIjoiZmxpZ2h0LWNvbnRyb2xsZXItZ3JhZmFuYS1hcGkta2V5IiwiaWQiOjF9",
            url="https://g-2e637a6ddc.grafana-workspace.ap-southeast-2.amazonaws.com/",
        )

        # Create Grafana dashboard
        grafanaDashboard = GrafanaDashboardComponent(
            self, "grafana_dashboard", 
        )


app = App()
stack = MyStack(app, "infra_tf_cdk",)

S3Backend(
    stack,
    bucket="099267815798-apac-flight-controller-aws",
    key="infra_tf_cdk/terraform.tfstate",
    dynamodb_table="099267815798-apac-flight-controller-aws",
)

app.synth()
