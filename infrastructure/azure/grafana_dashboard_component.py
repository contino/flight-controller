# Import the necessary modules
from constructs import Construct
import json

from imports.grafana.folder import Folder
from imports.grafana.dashboard import Dashboard

with open("dashboard.json", "r") as config:
    data = json.load(config)

data = json.dumps(data)

class GrafanaDashboardComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
    ):
        super().__init__(scope, id)

        self.folder = Folder(self, "folder", title="Azure Flight Controller")        
        self.dashboard = Dashboard(
            self,
            "azure-dashboard",
            config_json=data,
            overwrite=True,
            folder=self.folder.id,
        )
