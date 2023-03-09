from time import time
from uuid import uuid4

from src.adapters.controller import handle_event
from src.entities.accounts import (
    AccountCreated,
    AccountRequested,
)
from src.entities.compliance import (
    ResourceFoundCompliant,
    ResourceFoundNonCompliant,
)
from src.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivatedPayload,
    GuardrailPassed,
    GuardrailLeadTime,
)
from src.entities.patch import PatchRunSummary, PatchCompliancePercentage
from src.entities.projects import (
    ProjectAssigned,
    ProjectCreated,
    ProjectRequested,
)

EVENT_ID = str(uuid4())
AGGREGATE_ID = str(uuid4())
ALTERNATE_ID = str(uuid4())
CURRENT_TIME = int(time())

patch_run_summary_event = {
    "event_type": "patch_run_summary",
    "aggregate_id": f"{AGGREGATE_ID}",
    "time": f"{CURRENT_TIME}",
    "failed_instances": "i-adslkjfds,i-89dsfkjdkfj",
    "successful_instances": "i-peoritdsfl",
}

guardrail_activated_aggregate_event = GuardrailActivated(
    aggregate_id=AGGREGATE_ID,
    event_id=EVENT_ID,
    event_type="guardrail_activated",
    aggregate_version=1,
    payload=GuardrailActivatedPayload(
        guardrail_id=ALTERNATE_ID, timestamp=CURRENT_TIME
    ),
)

guardrail_activated_event = {
    "event_type": "guardrail_activated",
    "aggregate_id": guardrail_activated_aggregate_event.aggregate_id,
    "guardrail_id": guardrail_activated_aggregate_event.payload.guardrail_id,
    "time": CURRENT_TIME,
}

guardrail_passed_event = {
    "event_type": "guardrail_passed",
    "aggregate_id": guardrail_activated_aggregate_event.aggregate_id,
    "guardrail_id": guardrail_activated_aggregate_event.payload.guardrail_id,
    "time": int(guardrail_activated_aggregate_event.payload.timestamp + 10),
}

resource_found_non_compliant = {
    "event_type": "resource_found_non_compliant",
    "container_id": f"{ALTERNATE_ID}",
    "aggregate_id": f"{AGGREGATE_ID}",
    "time": f"{CURRENT_TIME}",
}

resource_found_compliant = {
    "event_type": "resource_found_compliant",
    "container_id": f"{ALTERNATE_ID}",
    "aggregate_id": f"{AGGREGATE_ID}",
    "time": f"{CURRENT_TIME}",
}

account_requested = {
    "event_type": "account_requested",
    "aggregate_id": f"{AGGREGATE_ID}",
    "time": f"{CURRENT_TIME}",
}

account_created = {
    "event_type": "account_created",
    "aggregate_id": f"{AGGREGATE_ID}",
    "time": f"{CURRENT_TIME}",
}

project_requested = {
    "event_type": "project_requested",
    "aggregate_id": f"{AGGREGATE_ID}",
    "time": f"{CURRENT_TIME}",
}

project_assigned = {
    "event_type": "project_assigned",
    "aggregate_id": f"{AGGREGATE_ID}",
    "time": f"{CURRENT_TIME}",
}

project_created = {
    "event_type": "project_created",
    "aggregate_id": f"{AGGREGATE_ID}",
    "time": f"{CURRENT_TIME}",
}


def test_handles_event_with_no_aggregate_events_returns_correct_payload_type():
    assert isinstance(handle_event(patch_run_summary_event, [])[0], PatchRunSummary)


def test_handles_event_with_no_aggregate_events_returns_correct_metric_type():
    assert isinstance(
        handle_event(patch_run_summary_event, [])[1][0], PatchCompliancePercentage
    )


def test_handles_event_with_aggregate_events_returns_correct_payload_type():
    assert isinstance(
        handle_event(guardrail_passed_event, [guardrail_activated_aggregate_event])[0],
        GuardrailPassed,
    )


def test_handles_event_with_aggregate_events_returns_correct_metric_type():
    assert isinstance(
        handle_event(guardrail_passed_event, [guardrail_activated_aggregate_event])[1][
            0
        ],
        GuardrailLeadTime,
    )


def test_handles_event_with_aggregate_events_returns_multiple_metrics():
    assert (
        len(
            handle_event(guardrail_passed_event, [guardrail_activated_aggregate_event])[
                1
            ]
        )
        == 2
    )


def test_handles_event_guardrail_activated():
    assert isinstance(
        handle_event(guardrail_activated_event, [])[0], GuardrailActivated
    )


def test_handles_event_resource_found_non_compliant():
    assert isinstance(
        handle_event(resource_found_non_compliant, [])[0], ResourceFoundNonCompliant
    )


def test_handles_event_resource_found_compliant():
    assert isinstance(
        handle_event(resource_found_compliant, [])[0], ResourceFoundCompliant
    )


def test_handles_event_account_requested():
    assert isinstance(handle_event(account_requested, [])[0], AccountRequested)


def test_handles_event_account_created():
    assert isinstance(handle_event(account_created, [])[0], AccountCreated)


def test_handles_event_project_requested():
    assert isinstance(handle_event(project_requested, [])[0], ProjectRequested)


def test_handles_event_project_assigned():
    assert isinstance(handle_event(project_assigned, [])[0], ProjectAssigned)


def test_handles_event_project_created():
    assert isinstance(handle_event(project_created, [])[0], ProjectCreated)


# Unknown Events
def test_handles_unknown_event():
    assert isinstance(
        handle_event(
            {
                "event_type": "not_an_event",
                "container_id": "123456789012",
                "aggregate_id": "the-armitagency",
            },
            [],
        ),
        Exception,
    )


# Malformed Events
def test_handles_malformed_event():
    assert isinstance(
        handle_event(
            {
                "CURRENT_TIME": CURRENT_TIME,
                "aggregate_id": "the-armitagency",
            },
            [],
        ),
        Exception,
    )
