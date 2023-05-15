import os
import os.path as Path
import json
from dirhash import dirhash

from constructs import Construct

from cdktf import (
    TerraformAsset,
    AssetType,
)

from cdktf_cdktf_provider_aws import (
    iam_role,
    iam_role_policy_attachment,
    lambda_function,
    grafana_workspace,
    lambda_permission,
    kms_key
)


class GrafanaLambdaComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        name: str,
        grafanaWorkspace: grafana_workspace.GrafanaWorkspace,
        api_kms_key: str,
        workspace_id_kms_key: str
    ):
        super().__init__(scope, id)

        asset = TerraformAsset(
            self,
            "lambda-asset",
            path=Path.join(os.getcwd(), "api_key_rotation"),
            type=AssetType.ARCHIVE,
            asset_hash=dirhash(Path.join(os.getcwd(), "api_key_rotation"), "md5"),
        )

        # KMS Key

        key = kms_key.KmsKey(
            self,
            "flight_controller_grafana_rotation_lambda_key",
            description="Flight Controller Grafana Rotation Lambda KMS Key",
            enable_key_rotation=True,
            lifecycle={
                "prevent_destroy": True
            }
        )

        # CREATE roles

        lambda_iam_role = iam_role.IamRole(
            self,
            "iam_role_lambda",
            name="grafana-lambda-iam-role",
            assume_role_policy=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "",
                            "Effect": "Allow",
                            "Principal": {"Service": "lambda.amazonaws.com"},
                            "Action": "sts:AssumeRole",
                        },
                    ],
                },
            ),
            inline_policy=[
                iam_role.IamRoleInlinePolicy(
                    name="AllowGrafanaActions",
                    policy=json.dumps(
                        {
                            "Version": "2012-10-17",
                            "Statement": {
                                "Action": [
                                    "grafana:DeleteWorkspaceApiKey",
                                    "grafana:CreateWorkspaceApiKey",
                                ],
                                "Resource": grafanaWorkspace.arn,
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
                                        "kms:ReEncrypt*",
                                        "kms:GenerateDataKey*"
                                    ],
                                    "Resource": [
                                        api_kms_key,
                                        workspace_id_kms_key
                                    ],
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
            "AWSLambdaBasicExecutionRole",
            policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
            role=lambda_iam_role.name,
        )

        iam_role_policy_attachment.IamRolePolicyAttachment(
            self,
            "SecretsManagerReadWrite",
            policy_arn="arn:aws:iam::aws:policy/SecretsManagerReadWrite",
            role=lambda_iam_role.name,
        )

        # Create lambda function from asset
        self.lambda_func = lambda_function.LambdaFunction(
            self,
            "lambda_grafana",
            function_name=name,
            handler="main.lambda_handler",
            runtime="python3.9",
            kms_key_arn=key.arn,
            role=lambda_iam_role.arn,
            filename=asset.path,
        )

        # Create rotation permission
        self.lambda_rotate = lambda_permission.LambdaPermission(
            self,
            "lambda_permission",
            function_name=self.lambda_func.function_name,
            action="lambda:InvokeFunction",
            principal="secretsmanager.amazonaws.com",
            statement_id="AllowRotation",
        )
