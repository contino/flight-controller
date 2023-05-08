from cdktf_cdktf_provider_google import (
    cloud_run_service, 
    eventarc_trigger,
    kms_crypto_key,
    kms_crypto_key_iam_binding,
    kms_key_ring, 
    project_iam_binding,
    pubsub_topic, 
    service_account,
)
from constructs import Construct


class EventarcWithPubsubComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        project_id: str,
        project_number: str,
        location: str,
        name_prefix: str,
        cloudrun: cloud_run_service.CloudRunService,
        service_account: service_account.ServiceAccount,
        cloudrun_account: service_account.ServiceAccount,
        flight_controller_key_ring: kms_key_ring.KmsKeyRing,
    ):
        super().__init__(scope, id)

        pub_sub_topic_key = kms_crypto_key.KmsCryptoKey(
            self,
            "pub_sub_topic_key",
            name="pub_sub_topic_key",
            key_ring=flight_controller_key_ring.id,
            rotation_period="7776000s",

            lifecycle= {
                "prevent_destroy": True
            }
        )

        pub_sub_key_iam = kms_crypto_key_iam_binding.KmsCryptoKeyIamBinding(
            self,
            "pub_sub_key_iam_binding",
            crypto_key_id=pub_sub_topic_key.id,
            role="roles/cloudkms.cryptoKeyEncrypterDecrypter",
            members=[
                service_account.member,
                f"serviceAccount:service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com"
                ],
        )

        self.pubsub = pubsub_topic.PubsubTopic(
            self,
            "pubsub",
            name=name_prefix,
            project=project_id,
            kms_key_name=pub_sub_topic_key.id,
        )

        self.trigger = eventarc_trigger.EventarcTrigger(
            self,
            "event_trigger",
            name=name_prefix,
            location=location,
            project=project_id,
            matching_criteria=[
                {
                    "attribute": "type",
                    "value": "google.cloud.pubsub.topic.v1.messagePublished",
                }
            ],
            transport={
                "pubsub": {
                    "topic": self.pubsub.name,
                }
            },
            destination={
                "cloud_run_service": {
                    "service": cloudrun.name,
                    "region": cloudrun.location,
                }
            },
            service_account=service_account.email,
        )

        self.project = project_iam_binding.ProjectIamBinding(
            self,
            "cloudrun_binding",
            project=project_id,
            role="roles/eventarc.eventReceiver",
            members=[f"serviceAccount:{cloudrun_account.email}"],
        )

        self.eventarc = project_iam_binding.ProjectIamBinding(
            self,
            "eventarc_binding",
            project=project_id,
            role="roles/run.invoker",
            members=[f"serviceAccount:{service_account.email}"],
        )