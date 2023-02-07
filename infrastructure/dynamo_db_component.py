from constructs import Construct

from cdktf_cdktf_provider_aws import dynamodb_table


class DynamoDBcomponent(Construct):
    def __init__(self, scope: Construct, id: str, name: str):
        super().__init__(scope, id)
        self.partition_key = "aggregateId"
        self.sort_key = "eventId"

        # create dynamoDB table
        self.table = dynamodb_table.DynamodbTable(
            self,
            "table",
            name=name,
            billing_mode="PAY_PER_REQUEST",
            hash_key=self.partition_key,
            range_key=self.sort_key,
            attribute=[
                dynamodb_table.DynamodbTableAttribute(
                    name=self.partition_key, type="S"
                ),
                dynamodb_table.DynamodbTableAttribute(name=self.sort_key, type="S"),
            ],
        )
