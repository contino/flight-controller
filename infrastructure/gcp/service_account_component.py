from cdktf_cdktf_provider_google import (
    service_account, 
    service_account_iam_binding,
)
from constructs import Construct


class ServiceAccountComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        project_id: str,
    ):
        super().__init__(scope, id)

        self.flight_controller = service_account.ServiceAccount(
            self,
            "flight-controller",
            project=project_id,
            account_id="fc-account",
        )

        self.cloud_run = service_account.ServiceAccount(
            self, "cloud-run", 
            project=project_id, 
            account_id="fc-cloud-run"
        )
        
        self.grafana = service_account.ServiceAccount(
            self, "grafana", 
            project=project_id, 
            account_id="fc-grafana"
        )