from typing import List, Optional
from src.entities.compliance import (
    ResourceComplianceLeadTime,
    ResourceFoundCompliant,
    ResourceFoundNonCompliant,
)
from src.entities.events import Event


def handle_resource_found_non_compliant(
    event: ResourceFoundNonCompliant, events: List[Event]
) -> None:
    return None


def handle_resource_found_compliant(
    event: ResourceFoundCompliant, events: List[Event]
) -> Optional[ResourceComplianceLeadTime]:
    last_compliant_event = 0
    for i, aggregate_event in enumerate(events):
        if isinstance(aggregate_event, ResourceFoundCompliant):
            last_compliant_event = i
    for aggregate_event in events[last_compliant_event:]:
        if isinstance(aggregate_event, ResourceFoundNonCompliant):
            return ResourceComplianceLeadTime(
                event.aggregateId,
                (event.payload.timestamp - aggregate_event.payload.timestamp),
            )
    return None
