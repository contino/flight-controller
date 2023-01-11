import os
import os.path as Path
import json

from constructs import Construct

from cdktf import (
    TerraformAsset,
    AssetType,
)

from cdktf_cdktf_provider_aws import (
    iam_role,
    iam_role_policy_attachment,
    lambda_function,
    dynamodb_table
)


class LambdaWithPermissionsStack(Construct):
    def __init__(self, scope: Construct, id: str, name: str, dynamoDbTable: dynamodb_table.DynamodbTable):
        super().__init__(scope, id)

        # create lambda helpers
        # TODO build the pip file
        # currently manually building and copying the src and pip requirements manually under "all_files" folder

        asset = TerraformAsset(
            self,
            "lambda-asset",
            path=Path.join(os.getcwd(), "all_files"),
            type=AssetType.ARCHIVE,
        )

        # CREATE roles

        lambda_iam_role = iam_role.IamRole(
            self,
            "iam_role_lambda",
            name="flight-controller-iam-role",
            assume_role_policy=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": {
                        "Action": "sts:AssumeRole",
                        "Principal": {
                            "Service": "lambda.amazonaws.com",
                        },
                        "Effect": "Allow",
                        "Sid": "",
                    },
                }
            ),
            inline_policy=[
                iam_role.IamRoleInlinePolicy(
                    name="AllowDynamoDB",
                    policy=json.dumps({
                        "Version": "2012-10-17",
                        "Statement":
                        {
                            "Action": [
                                "dynamodb:Scan",
                                "dynamodb:Query",
                                "dynamodb:BatchGetItem",
                                "dynamodb:BatchWriteItem",
                                "dynamodb:GetItem",
                                "dynamodb:PutItem",
                            ],
                            "Resource": dynamoDbTable.arn,
                            "Effect": "Allow",
                        },
                    })
                )
            ]
        )

        iam_role_policy_attachment.IamRolePolicyAttachment(
            self,
            "policy_attachment",
            policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
            role=lambda_iam_role.name,
        )

        # # Create lambda function from asset
        self.lambda_func = lambda_function.LambdaFunction(
            self,
            "lambda_flight_control",
            function_name=name,
            handler="src/entrypoints/aws_lambda.lambda_handler",
            runtime="python3.9",
            role=lambda_iam_role.arn,
            filename=asset.path,
            environment=lambda_function.LambdaFunctionEnvironment(
                variables={"DYNAMO_TABLE_NAME": dynamoDbTable.name}
            ),

        )

