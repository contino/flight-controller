import json
import requests

# Set up the API URL and authentication credentials
url = "https://g-2e637a6ddc.grafana-workspace.ap-southeast-2.amazonaws.com/api/dashboards/db"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer eyJrIjoiekNIV2hqbzdtUVMzcmhGZVNaYXJXNmNBZ2w0ZDhDcnMiLCJuIjoiYWRtaW4iLCJpZCI6MX0="
}


# Load the dashboard configuration from a JSON file
with open("dashboard.json", "r") as f:
    data = json.load(f)


# Convert the data to a JSON string
data = json.dumps(data)

# Send the API request to create the dashboard
response = requests.post(url=url, headers=headers, json=data)

# Check the response status code
if response.status_code != 200:
    print("Error creating dashboard:", response.content)
else:
    print("Dashboard created successfully")