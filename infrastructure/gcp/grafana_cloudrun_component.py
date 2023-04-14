from constructs import Construct
from cdktf_cdktf_provider_google import (
    cloud_run_service,
    cloud_run_service_iam_member,
    service_account,
)


class GrafanaComponent(Construct):
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
            "grafana_service",
            name=name,
            location=location,
            project=project_id,
            metadata={
                "annotations": 
                {
                    "run.googleapis.com/ingress" : "internal-and-cloud-load-balancing",
                }
            },
            template={
                "spec": {
                    "containers": [
                        {
                            "image": "mirror.gcr.io/grafana/grafana:latest",
                            "ports": [
                                {
                                    "container_port": 8080,
                                }
                            ],
                            "env": [
                                {
                                    "name": "GF_SERVER_HTTP_PORT",
                                    "value": "8080",
                                }
                            ],
                        }
                    ]
                }
            },
        )

        self.allowusers = cloud_run_service_iam_member.CloudRunServiceIamMember(
            self,
            "allow_contino_io",
            service=self.service.name,
            location=self.service.location,
            role="roles/run.invoker",
            project=project_id,
            member="domain:contino.io"
        )
