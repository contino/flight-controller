import json

from cdktf_cdktf_provider_aws import (cloudwatch_event_bus,
                                      cloudwatch_event_rule,
                                      cloudwatch_event_target, lambda_function,
                                      lambda_permission)
from constructs import Construct


class EventBridgeComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        name: str,
        lambda_target: lambda_function.LambdaFunction,
    ):
        super().__init__(scope, id)

        event_bus = cloudwatch_event_bus.CloudwatchEventBus(self, "eventbus", name=name)
        event_rule = cloudwatch_event_rule.CloudwatchEventRule(
            self,
            "eventRule",
            name="eventrule_cdktf",
            event_bus_name=event_bus.name,
            event_pattern=json.dumps({"source": [{"prefix": "contino"}]}),
        )

        event_target = cloudwatch_event_target.CloudwatchEventTarget(
            self,
            "event_target",
            target_id="target_id1",
            event_bus_name=event_bus.name,
            arn=lambda_target.arn,
            rule=event_rule.name,
        )

        lambda_permission.LambdaPermission(
            self,
            "lambda_resource_policy",
            statement_id="alloweventBridgetrigger",
            action="lambda:InvokeFunction",
            function_name=lambda_target.function_name,
            principal="events.amazonaws.com",
            source_arn=event_rule.arn,
        )
