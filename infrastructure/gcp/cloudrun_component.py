import string
from constructs import Construct
from cdktf_cdktf_provider_google import (
    cloud_run_service,
    service_account,
    project_iam_member,
)

class CloudRunComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        project_id: str,
        location: str,
        name: str,
        cloudrun_account: service_account.ServiceAccount,
    ):
        super().__init__(scope, id)


        self.service = cloud_run_service.CloudRunService(
            self,
            "flight_controller_service",
            name=name,
            location=location,
            project=project_id,
            metadata={
                "annotations": {
                    "run.googleapis.com/ingress": "internal"
                }
            },
            template={
                "spec": {
                    "containers": [
                        {
                            "image": "australia-southeast1-docker.pkg.dev/contino-squad0-fc/flight-contoller-event-receiver/event_receiver:latest",
                            "ports": [
                                {
                                    "container_port": 8080
                                }
                            ],
                        },
                    ],
                    "service_account_name": f"{cloudrun_account.email}",
                }
            },
        )

        self.bigquery_job = project_iam_member.ProjectIamMember(
            self,
            "bigquery_job",
            role="roles/bigquery.jobUser",
            member=f"serviceAccount:{cloudrun_account.email}",
            project=project_id,
        )