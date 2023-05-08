# Import the necessary modules
import json

from constructs import Construct
from imports.grafana.dashboard import Dashboard
from imports.grafana.folder import Folder

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
    ):
        super().__init__(scope, id)

        self.folder = Folder(self, "folder", title="AWS Flight Controller")

        # Create a new Grafana dashboard
        self.dashboard = Dashboard(
            self,
            "my-dashboard",
            config_json=data,
            overwrite=True,
            folder=self.folder.id,
        )
