#!/usr/bin/env python

import json
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_azurerm.provider import AzurermProvider
from imports.grafana.provider import GrafanaProvider
from imports.grafana.folder import Folder
from imports.grafana.dashboard import Dashboard
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
    
        az_prefix = "apacfc"
        az_env = "dev"
        az_location = "australiaeast"

        az_storage_account = {
            "tier": "Standard",
            "replication": "LRS",
            "public": False,
            "public_nested": False,
            "https_only": True
        }
        az_sql_server = { 
            "version": "12.0",
            "administrator_login": "4dm1n157r470r",
            "administrator_login_password": "4-v3ry-53cr37-p455w0rd"
        }
        az_sql_db = { 
            "sku_name": "GP_Gen5_2",
            "collation": "SQL_Latin1_General_CP1_CI_AS",
            "create_mode": "Default"
        }
        az_svc_plan = { 
            "os_type": "Linux",
            "sku_name": "Y1"
        }

        resourceGroup = resource_group.ResourceGroup(
            self, 
            "rg",
            name = f"{az_prefix}{az_env}rg",
            location = az_location
        )

        storageAccount = storage_account.StorageAccount(
            self,
            "sa",
            location = az_location,
            resource_group_name = resourceGroup.name,
            name = f"{az_prefix}{az_env}sa",
            account_tier = az_storage_account['tier'],
            account_replication_type = az_storage_account['replication']
        )

        storageContainer = storage_container.StorageContainer(
            self,
            "sc",
            name = f"{az_prefix}{az_env}sc",
            storage_account_name = storageAccount.name
        )

        sqlServer = mssql_server.MssqlServer(
            self,
            "sql",
            location = az_location,
            resource_group_name = resourceGroup.name,
            name = f"{az_prefix}{az_env}sql",
            version = az_sql_server["version"],
            administrator_login = az_sql_server["administrator_login"],
            administrator_login_password = az_sql_server["administrator_login_password"]
        )

        sqlDatabase = mssql_database.MssqlDatabase(
            self,
            "db",
            server_id = sqlServer.id,
            name = f"{az_prefix}{az_env}db",
            sku_name = az_sql_db["sku_name"],
            collation = az_sql_db["collation"],
            create_mode = az_sql_db["create_mode"],
        )

        servicePlan = service_plan.ServicePlan(
            self,
            "asp",
            location = az_location,
            resource_group_name = resourceGroup.name,
            name = f"{az_prefix}{az_env}asp",
            sku_name = az_svc_plan["sku_name"],
            os_type = az_svc_plan["os_type"]
        )

        appFnc = linux_function_app.LinuxFunctionApp(
            self,
            "fnc",
            location = az_location,
            resource_group_name = resourceGroup.name,
            service_plan_id = servicePlan.id,
            storage_account_name = storageAccount.name,
            storage_account_access_key = storageAccount.primary_access_key,
            name = f"{az_prefix}{az_env}fnc",
            site_config = { },
            identity = { "type": "SystemAssigned" }
        )

        eventgridtopic = eventgrid_topic.EventgridTopic(
            self,
            "egt",
            location = az_location,
            resource_group_name = resourceGroup.name,
            name = f"{az_prefix}{az_env}egt"
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
