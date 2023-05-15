from constructs import Construct

from cdktf_cdktf_provider_aws import (
    dynamodb_table,
    kms_key
)


class DynamoDBcomponent(Construct):
    def __init__(self, scope: Construct, id: str, name: str):
        super().__init__(scope, id)
        self.partition_key = "aggregate_id"
        self.sort_key = "event_id"

        # KMS Key
        self.key = kms_key.KmsKey(
            self,
            "flight_controller_core_dynamodb_key",
            description="Flight Controller Core DynamoDB KMS Key",
            enable_key_rotation=True,
            lifecycle={
                "prevent_destroy": True
            }
        )

        # create dynamoDB table
        self.table = dynamodb_table.DynamodbTable(
            self,
            "table",
            name=name,
            billing_mode="PAY_PER_REQUEST",
            point_in_time_recovery={
                "enabled": True
            },
            server_side_encryption={
                "enabled": True,
                "kms_key_arn": self.key.arn
            },
            hash_key=self.partition_key,
            range_key=self.sort_key,
            attribute=[
                dynamodb_table.DynamodbTableAttribute(
                    name=self.partition_key, type="S"
                ),
                dynamodb_table.DynamodbTableAttribute(name=self.sort_key, type="S"),
            ],
        )
