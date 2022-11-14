#!/usr/bin/env python
import os
import os.path as Path
from constructs import Construct
from cdktf import (
    App,
    TerraformStack,
    TerraformAsset,
    AssetType,
)

from cdktf_cdktf_provider_aws import (
    provider,
    iam_role,
    iam_role_policy_attachment,
    lambda_function,
)

from cdktf_cdktf_provider_archive import data_archive_file

# from cdktf_cdktf_provider_aws import  AwsProvider,lambda_function, iam_role

import json


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        provider.AwsProvider(self, "AWS", profile="default")
        # create lambda helpers
        # TODO build the pip file BELOW is not working
        # build_provisioner = LocalExecProvisioner(
        #     type="localrun",
        #     command="pip install -r ${var.lambda_root}/requirements.txt -t ./all_files",
        # )
        # build_resource = TerraformResource(
        #     self,
        #     "null_resource",
        #     provisioners=[build_provisioner],
        #     terraform_resource_type="localresource",
        # )

        asset = TerraformAsset(
            self,
            "lambda-asset",
            path=Path.join(os.getcwd(), "all_files"),
            type=AssetType.ARCHIVE,
        )

        ## CREATE roles

        lambda_iam_role = iam_role.IamRole(
            self,
            "iam_role_lambda",
            name="flight-controller-aim-role",
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
            inline_policy = [
                iam_role.IamRoleInlinePolicy(
                    name = "AllowDynamoDB",
                    policy = json.dumps({
                        "Version": "2012-10-17",
                        "Statement": 
                        {
                            "Action": [
                            "dynamodb:Scan",
                            "dynamodb:Query",
                            "dynamodb:BatchGetItem",
                            "dynamodb:GetItem",
                            "dynamodb:PutItem",
                            ],
                            "Resource": "*",
                            "Effect": "Allow",
                        },
                    }) 
                )
            ]
        )

        

        policy_attachment = iam_role_policy_attachment.IamRolePolicyAttachment(
            self,
            "policy_attachment",
            policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
            role = lambda_iam_role.name,
        )

        # # Create lambda function from asset
        lambda_func = lambda_function.LambdaFunction(
            self,
            "lambda_flight_control",
            function_name="tfcdk_flight_controller_lambda",
            handler="src/entrypoints/aws_lambda.lambda_handler",
            runtime="python3.9",
            role=lambda_iam_role.arn,
            filename=asset.path,
            environment=lambda_function.LambdaFunctionEnvironment(
                variables={"DYNAMODB_TABLE_NAME": "TODO DYNAMO DB TABLE NAME"}
            ),
        )


app = App()
MyStack(app, "infra_tf_cdk")

app.synth()
