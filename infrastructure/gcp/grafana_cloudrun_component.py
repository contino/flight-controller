import subprocess

from cdktf_cdktf_provider_google import (
    cloud_run_service,
    cloud_run_service_iam_member,
)
from constructs import Construct

COMMIT = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode("utf-8")


class GrafanaComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        project_id: str,
        location: str,
        name_prefix: str,
    ):
        super().__init__(scope, id)


        # Grafana service setup
        self.service = cloud_run_service.CloudRunService(
            self,
            "grafana_service",
            name=f"{name_prefix}-grafana",
            location=location,
            autogenerate_revision_name=True,
            project=project_id,
            metadata={
                "annotations": {
                    "run.googleapis.com/ingress": "internal-and-cloud-load-balancing",
                }
            },
            template={
                "spec": {
                    "containers": [
                        {
                            "image": f"australia-southeast1-docker.pkg.dev/contino-squad0-fc/flight-controller-event-receiver/grafana:{COMMIT}",
                            "ports": [
                                {
                                    "container_port": 8080,
                                }
                            ],
                            "env": [
                                {
                                    "name": "GF_SERVER_HTTP_PORT",
                                    "value": "8080",
                                },
                            ],
                        }
                    ]
                }
            },
            traffic=[
                {
                "percent": 100,
                "latest_revision": True,      
                }
            ],
        )

        self.allowusers = cloud_run_service_iam_member.CloudRunServiceIamMember(
            self,
            "allow_contino_io",
            service=self.service.name,
            location=self.service.location,
            role="roles/run.invoker",
            project=project_id,
            member="domain:contino.io",
        )
