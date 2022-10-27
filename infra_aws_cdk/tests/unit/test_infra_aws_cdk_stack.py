import aws_cdk as core
import aws_cdk.assertions as assertions

from infra_aws_cdk.infra_aws_cdk_stack import InfraAwsCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in infra_aws_cdk/infra_aws_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = InfraAwsCdkStack(app, "infra-aws-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
