#!/usr/bin/env python

import json
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_azurerm.provider import AzurermProvider
from cdktf_cdktf_provider_azurerm import (
    resource_group,
    storage_account,
    storage_container,
    mssql_server,
    mssql_database,
    service_plan,
    linux_function_app,
    eventgrid_topic
)
from imports.grafana.provider import GrafanaProvider
from imports.grafana.folder import Folder

class AzureCore(TerraformStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
    ):
        super().__init__(scope, id)

        AzurermProvider(
            self, 
            "Azure", 
            features = {}
        )

        with open("azurerm.json", "r") as f:
            az = json.load(f)

        rg = resource_group.ResourceGroup(
            self, 
            az['resource_group']['key'],
            name      = f"{az['key']}{az['env']}{az['resource_group']['key']}",
            location  = az['location']
        )

        sa = storage_account.StorageAccount(
            self,
            az['storage_account']['key'],
            location                   = az['location'],
            name                       = f"{az['key']}{az['env']}{az['storage_account']['key']}",
            account_tier               = az['storage_account']['tier'],
            account_replication_type   = az['storage_account']['replication'],
            resource_group_name        = rg.name
        )

        sc = storage_container.StorageContainer(
            self, 
            az['storage_container']['key'],
            name = f"{az['key']}{az['env']}{az['storage_container']['key']}",
            storage_account_name = sa.name
        )

        sql = mssql_server.Mssql(
            self, 
            az['mssql_server']['key'],
            name = f"{az['key']}{az['env']}{az['mssql_server']['key']}",
            location = az['location'],
            version  = az['mssql_server']['version'],
            administrator_login = az['mssql_server']['administrator_login'],
            administrator_login_password = az['mssql_server']['administrator_login_password'],
            resource_group_name = rg.name
        )

        db = mssql_database.MssqlDatabase(
            self, 
            az['mssql_database']['key'],
            name = f"{az['key']}{az['env']}{az['mssql_database']['key']}",
            sku_name = az['mssql_database']['sku_name'],
            collation = az['mssql_database']['collation'],
            create_mode = az['mssql_database']['create_mode'],
            server_id = sql.id
        )

        svc = service_plan.ServicePlan(
            self, 
            az['service_plan']['key'],
            location = az['location'],
            name = f"{az['key']}{az['env']}{az['service_plan']['key']}",
            sku_name = az['service_plan']['sku_name'],
            os_type = az['service_plan']['os_type'],
            resource_group_name = rg.name
        )

        fnc = linux_function_app.LinuxFunctionApp(
            self,
            az['linux_function_app']['key'],
            name = f"{az['key']}{az['env']}{az['linux_function_app']['key']}",
            location = az['location'],
            resource_group_name = rg.name,
            service_plan_id = svc.id,
            storage_account_name = sa.name,
            storage_account_access_key = sa.primary_access_key,
            site_config = { },
            identity = { "type": "SystemAssigned" }
        )

        eventgridtopic = eventgrid_topic.EventgridTopic(
            self,
            az['eventgrid_topic']['key'],
            location = az['location'],
            resource_group_name = rg.name,
            name = f"{az['key']}{az['env']}egt"
        )

class AzureGrafana(TerraformStack):
    def __init__(self, scope: Construct, id: str, workspace_id: str):
        super().__init__(scope, id)
        
        AzurermProvider(
            self, 
            "Azure", 
            features = {}
        )

        self.grafana = {
            'auth': 'supersecretkeygoeshere',
            'url': 'https://apacfcdevgrafana.azurewebsites.net'
        }

        GrafanaProvider(
            self,
            "Grafana",
            auth = self.grafana['auth'],
            url = self.grafana['url']
        )

        with open("dashboard.json", "r") as config:
            data = json.load(config)

        self.folder = Folder(
            self, 
            "folder", 
            title = "Azure Flight Controller"
        )
                
        self.dashboard = Dashboard(
            self,
            "dashboard",
            config_json = json.dumps(data),
            overwrite = True,
            folder = self.folder.id
        )


app = App()
core_stack = AzureCore(app, "azure_core")
#grafana_dashboard_stack = AzureGrafana(app, "azure_grafana_dashboard", core_stack.grafana_workspace_id)
app.synth()
