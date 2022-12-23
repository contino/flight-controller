#!/usr/bin/env python

from constructs import Construct
from cdktf import App, TerraformStack, S3Backend

from cdktf_cdktf_provider_aws import provider

from dynamo_db_component import DynamoDBcomponent
from lambda_with_permissions_component import LambdaWithPermissionsStack
from event_bridge_component import EventBridgeComponent
from timestream_database_component import TimeStreamDBcomponent


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        provider.AwsProvider(self, "AWS")

        self.dynamotable_name = (
            "event_sourcing_table"  # changed db from "event_sourcing_table_cdktf"
        )
        self.lambda_name = "producer_lambda_function_cdktf"
        self.event_bridge_name = "main_lambda_bus_cdktf"
        self.timestream_db_name = "core_timestream_db"

        # create dynamodb
        dynamoDBcomponent = DynamoDBcomponent(
            self, "event_table", self.dynamotable_name
        )
        # create timestream data base
        timeStreamComponent = TimeStreamDBcomponent(
            self, "time_stream", self.timestream_db_name
        )
        # create lambda function
        lambdaComponent = LambdaWithPermissionsStack(
            self,
            "lambda_function",
            self.lambda_name,
            dynamoDBcomponent.table,
            timeStreamComponent.table,
        )
        # create event bridge
        eventBridgeComponent = EventBridgeComponent(
            self, "event_bridge", self.event_bridge_name, lambdaComponent.lambda_func
        )


app = App()
stack = MyStack(app, "infra_tf_cdk")

S3Backend(
    stack,
    bucket="099267815798-apac-flight-controller-aws",
    key="infra_tf_cdk/terraform.tfstate",
    dynamodb_table="099267815798-apac-flight-controller-aws",
)

app.synth()
