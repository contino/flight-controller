<h1 align="center">Flight Controller GCP Infrastructure</h1>
<p align="center">Terraform CDK code for Flight Controller's GCP infrastructure</p>

## Architecture

![Flight Controller Architecture](images/gcp_flight_controller.png)

## Development

GCP's infrastructure deployment is divided in two parts viz. `base_gcp_infra` and `main_gcp_infra`. Reason being we need to setup Artifact registry first before uploading the container image and creating a Cloud Run service using the same image. 

Here are the components built in stage `base_gcp_infra`:
    - Enable relevant API's
    - Service Accounts
    - Artifact Registry

Subsequently, following components are built in stage `main_gcp_infra`:
    - Bigquery datasets and tables
    - PubSub topic
    - EventArc trigger
    - Cloud Run service (for event receiver)
    - Cloud Run service (for Grafana)
    - Load balancing components (NEG, URLMap, Frontend, backend, Global address)

### Deploying a change

- Authenticate to Google Cloud and set the correct project using `gcloud config set project $MY_PROJECT_ID`
- Synth, plan and deploy both infra & Grafana Dashboard.
  - `make build`
  - `make plan`
  - `make deploy`

### Make Commands

- `make clean` remove the cdktf.out file.
- `make synth-gcp` cdktf synth the core GCP infrastructure
- `make synth-gcp-grafana` cdktf synth the grafana infrastructure
- `make plan-gcp` cdktf plan the core GCP infrastructure
- `make plan-gcp-grafana` cdktf plan the grafana infrastructure
- `make plan-gcpstack` cdktf both base and main stacks for GCP infrastructure
- `make deploy-base-gcp` deploy base GCP infrastructure
- `make build-image` build, tag and push docker image to artifact registry
- `make deploy-main-gcp` deploy main GCP infrastructure

### Configure Grafana

WHilst writing this, running Grafana with Identiy-Aware Proxy is work in progress due to Cognizant ingetation. Therefore, accessing Grafana from the Cloud Run is not possible. 

As a workaround, it is recommended to run the Grafana container locally using the below image on `PORT: 3000`:
`mirror.gcr.io/grafana/grafana:latest`

#### Adding the BigQuery Plugin

1. Open the side menu by clicking the Grafana icon in the top header.
2. In the side menu under `Configuration` you should find a link named `Plugins`.
3. Type `BigQuery` in the search bar
4. Select Google BigQuery by "doitintl" from the list.
4. Finally, click on `Install`

#### Adding the DataSource to Grafana

There are two ways to authenticate the BigQuery plugin - either by uploading a Google JWT file, or by automatically retrieving credentials from Google's metadata server. The latter is only available when running Grafana on a GCE virtual machine.

##### Using a Google Service Account Key File

Create a GCP Service Account for a Project
1. Navigate to the `APIs & Services Credentials` page.
2. Click on `Create credentials` and choose `Service account key`.
![Create Credentials](images/credentials.png)

3. On the Create service account key page, choose key type `JSON`. Then in the Service Account dropdown, choose the `New service account` option:
![New Service Account](images/service_account_key.png)

4. Some new fields will appear. Fill in a name for the service account in the `Service account name` field and then choose the `BigQuery Data Viewer` and `BigQuery Job User` roles from the Role dropdown:
![Attach roles](images/service_account_role.png)

5. Click the `Create` button. A JSON key file will be created and downloaded to your computer. Store this file in a secure place as it allows access to your BigQuery data.

6. Upload it to Grafana on the datasource Configuration page. You can either upload the file or paste in the contents of the file.
![Grafana authentication](images/grafana_authentication.png)

7. The file contents will be encrypted and saved in the Grafana database. Don't forget to save after uploading the file!


#### Creating Dashboards

A dashboard in Grafana is represented by a JSON object, which stores metadata of its dashboard.

You can create a dashboard by simply uploading the `dashboard.json` file located within the `infrastructure/gcp` folder:

1. Open the side menu by clicking the Grafana icon in the top header.
2. In the side menu under `Dashboards` you should find a link named `Import`.
3. Upload the `dashboard.json` file
4. Finally, click on `Load`

This will create the Dashboard. In case, you decide to add new panels manually, remember to update the `dahboard.json` file and commit it along with the source code. This way, everyone can have the same view of dashboard.