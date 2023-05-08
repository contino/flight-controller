#!/usr/bin/env python

from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_azurerm.provider import AzurermProvider
from constructs import Construct

class AzureCore(TerraformStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
    ):
        super().__init__(scope, id)

        AzurermProvider(self, "Azure")

        self.resource_group = "rg_name"

app = App()
core_stack = AzureCore(app, "azure_core")
app.synth()
