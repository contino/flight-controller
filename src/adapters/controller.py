from typing import Any, Dict, List, Tuple, Union
from uuid import uuid4
from src.entities.compliance import (
    ResourceFoundCompliant,
    ResourceFoundCompliantPayload,
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)


from src.entities.events import Event, EventType
from src.entities.metrics import Metric
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectAssigned,
    ProjectAssignedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
)

from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountAssigned,
    AccountAssignedPayload,
    AccountRequested,
    AccountRequestedPayload,
)
from src.usecases.compliance import handle_resource_found_compliant

from src.usecases.projects import handle_project_created, handle_project_assigned
from src.usecases.accounts import handle_account_created, handle_account_assigned


def _convert_payload_to_event(
    payload: Dict[str, Any], event_type: EventType, aggregateVersion: int
) -> Event:
    if event_type == "ProjectRequested":
        return ProjectRequested(
            aggregateId=payload["aggregate_id"],
            aggregateType="Project",
            aggregateVersion=aggregateVersion + 1,
            eventId=str(uuid4()),
            eventVersion=1,
            payload=ProjectRequestedPayload(
                payload["aggregate_id"], int(payload["time"])
            ),
        )
    elif event_type == "ProjectAssigned":
        return ProjectAssigned(
            aggregateId=payload["aggregate_id"],
            aggregateType="Project",
            aggregateVersion=aggregateVersion + 1,
            eventId=str(uuid4()),
            eventVersion=1,
            payload=ProjectAssignedPayload(
                payload["aggregate_id"], int(payload["time"])
            ),
        )
    elif event_type == "ProjectCreated":
        return ProjectCreated(
            aggregateId=payload["aggregate_id"],
            aggregateType="Project",
            aggregateVersion=aggregateVersion + 1,
            eventId=str(uuid4()),
            eventVersion=1,
            payload=ProjectCreatedPayload(
                payload["aggregate_id"], int(payload["time"])
            ),
        )
    elif event_type == "ResourceFoundNonCompliant":
        return ResourceFoundNonCompliant(
            aggregateId=payload["aggregate_id"],
            aggregateType="Resource",
            aggregateVersion=aggregateVersion + 1,
            eventId=str(uuid4()),
            eventVersion=1,
            payload=ResourceFoundNonCompliantPayload(
                payload["container_id"], int(payload["time"])
            ),
        )
    elif event_type == "ResourceFoundCompliant":
        return ResourceFoundCompliant(
            aggregateId=payload["aggregate_id"],
            aggregateType="Resource",
            aggregateVersion=aggregateVersion + 1,
            eventId=str(uuid4()),
            eventVersion=1,
            payload=ResourceFoundCompliantPayload(
                payload["container_id"], int(payload["time"])
            ),
        )
    elif event_type == "AccountRequested":
        return AccountRequested(
            aggregateId=payload["aggregate_id"],
            aggregateType="Account",
            aggregateVersion=aggregateVersion + 1,
            eventId=str(uuid4()),
            eventVersion=1,
            payload=AccountRequestedPayload(
                payload["aggregate_id"],
                int(payload["time"])
            ),
        )
    elif event_type == "AccountAssigned":
        return AccountAssigned(
            aggregateId=payload["aggregate_id"],
            aggregateType="Account",
            aggregateVersion=aggregateVersion + 1,
            eventId=str(uuid4()),
            eventVersion=1,
            payload=AccountAssignedPayload(
                payload["aggregate_id"],
                int(payload["time"])
            ),
        )
    elif event_type == "AccountCreated":
        return AccountCreated(
            aggregateId=payload["aggregate_id"],
            aggregateType="Account",
            aggregateVersion=aggregateVersion + 1,
            eventId=str(uuid4()),
            eventVersion=1,
            payload=AccountCreatedPayload(
                payload["aggregate_id"],
                int(payload["time"])
            ),
        )

def handle_event(
    payload: Any, aggregate_events: List[Event]
) -> Union[Exception, Tuple[Event, List[Metric]]]:
    if "event_type" in payload:
        event = _convert_payload_to_event(
            payload, payload["event_type"], len(aggregate_events)
        )
        if isinstance(event, ProjectRequested):
            return (event, [])
        elif payload["event_type"] in [
            "ProjectCreated",
            "ProjectAssigned",
            "AccountCreated",
            "AccountAssigned",
            "ResourceFoundNonCompliant",
        ]:
            metrics = []
            for aggregate_event in aggregate_events:
                if payload["event_type"] == "ProjectCreated" and isinstance(
                    aggregate_event, ProjectRequested
                ):
                    metrics.append(handle_project_created(aggregate_event, event))
                elif payload["event_type"] == "ProjectAssigned" and isinstance(
                    aggregate_event, ProjectRequested
                ):
                    metrics.append(handle_project_assigned(aggregate_event, event))
                elif payload["event_type"] == "AccountCreated" and isinstance(aggregate_event, AccountRequested):
                    metrics.append(handle_account_created(aggregate_event, event))
                elif payload["event_type"] == "AccountAssigned" and isinstance(aggregate_event, AccountRequested):
                    metrics.append(handle_account_assigned(aggregate_event, event))
            return (event, metrics)
        elif payload["event_type"] in ["ResourceFoundCompliant"]:
            return (event, [handle_resource_found_compliant(event, aggregate_events)])
        else:
            return Exception(f"Unknown Event type {payload['event_type']}")
    return Exception("Malformed event with no event_type")
