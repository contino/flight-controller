import os

os.chdir("infra_aws_cdk")

import aws_cdk as core
import aws_cdk.assertions as assertions
from aws_cdk.assertions import Match

from infra_aws_cdk.infra_aws_cdk_stack import InfraAwsCdkStack


app = core.App()
stack = InfraAwsCdkStack(app, "infra-aws-cdk")
template = assertions.Template.from_stack(stack)


def test_lambda_is_created_with_correct_runtime():
    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Handler": "src.entrypoints.aws_lambda.lambda_handler",
            "Runtime": "python3.9",
        },
    )


def test_dynamodb_is_created_with_correct_partition_and_sort_key():
    template.has_resource_properties(
        "AWS::DynamoDB::Table",
        {
            "KeySchema": [
                {"AttributeName": "aggregateId", "KeyType": "HASH"},
                {"AttributeName": "eventId", "KeyType": "RANGE"},
            ],
            "AttributeDefinitions": [
                {"AttributeName": "aggregateId", "AttributeType": "S"},
                {"AttributeName": "eventId", "AttributeType": "S"},
            ],
            "ProvisionedThroughput": {
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
        },
    )


def test_eventbridge_bus_is_created():
    template.has_resource_properties(
        "AWS::Events::EventBus",
        {"Name": "main_lambda_bus"},
    )


def test_eventbridge_rule_is_created_with_correctlambda():
    template.has_resource_properties(
        "AWS::Events::Rule",
        {"EventPattern": {"source": ["contino.custom"]}, "Name": "routeToLambda2"},
    )


def test_timestream_database_is_created_with_correct_name():
    template.has_resource_properties(
        "AWS::Timestream::Database",
        {"DatabaseName": "core_timestream_db"},
    )


def test_timestream_table_is_created_with_correct_name_and_retention():
    template.has_resource_properties(
        "AWS::Timestream::Table",
        {
            "DatabaseName": "core_timestream_db",
            "RetentionProperties": {
                "memoryStoreRetentionPeriodInHours": 168,
                "magneticStoreRetentionPeriodInDays": 730,
            },
        },
    )
