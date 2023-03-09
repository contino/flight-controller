from constructs import Construct
from cdktf_cdktf_provider_google import service_account, data_google_iam_policy, service_account_iam_policy


class ServiceAccountComponent(Construct):
    def __init__(self, scope: Construct, id: str, project_id: str,):
        super().__init__(scope, id)

        self.flight_controller = service_account.ServiceAccount(
           self,
           "flight-controller",
           project=project_id,
           account_id="fc-account",
        )

        self.cloud_run = service_account.ServiceAccount(
            self,
            "cloud-run",
            project=project_id,
            account_id="fc-cloud-run"
        )