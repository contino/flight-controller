from typing import List, Tuple

from src.entities.compliance import (
    ResourceComplianceExtraDimensions,
    ResourceComplianceLeadTime,
    ResourceFoundCompliant,
    ResourceFoundNonCompliant,
)
from src.entities.events import Event


def handle_resource_found_non_compliant(
    event: Event, aggregate_events: List[Event]
) -> Tuple[ResourceFoundNonCompliant, List]:
    return (event, [])


def handle_resource_found_compliant(
    event: Event, aggregate_events: List[Event]
) -> Tuple[ResourceFoundCompliant, List[ResourceComplianceLeadTime]]:
    last_compliant_event = 0
    for i, aggregate_event in enumerate(aggregate_events):
        if isinstance(aggregate_event, ResourceFoundCompliant):
            last_compliant_event = i
    for aggregate_event in aggregate_events[last_compliant_event:]:
        if isinstance(aggregate_event, ResourceFoundNonCompliant):
            return (
                event,
                [
                    ResourceComplianceLeadTime(
                        aggregate_id=event.aggregate_id,
                        dimensions=ResourceComplianceExtraDimensions(
                            dimension_names=["container_id"],
                            container_id=event.payload.container_id,
                        ),
                        metric_value=(
                            event.payload.timestamp - aggregate_event.payload.timestamp
                        ),
                    )
                ],
            )
    return (event, [])
