import pytest 
from cdktf import ( 
    Testing, 
    TerraformStack
)
from main import MyStack

# The tests below are example tests, you can find more information at
# https://cdk.tf/testing

class TestMain:

    def test_my_app(self):
        assert True

    stack = TerraformStack(Testing.app(), "stack")
    app_abstraction = MyStack(stack, "app-abstraction")
    synthesized = Testing.synth(stack)
    
    def test_lambda_is_created_with_correct_runtime(self):
        Testing.to_have_resource_with_properties(
            self.synthesized,
            "AWS::Lambda::Function",
            {
                "Handler": "src.entrypoints.aws_lambda.lambda_handler",
                "Runtime": "python3.9",
            },
        )