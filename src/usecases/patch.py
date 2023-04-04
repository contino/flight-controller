from typing import List, Tuple

from src.entities.events import Event
from src.entities.patch import (
    PatchRunSummary,
    PatchCompliancePercentage,
)


def handle_patch_summary(
    event: Event, aggregate_events: List[Event]
) -> Tuple[PatchRunSummary, List[PatchCompliancePercentage]]:
    return (
        event,
        [
            PatchCompliancePercentage(
                aggregate_id=event.aggregate_id,
                metric_value=round(
                    len(event.payload.successful_instances.split(","))
                    / (
                        len(event.payload.failed_instances.split(","))
                        + len(event.payload.successful_instances.split(","))
                    )
                    * 100,
                    1,
                ),
            )
        ],
    )
