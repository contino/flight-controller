# import json
# import requests

# # Set up the API URL and authentication credentials
# url = "https://g-2e637a6ddc.grafana-workspace.ap-southeast-2.amazonaws.com/api/dashboards/db"
# headers = {
#     # "Content-Type": "application/json",
#     # "Accept": "application/json",
#     "Authorization": "Bearer eyJrIjoiZnhrMXVCb3c5ajZSUlFDQU1hMXdRUzZEVTFzREJPOGIiLCJuIjoiZmxpZ2h0LWNvbnRyb2xsZXItZ3JhZmFuYS1hcGkta2V5IiwiaWQiOjF9"
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
from cdktf import TerraformStack

from imports.grafana.dashboard import Dashboard
from imports.grafana.provider import GrafanaProvider


# Create a new stack


class GrafanaStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        GrafanaProvider(self, "Grafana")

        # Create a new Grafana dashboard

        self.dashboard = Dashboard(
            self,
            "my-dashboard",
            config_json="""{
      title: 'My Dashboard',
      panels: [
        {
          type: 'graph',
          title: 'My Graph',
          dataselect: {
            time: {
              from: 'now-6h',
              to: 'now'
            }
          },
          targets: [
            {
              expr: 'SELECT value FROM my-existing-database.my-existing-table WHERE time >= now() - 6h AND time <= now()',
              timestream: {
                query: {
                  database: 'my-existing-database',
                  table: 'my-existing-table'
                }
              }
            }
          ]
        }
      ]
    }""",
        )
