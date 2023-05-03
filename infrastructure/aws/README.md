<h1 align="center">Flight Controller AWS Infrastructure</h1>
<p align="center">Terraform CDK code for Flight Controller's AWS infrastructure</p>

## Architecture

![Flight Controller Architecture](/images/aws_flight_controller.png)

## Development

### Deploying a change

- Assume the correct AWS account/refresh credentials
- Synth, plan and deploy both infra & Grafana Dashboard.
  - `make aws-synth`
  - `make aws-plan-all`
  - `make aws-deploy-all`

### Make Commands

- `make aws-build-dependencies` build all the lambda requirements and store in `infrastructure/aws/controller_core`
- `make aws-synth` cdktf synth the all the stacks
- `make aws-plan-core` cdktf plan the core stack
- `make aws-plan-grafana` cdktf plan the grafana dashboard stack
- `make aws-plan-all` cdktf plan all stacks
- `make aws-deploy-core` cdktf deploy the core_stack
- `make aws-deploy-grafana` cdktf deploy the grafanadashboard stack
- `make aws-deploy-all` cdktf deploy all stacks
- `make aws-destroy-core` cdktf destroy core stack
- `make aws-destroy-grafana` cdktf destroy grafana deashboard stack
- `make aws-destroy-all` cdktf destroy all stacks
- `make aws-test` aws specific tests
- `make aws-e2e` aws specific end to end tests

## Grafana

### Creating Dashboards

Dashboards are added using the terrafrom. Fortunately, you can use JSON templates to make it easier to manage your Terraform-provisioned Grafama dashboards without having to convert them to HCL syntax or CDKTF.

1. Within `infrastructure/aws`, JSON file is pre-created named `dashboard.json`
2. To update the dashboard/panels, simple update the json code and run the CI pipeline using Github actions. This will update the Grafana dashboard.
3. To add new dashboard, create a new JSON file. 
4. Add terraform block of code for newly created JSON file in the `grafana_dashboard_component.py` file.

### Terraform configuration for Grafana provider

This Terraform configuration configures the Grafana provider to provide necessary authentication when creating folders and dashboards in the Grafana instance.

API key is created by the terraform whilst core AWS infrastructure is being deployed. After creating the key it is stored in the AWS Secrets Manager to be used as required to run Grafana Terraform CDK stack. 

### Managing Grafana API Keys

While writing this, Grafana API Keys are valid for maximum 30 days only. 
Hopefully, Amazon will address this limitation in the future - but in the meantime, this simple pattern can be used to automatically rotate an API key every 29 days and store it for use in AWS Secrets Manager.

![Grafana](/images/manage_grafana_api_key.png)

The solution is made up of two components:

1. AWS Secret is created with a rotation lifecycle policy that will trigger a Lambda function every 29 days
2. AWS Lambda Function that will create a new API key in Amazon Managed Grafana and update the AWS Secret with the new key

Python code handling the rotation is stored  at `src/entrypoint/grafana_lambda.py`. The code expects two input variables to retrieve secret values from AWS Secrets Manager viz. `grafana_api_key_name` and `grafana_workspace_id`. As the name suggest these values are secret names being used as filters.
