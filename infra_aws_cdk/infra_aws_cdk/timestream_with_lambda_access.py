from aws_cdk import (
    aws_lambda,
    aws_events,
    aws_events_targets,
    aws_iam,
    aws_timestream as timestream,
    CfnTag,
    Stack,
)

from constructs import Construct


class TimeStreamWithLambdaAccess(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        give_permission_to: aws_lambda.IFunction,
        **kwargs,
    ):
        super().__init__(scope, f"{id}-construct", **kwargs)
        self.table_name = "metrics_table"

        cfn_database = timestream.CfnDatabase(
            self,
            id,
            database_name=id,
            tags=[CfnTag(key="DBtype", value="Core time stream DB")],
        )

        cfn_table = timestream.CfnTable(
            self,
            self.table_name,
            database_name=cfn_database.database_name,
            # the properties below are optional
            table_name=self.table_name,
            retention_properties={  # in-memory tier of a week and afterwards data will be moved to read-optimised tier for two years.
                "memoryStoreRetentionPeriodInHours": 24 * 7,
                "magneticStoreRetentionPeriodInDays": 365 * 2,
            },
            tags=[CfnTag(key="tableType", value="Core time stream table")],
        )
        cfn_table.node.add_dependency(cfn_database)

        give_permission_to.add_to_role_policy(
            aws_iam.PolicyStatement(resources=["*"], actions=["timestream:*"])
        )
