from constructs import Construct
from cdktf_cdktf_provider_google import (
    artifact_registry_repository,
    artifact_registry_repository_iam_binding,
    service_account,
)


class ArtifactRegistryComponent(Construct):
    def __init__(
            self, 
            scope: Construct, 
            id: str, 
            project_id: str, 
            location: str, 
            name: str,
            cloudrun_account: service_account.ServiceAccount):
        super().__init__(scope, id)

        self.registry = artifact_registry_repository.ArtifactRegistryRepository(
            self,
            "registry",
            repository_id=name,
            description="Registry to store event_receiver docker images",
            format="DOCKER",
            project=project_id,
            location=location,
        )

        self.adminbinding = artifact_registry_repository_iam_binding.ArtifactRegistryRepositoryIamBinding(
            self,
            "admin",
            repository=self.registry.id,
            role="roles/artifactregistry.repoAdmin",
            members=[
            "domain:contino.io",
            ]
        )

        self.readerbinding = artifact_registry_repository_iam_binding.ArtifactRegistryRepositoryIamBinding(
            self,
            "reader",
            repository=self.registry.id,
            role="roles/artifactregistry.reader",
            members=[
            f"serviceAccount:{cloudrun_account.email}"
            ]
        )