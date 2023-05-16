import json
from typing import Any

from constructs import Construct
from imports.grafana.dashboard import Dashboard
from imports.grafana.data_source import DataSource
from imports.grafana.folder import Folder


# Function for updating the datasource in the static dashboard.json config file.
# This allowing the datasource and config to be updated at the same time. Aswell as removes production config issues where it uses dev/different datasource uid.
def update_uid(obj: dict, uid: str) -> None:
    if isinstance(obj, dict):
        for key in obj:
            if key == "targets":
                for target in obj[key]:
                    if target["datasource"]["type"] == "grafana-timestream-datasource":
                        if target["datasource"]["uid"] != uid:
                            target["datasource"]["uid"] = uid
            else:
                update_uid(obj[key], uid)
    elif isinstance(obj, list):
        for item in obj:
            update_uid(item, uid)


# Create a new component
class GrafanaDashboardComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        data: Any
    ):
        super().__init__(scope, id)

        self.folder = Folder(self, "folder", title="AWS Flight Controller")

        datasource_config = json.dumps({
                        'authType': 'ec2_iam_role',
                        'defaultRegion': 'ap-southeast-2',
                        'defaultDatabase': '"core_timestream_db"',
                        'defaultTable': '"metrics_table"'
                    })

        self.datasource = DataSource(
            self,
            "timestream-datasource",
            name="Flight Controller Timestream",
            type="grafana-timestream-datasource",
            is_default=True,
            json_data_encoded=datasource_config
        )

        # Update datasource UID
        update_uid(data, self.datasource.uid)
        
        # Convert the data to a JSON string
        data = json.dumps(data)
    
        # Create a new Grafana dashboard
        self.dashboard = Dashboard(
            self,
            "dashboard",
            config_json=data,
            overwrite=True,
            folder=self.folder.id,
        )
       
