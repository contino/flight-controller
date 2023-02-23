from typing import Any, Dict, List, Tuple, Union
from uuid import uuid4

from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountRequested,
    AccountRequestedPayload,
)
from src.entities.compliance import (
    ResourceFoundCompliant,
    ResourceFoundCompliantPayload,
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)
from src.entities.events import Event, Event_Type
from src.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivatedPayload,
    GuardrailPassed,
    GuardrailPassedPayload,
)
from src.entities.identity import (
    IdentityCreated,
    IdentityCreatedPayload,
    IdentityRequested,
    IdentityRequestedPayload,
)
from src.entities.metrics import Metric
from src.entities.patch import PatchRunSummary, PatchRunSummaryPayload
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
)
from src.usecases.accounts import handle_account_created
from src.usecases.compliance import handle_resource_found_compliant
from src.usecases.guardrail import handle_guardrail_activated, handle_guardrail_passed
from src.usecases.identity import handle_identity_created
from src.usecases.patch import handle_patch_summary
from src.usecases.projects import handle_project_created


def _convert_payload_to_event(
    payload: Dict[str, Any], event_type: Event_Type, aggregate_version: int
) -> Event:
    if event_type == "project_requested":
        return ProjectRequested(
            aggregate_id=payload["aggregate_id"],
            aggregate_type="Project",
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=ProjectRequestedPayload(
                payload["aggregate_id"], int(payload["time"])
            ),
        )
    elif event_type == "project_created":
        return ProjectCreated(
            aggregate_id=payload["aggregate_id"],
            aggregate_type="Project",
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=ProjectCreatedPayload(
                payload["aggregate_id"], int(payload["time"])
            ),
        )
    elif event_type == "resource_found_non_compliant":
        return ResourceFoundNonCompliant(
            aggregate_id=payload["aggregate_id"],
            aggregate_type="Resource",
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=ResourceFoundNonCompliantPayload(
                payload["container_id"], int(payload["time"])
            ),
        )
    elif event_type == "resource_found_compliant":
        return ResourceFoundCompliant(
            aggregate_id=payload["aggregate_id"],
            aggregate_type="Resource",
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=ResourceFoundCompliantPayload(
                payload["container_id"], int(payload["time"])
            ),
        )
    elif event_type == "patch_run_summary":
        return PatchRunSummary(
            aggregate_id=payload["aggregate_id"],
            aggregate_type="Account",
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=PatchRunSummaryPayload(
                payload["failed_instances"], payload["successful_instances"]
            ),
        )
    elif event_type == "account_requested":
        return AccountRequested(
            aggregate_id=payload["aggregate_id"],
            aggregate_type="Account",
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=AccountRequestedPayload(
                payload["aggregate_id"], int(payload["time"])
            ),
        )
    elif event_type == "account_created":
        return AccountCreated(
            aggregate_id=payload["aggregate_id"],
            aggregate_type="Account",
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=AccountCreatedPayload(
                payload["aggregate_id"], int(payload["time"])
            ),
        )
    elif event_type == "guardrail_passed":
        return GuardrailPassed(
            aggregate_id=payload["aggregate_id"],
            aggregate_type="Resource",
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=GuardrailPassedPayload(
                payload["guardrail_id"], int(payload["time"])
            ),
        )
    elif event_type == "guardrail_activated":
        return GuardrailActivated(
            aggregate_id=payload["aggregate_id"],
            aggregate_type="Resource",
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=GuardrailActivatedPayload(
                payload["guardrail_id"], int(payload["time"])
            ),
        )
    elif event_type == "identity_requested":
        return IdentityRequested(
            aggregate_id=payload["aggregate_id"],
            aggregate_type="Account",
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=IdentityRequestedPayload(
                payload["aggregate_id"], int(payload["time"])
            ),
        )
    elif event_type == "identity_created":
        return IdentityCreated(
            aggregate_id=payload["aggregate_id"],
            aggregate_type="Account",
            aggregate_version=aggregate_version + 1,
            event_id=str(uuid4()),
            event_version=1,
            payload=IdentityCreatedPayload(
                payload["aggregate_id"], int(payload["time"])
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
            "project_created",
            "project_assigned",
            "account_created",
            "account_requested",
            "identity_created",
            "identity_requested",
            "resource_found_non_compliant",
        ]:
            metrics = []
            for aggregate_event in aggregate_events:
                if payload["event_type"] == "project_created" and isinstance(
                    aggregate_event, ProjectRequested
                ):
                    metrics.append(handle_project_created(aggregate_event, event))
                elif payload["event_type"] == "account_created" and isinstance(
                    aggregate_event, AccountRequested
                ):
                    metrics.append(handle_account_created(aggregate_event, event))
                elif payload["event_type"] == "identity_created" and isinstance(
                    aggregate_event, IdentityRequested
                ):
                    metrics.append(handle_identity_created(aggregate_event, event))
            return (event, metrics)
        elif payload["event_type"] in ["resource_found_compliant"]:
            return (event, [handle_resource_found_compliant(event, aggregate_events)])
        elif payload["event_type"] in ["patch_run_summary"]:
            return (event, [handle_patch_summary(event)])
        elif payload["event_type"] in ["guardrail_passed"]:
            return (event, handle_guardrail_passed(event, aggregate_events))
        elif payload["event_type"] in ["guardrail_activated"]:
            return (event, [handle_guardrail_activated(event, aggregate_events)])
        else:
            return Exception(f"Unknown Event type {payload['event_type']}")
    return Exception("Malformed event with no event_type")
