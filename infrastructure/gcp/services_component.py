from cdktf_cdktf_provider_google import project_service
from constructs import Construct


class ServicesComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        project_id: str,
    ):
        super().__init__(scope, id)

        self.cloudrun = project_service.ProjectService(
            self,
            "cloudrun",
            project=project_id,
            disable_on_destroy=False,
            service="run.googleapis.com",
        )

        self.eventarc = project_service.ProjectService(
            self,
            "eventarc",
            project=project_id,
            disable_on_destroy=False,
            service="eventarc.googleapis.com",
        )

        self.pubsub = project_service.ProjectService(
            self,
            "pubsub",
            project=project_id,
            disable_on_destroy=False,
            service="pubsub.googleapis.com",
        )

        self.artifactregistry = project_service.ProjectService(
            self,
            "artifactregistry",
            project=project_id,
            disable_on_destroy=False,
            service="artifactregistry.googleapis.com",
        )

        self.bigquery = project_service.ProjectService(
            self,
            "bigquery",
            project=project_id,
            disable_on_destroy=False,
            service="bigquery.googleapis.com",
        )

        self.compute = project_service.ProjectService(
            self,
            "compute",
            project=project_id,
            disable_on_destroy=False,
            service="compute.googleapis.com",
        )
