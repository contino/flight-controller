from cdktf_cdktf_provider_aws import (lambda_function, secretsmanager_secret,
                                      secretsmanager_secret_rotation)
from constructs import Construct


class RotationComponent(Construct):
    def __init__(self, scope: Construct, id: str, secretsManager: secretsmanager_secret.SecretsmanagerSecret, lambda_func: lambda_function.LambdaFunction):
        super().__init__(scope, id)


        # Secret rotation every 29 days
        self.rotate_secret = (
            secretsmanager_secret_rotation.SecretsmanagerSecretRotation(
            self,
            "secret_rotation",
            secret_id=secretsManager.id,
            rotation_lambda_arn=lambda_func.arn,
            rotation_rules= {"automatically_after_days": 29},
            )
        )

