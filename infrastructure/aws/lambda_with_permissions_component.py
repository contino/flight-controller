import json
import os
import os.path as Path

from cdktf import AssetType, TerraformAsset
from cdktf_cdktf_provider_aws import (dynamodb_table, iam_role,
                                      iam_role_policy_attachment, kms_key,
                                      lambda_function, timestreamwrite_table)
from constructs import Construct
from dirhash import dirhash


class LambdaWithPermissionsComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        name: str,
        dynamo_db_table: dynamodb_table.DynamodbTable,
        timestream_table: timestreamwrite_table.TimestreamwriteTable,
        dynamo_db_key: str
    ):
        super().__init__(scope, id)

        # create lambda helpers
        # TODO build the pip file
        # currently manually building and copying the src and pip requirements manually under "controller_core" folder

        asset = TerraformAsset(
            self,
            "lambda-asset",
            path=Path.join(os.getcwd(), "controller_core"),
            type=AssetType.ARCHIVE,
            asset_hash=dirhash(Path.join(os.getcwd(), "controller_core"), "md5"),
        )

        # KMS Key

        key = kms_key.KmsKey(
            self,
            "flight_controller_core_lambda_key",
            description="Flight Controller Core Lambda KMS Key",
            enable_key_rotation=True,
            lifecycle={
                "prevent_destroy": True
            }
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
                    policy=json.dumps(
                        {
                            "Version": "2012-10-17",
                            "Statement": {
                                "Action": [
                                    "dynamodb:Scan",
                                    "dynamodb:Query",
                                    "dynamodb:BatchGetItem",
                                    "dynamodb:BatchWriteItem",
                                    "dynamodb:GetItem",
                                    "dynamodb:PutItem",
                                ],
                                "Resource": dynamo_db_table.arn,
                                "Effect": "Allow",
                            },
                        }
                    ),
                ),
                iam_role.IamRoleInlinePolicy(
                    name="AllowTimeStream",
                    policy=json.dumps(
                        {
                            "Version": "2012-10-17",
                            "Statement": {
                                "Action": [
                                    "timestream:DescribeEndpoints",
                                    "timestream:WriteRecords",
                                ],
                                "Resource": "*",
                                "Effect": "Allow",
                            },
                        }
                    ),
                ),
                iam_role.IamRoleInlinePolicy(
                    name="AllowKMSDecrypt",
                    policy=json.dumps(
                        {
                            "Version": "2012-10-17",
                            "Statement": [
                                {
                                    "Action": [
                                        "kms:Decrypt",
                                        "kms:Encrypt",
                                        "kms:CreateGrant",
                                    ],
                                    "Resource": dynamo_db_key,
                                    "Effect": "Allow",
                                },
                                {
                                    "Action": "kms:ListAliases",
                                    "Resource": "*",
                                    "Effect": "Allow",
                                }
                            ]
                        }
                    ),
                )
            ],
        )

        iam_role_policy_attachment.IamRolePolicyAttachment(
            self,
            "policy_attachment",
            policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
            role=lambda_iam_role.name,
        )

        # Create lambda function from asset
        self.lambda_func = lambda_function.LambdaFunction(
            self,
            "lambda_flight_control",
            function_name=name,
            handler="src/entrypoints/aws_lambda.lambda_handler",
            runtime="python3.9",
            kms_key_arn=key.arn,
            role=lambda_iam_role.arn,
            filename=asset.path,
            environment=lambda_function.LambdaFunctionEnvironment(
                variables={
                    "DYNAMO_TABLE_NAME": dynamo_db_table.name,
                    "TIMESTREAM_DATABASE_NAME": timestream_table.database_name,
                    "TIMESTREAM_TABLE_NAME": timestream_table.table_name,
                }
            ),
        )
