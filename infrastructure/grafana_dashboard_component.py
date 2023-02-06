# Import the necessary modules
from constructs import Construct
import json

from imports.grafana.folder import Folder
from imports.grafana.dashboard import Dashboard

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
        # grafana_workspace_api_key: grafana_workspace_api_key.GrafanaWorkspaceApiKey,
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
