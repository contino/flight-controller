from aws_cdk import (
    aws_lambda,
    aws_events,
    aws_events_targets
)

from constructs import Construct

class EventBridgeWithLambdaRule(Construct):
    """Class that creates an event bridge with the associated rules.
    it sends the events to the lambda that is passed in the constructor.
    """
    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        send_event_to: aws_lambda.IFunction,
        **kwargs
    ):
        super().__init__(scope, f"{id}-construct", **kwargs)
        
        # create event bus for core to consume
        eventBus = aws_events.EventBus(
            scope=scope, id=f"{id}-eventbus", event_bus_name=id
        )

        # Create event pattern and associated rule 
        eventPattern = aws_events.EventPattern(source=["contino.custom"])
        lambdaTarget1 = aws_events_targets.LambdaFunction(handler=send_event_to)

        aws_events.Rule(
            scope=self,
            id="coreevent",
            rule_name="routeToLambda2",
            targets=[lambdaTarget1],
            description="pushing straight to main lambda",
            event_bus=eventBus,
            event_pattern=eventPattern,
        )
