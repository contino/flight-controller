from typing import List, Tuple
from enum import Enum

from aws_cdk import aws_lambda, aws_dynamodb
from constructs import Construct

PermissionType = Enum("PermissionType", ["Read", "Write", "ReadWrite"])
LambdaPermissions = Tuple[aws_lambda.IFunction, PermissionType]


class DynamoWithPermission(Construct):
    """Class that creates a dynamo table and assign permissions to access to lambda functions.
    It automatically adds the table name to Lambda env variable DYNAMO_TABLE_NAME
    """

    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        give_permission_to: List[LambdaPermissions] = None,
        **kwargs
    ):
        super().__init__(scope, f"{id}-construct", **kwargs)
        self.partition_key = "aggregateId"
        self.sort_key = "eventId"

        # create dynamo table
        demo_table = aws_dynamodb.Table(
            self,
            id,
            partition_key=aws_dynamodb.Attribute(
                name=self.partition_key, type=aws_dynamodb.AttributeType.STRING
            ),
            sort_key=aws_dynamodb.Attribute(
                name=self.sort_key, type=aws_dynamodb.AttributeType.STRING
            ),
        )

        for constructor, permType in give_permission_to:
            constructor.add_environment("DYNAMO_TABLE_NAME", demo_table.table_name)
            if permType == PermissionType.Read:
                demo_table.grant_read_data(constructor)
            elif permType == PermissionType.Write:
                demo_table.grant_write_data(constructor)
            elif permType == PermissionType.ReadWrite:
                demo_table.grant_read_write_data(constructor)
