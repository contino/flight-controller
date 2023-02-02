import json

# import requests

# # Set up the API URL and authentication credentials
# url = "https://g-2e637a6ddc.grafana-workspace.ap-southeast-2.amazonaws.com/api/dashboards/db"
# headers = {
#     # "Content-Type": "application/json",
#     # "Accept": "application/json",
#     "Authorization": "Bearer eyJrIjoiekNIV2hqbzdtUVMzcmhGZVNaYXJXNmNBZ2w0ZDhDcnMiLCJuIjoiYWRtaW4iLCJpZCI6MX0="
# }


# # Load the dashboard configuration from a JSON file
# with open("dashboard.json", "r") as f:
#     data = json.load(f)


# # Send the API request to create the dashboard
# response = requests.post(url=url, headers=headers, json=data)

# # Check the response status code
# if response.status_code != 200:
#     print("Error creating dashboard:", response.content)
# else:
#     print("Dashboard created successfully")

# Import the necessary modules
from constructs import Construct

# from cdktf import TerraformStack
from imports.grafana.folder import Folder
from imports.grafana.dashboard import Dashboard
from imports.grafana.provider import GrafanaProvider
from managed_grafana_component import grafana_workspace_api_key

# Load the dashboard configuration from a JSON file
with open("dashboard.json", "r") as f:
    data = json.load(f)

# Convert the data to a JSON string
data = json.dumps(data)


# Create a new component
class GrafanaDashboardComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        grafana_workspace_api_key: grafana_workspace_api_key.GrafanaWorkspaceApiKey,
    ):
        super().__init__(scope, id)

        self.folder = Folder(self, "folder", title="Terraform Test Folder")

        # Create a new Grafana dashboard
        self.dashboard = Dashboard(
            self,
            "my-dashboard",
            config_json=data,
            overwrite=True,
            folder=self.folder.id,
        )
