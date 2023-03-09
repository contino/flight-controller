from constructs import Construct
from cdktf_cdktf_provider_google import (
    pubsub_topic, 
    eventarc_trigger,
    cloud_run_service,
    service_account,
    project_iam_binding,
)

class EventarcWithPubsubComponent(Construct):
    def __init__(
            self, 
            scope: Construct, 
            id: str, 
            project_id: str, 
            location: str, 
            name: str,
            cloudRun: cloud_run_service.CloudRunService,
            service_account: service_account.ServiceAccount,
            cloudrun_account: service_account.ServiceAccount
    ):
        super().__init__(scope, id)

        self.pubsub = pubsub_topic.PubsubTopic(
            self,
            "pubsub",
            name=name,
            project=project_id,
        )
        
        self.trigger = eventarc_trigger.EventarcTrigger(
            self,
            "event_trigger",
            name=name,
            location=location,
            project=project_id,
            matching_criteria=[{
                "attribute": "type",
                "value": "google.cloud.pubsub.topic.v1.messagePublished"
            }],
            transport={
                "pubsub": 
                    {
                        "topic": self.pubsub.name,
                    }
                
            },
            destination = { 
                "cloud_run_service": 
                    {
                        "service": cloudRun.name,
                        "region": cloudRun.location,
                    }
            },
            service_account=service_account.email,
        )

        self.project = project_iam_binding.ProjectIamBinding(
            self,
            "cloudrun_binding",
            project=project_id,
            role="roles/eventarc.eventReceiver",
            members=[f"serviceAccount:{cloudrun_account.email}"]
        )