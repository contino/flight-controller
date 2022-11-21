# AWS python CDK https://docs.aws.amazon.com/cdk/api/v2/python/index.html

from aws_cdk import (
    Stack,
)

from infra_aws_cdk.dynamo_with_lambda_permission import (
    DynamoWithPermission,
    PermissionType,
)

from infra_aws_cdk.python_lambda_with_requirements import LambdaPtyhonWithRequirements
from infra_aws_cdk.create_event_bridge import EventBridgeWithLambdaRule
from infra_aws_cdk.timestream_with_lambda_access import TimeStreamWithLambdaAccess

from constructs import Construct


class InfraAwsCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.dynamotable_name = "event_sourcing_table"
        self.lambda_name = "producer_lambda_function"
        self.event_bridge_name = "MainEventBus"
        self.timestream_db_name = "core_timestream_db"

        # create producer lambda function
        producer_lambda = LambdaPtyhonWithRequirements(
            self, self.lambda_name
        ).get_lambda()

        # Create dynameDb table and grant permission to lambda to write to demo table
        DynamoWithPermission(
            self,
            self.dynamotable_name,
            give_permission_to=[(producer_lambda, PermissionType.ReadWrite)],
        )

        ## Create event bridge
        EventBridgeWithLambdaRule(
            self, self.event_bridge_name, send_event_to=producer_lambda
        )

        ## create time stream
        TimeStreamWithLambdaAccess(
            self, self.timestream_db_name, give_permission_to=producer_lambda
        )
