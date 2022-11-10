from typing import List, Tuple
from enum import Enum

from aws_cdk import (
    aws_lambda_python_alpha,
    aws_lambda,
)
from constructs import Construct


class LambdaPtyhonWithRequirements(Construct):
    """Class that creates a python lambda function. it packages all the dependecies defined in the requirements.txt file.
    !important! entry point should be at the root of the python src code. That is, if you are suing the __init__.py
    for crating the package structure then your "entry" will be a folder above the package root structure.

    code <-- !!entry point
      |
      requirements.txt <-- !!requirements fo all your lambda functions
      -- src
        |
        __init__.py
        sourceCode0.py
        entrypoints
           |
           aws_lambda.py <-- !!lambda handler at src/entrypoints/aws_lambda.py
        folder1
           |
           __init__.py
           sourceCode1.py
        folder2
           |
           __init__.py
           sourceCode3.py



    - you need to put the "requirements.txt" shold be at the same level as the "src" fodler for them to be packaged with
    the lambda function

    - sourceCode3.py imports sourceCode0.py as follows
    ## sourceCode3.py source code
    import src.sourceCode0

    -- "index" defines the location of your lambda code and it starts from the "src" folder as relative path

    your AWS cdk should be at the asme level with the "code (entry)" folder. Eg.

    code <-- entry point
    infra_aws_cdk
      |
      -- infra_aws_cdk
        |
        aws_stack.py

    """

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, f"{id}-construct", **kwargs)
        self.entry = "../code"
        self.index = "src/entrypoints/aws_lambda.py"
        self.handler = "lambda_handler"

        self.producer_lambda = aws_lambda_python_alpha.PythonFunction(
            self,
            id,
            entry=self.entry,
            index=self.index,
            handler=self.handler,
            runtime=aws_lambda.Runtime.PYTHON_3_9,
        )

    def get_lambda(self):
        return self.producer_lambda
