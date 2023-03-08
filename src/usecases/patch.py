from typing import Dict, List, Tuple
from uuid import uuid4

from src.entities.events import Event
from src.entities.patch import (
    PatchRunSummary,
    PatchRunSummaryPayload,
    PatchCompliancePercentage,
)


def _convert_payload_to_event(event: Dict, aggregate_version: int) -> PatchRunSummary:
    return PatchRunSummary(
        aggregate_id=event["aggregate_id"],
        aggregate_version=aggregate_version + 1,
        event_id=str(uuid4()),
        payload=PatchRunSummaryPayload(
            failed_instances=event["failed_instances"],
            successful_instances=event["successful_instances"],
        ),
    )


def handle_patch_summary(
    event: Dict, aggregate_events: List[Event]
) -> Tuple[PatchRunSummary, List[PatchCompliancePercentage]]:
    event = _convert_payload_to_event(event, len(aggregate_events))
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
