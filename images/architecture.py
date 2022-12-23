# see https://diagrams.mingrammer.com/docs/nodes/aws for different nodes

from diagrams import Cluster, Diagram
from diagrams.aws.integration import Eventbridge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb, Timestream
from diagrams.aws.devtools import Codepipeline, Codebuild
from diagrams.custom import Custom
from diagrams.aws.management import Cloudformation, Config, SystemsManager, Cloudwatch
from diagrams.aws.network import TransitGateway

with Diagram("Flight Controller", show=False):
    with Cluster("Native Events"):
        pubsubNativeNode = Eventbridge("Ingest")
        codepipelineNode = Codepipeline("CI/CD")
        cloudformationNode = Cloudformation("Deployment")
        configNode = Config("Config")
        systemsManagerNode = SystemsManager("Secret")
        cloudwatchNode = Cloudwatch("Logs")
        ## edges
        codepipelineNode >> pubsubNativeNode
        cloudformationNode >> pubsubNativeNode
        configNode >> pubsubNativeNode
        systemsManagerNode >> pubsubNativeNode
        cloudwatchNode >> pubsubNativeNode

    with Cluster("Custom Events"):
        pubsubCustomNode = Eventbridge("Ingest")
        transitGatewayNode = TransitGateway()
        lambdaCustomNode = Lambda("Event handler")
        prometheusNode = Custom("Collection", "./icons/AWS_hosted_promotheus_icon.png")
        codebuildNode = Codebuild("Build")

        # edges
        transitGatewayNode >> lambdaCustomNode >> pubsubCustomNode
        prometheusNode >> pubsubCustomNode
        codebuildNode >> pubsubCustomNode

    with Cluster("Flight Controller Core"):
        pubsubNode = Eventbridge("Ingest")
        lambdaNode = Lambda("Event handler")
        ##edges
        pubsubNode >> lambdaNode

        with Cluster("Storage"):
            dynamoDbNode = Dynamodb("Event Store")
            timestreamNode = Timestream("Time Stream")
            # edges
            lambdaNode >> dynamoDbNode
            lambdaNode >> timestreamNode

    with Cluster("Visualisations"):
        grafanaNode = Custom("Dashboarding", "./icons/AWS_hosted_grafana_icon.png")

    pubsubCustomNode >> pubsubNode
    pubsubNativeNode >> pubsubNode
    timestreamNode << grafanaNode
