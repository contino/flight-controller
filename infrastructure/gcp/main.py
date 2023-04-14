#!/usr/bin/env python

from cdktf import App, TerraformStack, GcsBackend
from constructs import Construct
from cdktf_cdktf_provider_google.provider import GoogleProvider
from cdktf_cdktf_provider_google import kms_key_ring
from services_component import ServicesComponent
from service_account_component import ServiceAccountComponent
from bigquery_component import BigQueryComponent
from artifact_registry_component import ArtifactRegistryComponent
from eventarc_with_pubsub_component import EventarcWithPubsubComponent
from cloudrun_component import CloudRunComponent
from grafana_cloudrun_component import GrafanaComponent
from lb_component import LBComponent
from imports.grafana.provider import GrafanaProvider
from grafana_dashboard_component import GrafanaDashboardComponent

# ProjectID & location
project_id = "contino-squad0-fc"
project_number = "564183220985"
location = "australia-southeast1"

# Variables
event_table_name = "event_sourcing_table"
metric_table_name = "metric_sourcing_table"
artifactregistry_name = "flight-contoller-event-receiver"
eventarc_name = "flight-controller"
cloudrunservice_name = "flight-controller-service"
grafanaservice_name = "flight-controller-grafana"
loadbalanacer_name = "flight-controller-grafana-lb"

class GcpBase(TerraformStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
    ):
        super().__init__(scope, id)

        GoogleProvider(self, "BASE_GCP")

        # Enable services API
        servicesComponent = ServicesComponent(
            self, "services", project_id,
        )

        # Create service account
        serviceAccountComponent = ServiceAccountComponent(
            self, "service_account", project_id,
        )
        self.fc_account = serviceAccountComponent.flight_controller
        self.cloudrun_account = serviceAccountComponent.cloud_run
        
        flight_controller_key_ring = kms_key_ring.KmsKeyRing(
            self,
            "flight_controller_key_ring",
            name="flight-controller",
            location=location
        )
        
        self.key_ring = flight_controller_key_ring
        # Create artifact registry to store docker images
        artifactRegistryComponent = ArtifactRegistryComponent(
            self, 
            "artifact_registry", 
            project_id, 
            project_number,
            location, 
            artifactregistry_name, 
            serviceAccountComponent.cloud_run,
            flight_controller_key_ring
        )

        
class GcpCore(TerraformStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        fc_account: str,
        cloudrun_account: str,
        key_ring: kms_key_ring.KmsKeyRing
    ):
        super().__init__(scope, id)

        GoogleProvider(self, "GCP")


        # create BigQuery component
        bigQueryComponent = BigQueryComponent(
            self, 
            "event_table",  
            project_id,
            project_number, 
            location, 
            event_table_name, 
            metric_table_name,
            cloudrun_account,
            key_ring
        )

        # Create cloud run service
        cloudRunComponent = CloudRunComponent(
            self, 
            "cloud_run", 
            project_id, 
            location, 
            cloudrunservice_name, 
            cloudrun_account,
        )

        # Create event arc trigger
        eventArcComponent = EventarcWithPubsubComponent(
            self, "trigger", 
            project_id, 
            project_number,
            location, 
            eventarc_name, 
            cloudRunComponent.service,
            fc_account,
            cloudrun_account,
            key_ring
        )

        # Create Grafana Cloud Run service
        grafanaComponent = GrafanaComponent(
            self, 
            "grafana_service", 
            project_id, 
            location, 
            grafanaservice_name, 
            cloudrun_account,
        )
        
        # Create Load balancer for grafana service
        lbComponent = LBComponent(
            self, 
            "load_balancer", 
            project_id, 
            location, 
            loadbalanacer_name, 
            grafanaservice_name
        )
        # self.grafana_workspace_id = lbComponent.global_address.address

# class GcpGrafana(TerraformStack):
#     def __init__(self, scope: Construct, id: str, workspace_id: str,):
#         super().__init__(scope, id)
        
#         GrafanaProvider(
#             self,
#             "Grafana",
#             auth="",
#             url=workspace_id
#             + ":80",
#         )

#         # Create Grafana dashboard
#         GrafanaDashboardComponent(
#             self,
#             "grafana_dashboard",
#         )

app = App()

base_stack = GcpBase(app, "gcp_base",)

core_stack = GcpCore(app, "gcp_core", base_stack.fc_account, base_stack.cloudrun_account, base_stack.key_ring)

# grafana_stack = GcpGrafana(app, "gcp_grafana", gcp_stack.grafana_workspace_id)

GcsBackend(
    base_stack,
    bucket = "flight-controller-state",
    prefix="base_gcp_infra/terraform.tfstate",
)

GcsBackend(
    core_stack,
    bucket = "flight-controller-state",
    prefix="main_gcp_infra/terraform.tfstate",
)

# GcsBackend(
#     grafana_stack,
#     bucket = "flight-controller-state",
#     prefix="grafana_infra/terraform.tfstate",
# )

app.synth()
