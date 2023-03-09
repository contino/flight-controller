import json
from cdktf_cdktf_provider_aws import (
    grafana_workspace,
    grafana_workspace_api_key,
    iam_role,
    iam_role_policy_attachment,
    secretsmanager_secret,
    secretsmanager_secret_version,
)
from constructs import Construct


class GrafanaWithPermissionsComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        name: str,
    ):
        super().__init__(scope, id)

        # CREATE roles
        grafana_iam_role = iam_role.IamRole(
            self,
            "iam_role_grafana",
            name="flight-controller-grafana-role",
            assume_role_policy=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": {
                        "Action": "sts:AssumeRole",
                        "Principal": {
                            "Service": "grafana.amazonaws.com",
                        },
                        "Effect": "Allow",
                        "Sid": "",
                    },
                }
            ),
            inline_policy=[
                iam_role.IamRoleInlinePolicy(
                    name="AllowTimestreamDB",
                    policy=json.dumps(
                        {
                            "Version": "2012-10-17",
                            "Statement": {
                                "Action": [
                                    "timestream:CancelQuery",
                                    "timestream:DescribeDatabase",
                                    "timestream:DescribeEndpoints",
                                    "timestream:DescribeTable",
                                    "timestream:ListDatabases",
                                    "timestream:ListMeasures",
                                    "timestream:ListTables",
                                    "timestream:ListTagsForResource",
                                    "timestream:Select",
                                    "timestream:SelectValues",
                                    "timestream:DescribeScheduledQuery",
                                    "timestream:ListScheduledQueries",
                                ],
                                "Resource": "*",
                                "Effect": "Allow",
                            },
                        }
                    ),
                )
            ],
        )

        iam_role_policy_attachment.IamRolePolicyAttachment(
            self,
            "policy_attachment",
            policy_arn="arn:aws:iam::aws:policy/AmazonTimestreamReadOnlyAccess",
            role=grafana_iam_role.name,
        )

        # Create a Grafana workspace
        self.grafana_workspace = grafana_workspace.GrafanaWorkspace(
            self,
            "grafana_flight_control",
            name=name,
            account_access_type="CURRENT_ACCOUNT",
            authentication_providers=["AWS_SSO"],
            permission_type="SERVICE_MANAGED",
            role_arn=grafana_iam_role.arn,
            data_sources=["TIMESTREAM"],
        )

        # Create an API key for the admin role
        self.grafana_workspace_api_key = (
            grafana_workspace_api_key.GrafanaWorkspaceApiKey(
                self,
                "grafana_workspace_api_key",
                key_name="flight_controller_api_key",
                key_role="ADMIN",
                workspace_id=self.grafana_workspace.id,
                seconds_to_live=2525000,
            )
        )

        # Create secret in AWS Secrets Manager
        self.grafana_key = secretsmanager_secret.SecretsmanagerSecret(
            self,
            "grafana_key",
            name="flight-controller-grafana-api-key",
        )

        # Store secret in above created resource
        self.grafana_key_value = (
            secretsmanager_secret_version.SecretsmanagerSecretVersion(
                self,
                "grafana_key_value",
                secret_id=self.grafana_key.id,
                secret_string=self.grafana_workspace_api_key.key,
            )
        )

        # Store workspace ID in AWS Secrets Manager
        self.workspace_id = secretsmanager_secret.SecretsmanagerSecret(
            self,
            "workspace_id",
            name="flight-controller-grafana-workspace-id",
        )

        # Store workspace ID in above created resource
        self.workspace_id_value = (
            secretsmanager_secret_version.SecretsmanagerSecretVersion(
                self,
                "workspace_id_value",
                secret_id=self.workspace_id.id,
                secret_string=self.grafana_workspace.id,
            )
        )
