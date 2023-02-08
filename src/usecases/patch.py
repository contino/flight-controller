from src.entities.patch import (
    PatchRunSummary,
    PatchCompliancePercentage,
)

def handle_patch_summary(
    event: PatchRunSummary
    ) -> PatchCompliancePercentage:
    return PatchCompliancePercentage(
        event.aggregateId,
        round(len(event.payload.successful_instances.split(",")) / (len(event.payload.failed_instances.split(",")) + len(event.payload.successful_instances.split(","))) * 100, 1)
    )
