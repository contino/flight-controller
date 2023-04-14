from constructs import Construct
from cdktf_cdktf_provider_google import (
    artifact_registry_repository,
    artifact_registry_repository_iam_binding,
    service_account,
    kms_key_ring,
    kms_crypto_key,
    kms_crypto_key_iam_binding
)


class ArtifactRegistryComponent(Construct):
    def __init__(
            self, 
            scope: Construct, 
            id: str, 
            project_id: str, 
            project_number: str,
            location: str, 
            name: str,
            cloudrun_account: service_account.ServiceAccount,
            flight_controller_key_ring: kms_key_ring.KmsKeyRing):
        super().__init__(scope, id)

        registry_key = kms_crypto_key.KmsCryptoKey(
            self,
            "registry_key",
            name="flight_controller_registry_key",
            key_ring=flight_controller_key_ring.id,
            rotation_period="7776000s",
        )

        registry_key_iam = kms_crypto_key_iam_binding.KmsCryptoKeyIamBinding(
            self,
            "registry_key_iam_binding",
            crypto_key_id=registry_key.id,
            role="roles/cloudkms.cryptoKeyEncrypterDecrypter",

            members= [
                f"serviceAccount:service-{project_number}@gcp-sa-artifactregistry.iam.gserviceaccount.com"
            ]
        )

        self.registry = artifact_registry_repository.ArtifactRegistryRepository(
            self,
            "registry",
            repository_id=name,
            description="Registry to store event_receiver docker images",
            format="DOCKER",
            project=project_id,
            location=location,
            kms_key_name=registry_key.id,
            depends_on = [
                registry_key
            ]
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