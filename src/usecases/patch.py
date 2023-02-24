from src.entities.patch import (
    PatchCompliancePercentage,
    PatchRunSummary,
)

def handle_patch_summary(
    event: PatchRunSummary
    ) -> PatchCompliancePercentage:
    return PatchCompliancePercentage(
        event.aggregate_id,
        round(len(event.payload.successful_instances.split(",")) / (len(event.payload.failed_instances.split(",")) + len(event.payload.successful_instances.split(","))) * 100, 1)
    )
