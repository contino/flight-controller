from cdktf_cdktf_provider_google import (cloud_run_service, project_iam_member,
                                         service_account)
from constructs import Construct


class CloudRunComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        project_id: str,
        location: str,
        name_prefix: str,
        cloudrun_account: service_account.ServiceAccount,
    ):
        super().__init__(scope, id)

        self.service = cloud_run_service.CloudRunService(
            self,
            "flight_controller_service",
            name=f"{name_prefix}-service",
            location=location,
            project=project_id,
            metadata={"annotations": {"run.googleapis.com/ingress": "internal"}},
            template={
                "spec": {
                    "containers": [
                        {
                            "image": "australia-southeast1-docker.pkg.dev/contino-squad0-fc/flight-controller-event-receiver/event_receiver:latest",
                            "ports": [{"container_port": 8080}],
                        },
                    ],
                    "service_account_name": f"{cloudrun_account.email}",
                }
            },
        )

        self.bigquery_job = project_iam_member.ProjectIamMember(
            self,
            "bigquery_job",
            role="roles/bigquery.dataEditor",
            member=f"serviceAccount:{cloudrun_account.email}",
            project=project_id,
        )
