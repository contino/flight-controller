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

import * as cdktf from 'cdktf';

import grafana from cdktf-provider-grafana

import * as grafana from "imports/grafana/"

import grafana_provider from 

 

# Create a new stack

class MyStack extends cdktf.Stack {
  constructor(scope: cdktf.App, id: string, props?: cdktf.StackProps) {
    super(scope, id, props);

    # Create a new Grafana dashboard

    new grafana.Dashboard(this, 'my-dashboard', {
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
    });
  }
}
# Create a new CDKTF app

const app = new cdktf.App();
new MyStack(app, 'my-stack');
app.synth();