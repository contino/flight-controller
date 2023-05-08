#!/usr/bin/env python

from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_azurerm.provider import AzurermProvider
from imports.grafana.provider import GrafanaProvider
from grafana_dashboard_component import GrafanaDashboardComponent
from cdktf_cdktf_provider_azurerm import (
    resource_group
)


class AzureCore(TerraformStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
    ):
        super().__init__(scope, id)

        self.location = "australiasoutheast"
        self.resource_group_name = "flight_controller"
        self.function_name = "azfcdev"
        self.azure_sql = "azfcdevdb"
        self.grafana_workspace_name = "grafana_dashboard"

        AzurermProvider(
            self, 
            "Azure", 
            features = {}
        )

        resourceGroup = resource_group.ResourceGroup(
            self, 
            "rg",
            name = self.resource_group_name,
            location = self.location,
        )
        
        # self.grafana_workspace_id = grafanaWorkspace.grafana_workspace.id

class AzureGrafana(TerraformStack):
    def __init__(self, scope: Construct, id: str, workspace_id: str):
        super().__init__(scope, id)
        
        AzurermProvider(
            self, 
            "Azure", 
            features = {}
        )

        GrafanaProvider(
            self,
            "Grafana",
            auth=api_key.secret_string,
            url="https://"
            + workspace_id
            + ".azurewebsites.net",
        )

        GrafanaDashboardComponent(
            self,
            "grafana_dashboard"
        )


app = App()
core_stack = AzureCore(app, "azure_core")
#grafana_dashboard_stack = AzureGrafana(app, "azure_grafana_dashboard", core_stack.grafana_workspace_id)
app.synth()
