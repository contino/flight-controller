# AWS python CDK https://docs.aws.amazon.com/cdk/api/v2/python/index.html

from aws_cdk import (
    aws_lambda_python_alpha,
    aws_lambda,
    aws_dynamodb,
    aws_events,
    aws_events_targets,
    aws_iam,
    CfnTag,
    Stack
)
import aws_cdk.aws_timestream as timestream

from constructs import Construct


class InfraAwsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create dynamo table
        demo_table = aws_dynamodb.Table(
            self, "event_sourcing_table",
            partition_key=aws_dynamodb.Attribute(
                name="aggregateId",
                type=aws_dynamodb.AttributeType.STRING
            ),
            sort_key=aws_dynamodb.Attribute(
                name="eventId",
                type=aws_dynamodb.AttributeType.STRING
            )
        )

        # create producer lambda function
        producer_lambda = aws_lambda_python_alpha.PythonFunction(self, "producer_lambda_function",
                                              entry='../code',
                                              index='src/entrypoints/aws_lambda.py',
                                              handler="lambda_handler",
                                              runtime=aws_lambda.Runtime.PYTHON_3_9)

        # producer_lambda = aws_lambda_python_alpha.PythonFunction(self, "producer_lambda_function",
        #                                       entry='../src',
        #                                       index='entry_point2.py',
        #                                       handler="lambda_handler",
        #                                       runtime=aws_lambda.Runtime.PYTHON_3_9)

        producer_lambda.add_environment("DYNAMO_TABLE_NAME", demo_table.table_name)
        # grant permission to lambda to write to demo table
        demo_table.grant_read_write_data(producer_lambda)

        ## CREATE event bridge 
        
        self.setup_event_bridge(producer_lambda)

        ## create time stream

        cfn_database = timestream.CfnDatabase(self, "MyCfnDatabase",
                    database_name="core_flight_controller_db",
                    tags=[CfnTag(
                        key="DBtype",
                        value="Core time stream DB"
                    )])

        cfn_table = timestream.CfnTable(self, "MyCfnTable",
                            database_name=cfn_database.database_name,
                            # the properties below are optional
                            table_name="event_time_series",
                            retention_properties= { #in-memory tier of a week and afterwards data will be moved to read-optimised tier for two years.
                                "memoryStoreRetentionPeriodInHours": 24*7,
                                "magneticStoreRetentionPeriodInDays": 365*2
                            },
                            tags=[CfnTag(
                                key="tableType",
                                value="Core time stream table"
                            )])
        cfn_table.node.add_dependency(cfn_database)
        
        producer_lambda.add_to_role_policy(aws_iam.PolicyStatement(
                    resources=["*"],
                    actions=["timestream:*"]
            ))



    def setup_event_bridge(self, base_lambda: aws_lambda.IFunction):
        # create event bus for core to consume
        eventBus = aws_events.EventBus(
            scope=self, id="main_lambda_bus", event_bus_name="MainEventBus")
        eventPattern  = aws_events.EventPattern(source=['contino.custom'])
        lambdaTarget1 = aws_events_targets.LambdaFunction(handler=base_lambda)

        

        aws_events.Rule(scope=self,
                        id="coreevent",
                        rule_name="routeToLambda",
                        targets=[lambdaTarget1],
                        description="pushing straight to main lambda",
                        event_bus=eventBus,
                        event_pattern=eventPattern,
                        )
