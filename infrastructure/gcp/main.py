#!/usr/bin/env python

from artifact_registry_component import ArtifactRegistryComponent
from bigquery_component import BigQueryComponent
from cdktf import App, GcsBackend, TerraformStack
from cdktf_cdktf_provider_google import kms_key_ring, service_account
from cdktf_cdktf_provider_google.provider import GoogleProvider
from cloudrun_component import CloudRunComponent
from constructs import Construct
from eventarc_with_pubsub_component import EventarcWithPubsubComponent
from grafana_cloudrun_component import GrafanaComponent
from grafana_dashboard_component import GrafanaDashboardComponent
from imports.grafana.provider import GrafanaProvider
from lb_component import LBComponent
from service_account_component import ServiceAccountComponent
from services_component import ServicesComponent

# Constants
PROJECT_ID = "contino-squad0-fc"
PROJECT_NUMBER = "564183220985"
LOCATION = "australia-southeast1"
NAME_PREFIX = "flight-controller"
EVENT_TABLE_NAME = "event_sourcing_table"
METRIC_TABLE_NAME = "metric_sourcing_table"

# GCP Base Stack
class GcpBase(TerraformStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
    ):
        super().__init__(scope, id)

        GoogleProvider(self, "BASE_GCP")

        # Enable services API
        services_component = ServicesComponent(
            self,
            "services",
            PROJECT_ID,
        )

        # Create service account
        service_account_component = ServiceAccountComponent(
            self,
            "service_account",
            PROJECT_ID,
        )

        flight_controller_key_ring = kms_key_ring.KmsKeyRing(
            self,
            "flight_controller_key_ring",
            name=NAME_PREFIX,
            location=LOCATION,
        )

        # Create artifact registry to store docker images
        artifact_registry_component = ArtifactRegistryComponent(
            self,
            "artifact_registry",
            PROJECT_ID,
            PROJECT_NUMBER,
            NAME_PREFIX,
            LOCATION,
            service_account_component.cloud_run,
            flight_controller_key_ring
        )

        # Outputs
        self.fc_account = service_account_component.flight_controller
        self.cloudrun_account = service_account_component.cloud_run
        self.key_ring = flight_controller_key_ring

# GCP Core Stack
class GcpCore(TerraformStack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        fc_account: service_account.ServiceAccount,
        cloudrun_account: service_account.ServiceAccount,
        key_ring: kms_key_ring.KmsKeyRing,
    ):
        super().__init__(scope, id)

        GoogleProvider(self, "GCP")

        # create BigQuery component
        bigquery_component = BigQueryComponent(
            self,
            "event_table",
            PROJECT_ID,
            LOCATION,
            EVENT_TABLE_NAME,
            METRIC_TABLE_NAME,
            key_ring
        )

        # Create cloud run service
        cloudrun_component = CloudRunComponent(
            self,
            "cloud_run",
            PROJECT_ID,
            LOCATION,
            NAME_PREFIX,
            cloudrun_account,
        )

        # Create event arc trigger
        eventarc_component = EventarcWithPubsubComponent(
            self,
            "trigger",
            PROJECT_ID,
            PROJECT_NUMBER,
            LOCATION,
            NAME_PREFIX,
            cloudrun_component.service,
            fc_account,
            cloudrun_account,
            key_ring,
        )

        # Create Grafana Cloud Run service
        grafana_component = GrafanaComponent(
            self,
            "grafana_service",
            PROJECT_ID,
            LOCATION,
            NAME_PREFIX
        )

        # Create Load balancer for grafana service
        lb_component = LBComponent(
            self,
            "load_balancer",
            PROJECT_ID,
            LOCATION,
            NAME_PREFIX,
        )
        # self.grafana_workspace_id = lb_component.global_address.address

# GCP Grafana Stack
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

base_stack = GcpBase(
    app,
    "gcp_base",
)

core_stack = GcpCore(
    app,
    "gcp_core",
    base_stack.fc_account,
    base_stack.cloudrun_account,
    base_stack.key_ring,
)

# grafana_stack = GcpGrafana(app, "gcp_grafana", gcp_stack.grafana_workspace_id)

GcsBackend(
    base_stack,
    bucket="flight-controller-state",
    prefix="base_gcp_infra/terraform.tfstate",
)

GcsBackend(
    core_stack,
    bucket="flight-controller-state",
    prefix="main_gcp_infra/terraform.tfstate",
)

# GcsBackend(
#     grafana_stack,
#     bucket = "flight-controller-state",
#     prefix="grafana_infra/terraform.tfstate",
# )

app.synth()
