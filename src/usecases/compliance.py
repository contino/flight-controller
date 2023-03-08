from typing import List, Dict, Union, Tuple
from uuid import uuid4

from src.entities.compliance import (
    ResourceComplianceExtraDimensions,
    ResourceComplianceLeadTime,
    ResourceFoundCompliant,
    ResourceFoundCompliantPayload,
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)
from src.entities.events import Event


def _convert_payload_to_event(
    event: Dict, aggregate_version: int
) -> Union[ResourceFoundCompliant, ResourceFoundNonCompliant]:
    if event["event_type"] == "resource_found_non_compliant":
        return ResourceFoundNonCompliant(
            aggregate_id=event["aggregate_id"],
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=ResourceFoundNonCompliantPayload(
                container_id=event["container_id"],
                timestamp=int(event["time"]),
            ),
        )
    elif event["event_type"] == "resource_found_compliant":
        return ResourceFoundCompliant(
            aggregate_id=event["aggregate_id"],
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=ResourceFoundCompliantPayload(
                container_id=event["container_id"],
                timestamp=int(event["time"]),
            ),
        )


def handle_resource_found_non_compliant(
    event: Dict, aggregate_events: List[Event]
) -> Tuple[ResourceFoundNonCompliant, List]:
    event = _convert_payload_to_event(event, len(aggregate_events))
    return (event, [])


def handle_resource_found_compliant(
    event: Dict, aggregate_events: List[Event]
) -> Tuple[ResourceFoundCompliant, List[ResourceComplianceLeadTime]]:
    event = _convert_payload_to_event(event, len(aggregate_events))
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
