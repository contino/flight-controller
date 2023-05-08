#!/usr/bin/env python

from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_azure.provider import AzurermProvider
from constructs import Construct

class AzureCore(TerraformStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
    ):
        super().__init__(scope, id)

        AzurermProvider(self, "Azure")

        self.dynamotable_name = "event_sourcing_table"
        self.lambda_name = "producer_lambda_function_cdktf"
        self.event_bridge_name = "main_lambda_bus_cdktf"
        self.timestream_db_name = "core_timestream_db"
        self.grafana_workspace_name = "grafana_dashboard"
        self.grafana_lambda_name = "grafana_api_key_rotator"

app = App()
core_stack = AzureCore(app, "azure_core")
app.synth()
