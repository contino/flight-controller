#!/usr/bin/env python
import uuid
from constructs import Construct
from cdktf import (
    App,
    TerraformStack,
    TerraformVariable,
    TerraformResource,
    LocalExecProvisioner,
)
from cdktf_cdktf_provider_aws import (
    provider,
    iam_role,
    iam_policy,
    iam_role_policy_attachment,
    lambda_function,
)

from cdktf_cdktf_provider_archive import data_archive_file

# from cdktf_cdktf_provider_aws import  AwsProvider,lambda_function, iam_role

import json


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        provider.AwsProvider(self, "AWS", region="app-southest-2")
        # create lambda helpers
        lambdaVariable = TerraformVariable(
            self,
            "lambda_root",
            type="string",
            default="../code",
            description="Root folder of lambda code.",
        )
        build_provisioner = LocalExecProvisioner(
            type="localrun",
            command="pip install -r ${var.lambda_root}/requirements.txt -t ./all_files",
        )
        build_resource = TerraformResource(
            self,
            "null_resource",
            provisioners=[build_provisioner],
            terraform_resource_type="localresource",
        )

        data_archive = data_archive_file.DataArchiveFile(
            self,
            "id_data_archive",
            type="zip",
            source_dir="${path.module}/all_files",
            output_path="${path.module}/output.zip",
        )

        ## CREATE roles

        lambda_iam_role = iam_role.IamRole(
            self,
            "iam_role_lambda",
            name="flight_controller_aim_role",
            assume_role_policy='{ "Version": "2012-10-17","Statement": [{"Action": "sts:AssumeRole","Principal": {"Service": "lambda.amazonaws.com"},"Effect": "Allow","Sid": ""}]}',
        )

        lambda_iam_policy = iam_policy.IamPolicy(
            self,
            "iam_polic_lambda",
            policy='{"Version": "2012-10-17","Statement": [{"Action": ["logs:CreateLogGroup","logs:CreateLogStream","logs:PutLogEvents"],"Resource": "arn:aws:logs:*:*:*","Effect": "Allow"}]}',
        )

        policy_attachment = iam_role_policy_attachment.IamRolePolicyAttachment(
            self,
            "policy_attachment",
            role=lambda_iam_role.arn,
            policy_arn=lambda_iam_policy.arn,
        )

        # create lambda
        lambda_func = lambda_function.LambdaFunction(
            self,
            "lambda_flight_control",
            filename=data_archive.output_path,
            function_name="tfcdk_flight_controller_lambda",
            role=lambda_iam_role.arn,
            runtime="python3.9",
            handler="src/entrypoints/aws_lambda.lambda_handler",
            depends_on=[policy_attachment, data_archive],
        )


app = App()
MyStack(app, "infra_tf_cdk")

app.synth()
