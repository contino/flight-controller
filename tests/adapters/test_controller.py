from datetime import datetime
import random
import string
from uuid import uuid4

from src.adapters.controller import handle_event
from src.entities.accounts import (
    AccountCreated,
    AccountLeadTime,
    AccountRequested,
    AccountRequestedPayload,
)
from src.entities.compliance import (
    ResourceComplianceLeadTime,
    ResourceFoundCompliant,
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)
from src.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivatedPayload,
    GuardrailActivationCount,
    GuardrailLeadTime,
    GuardrailMaxActivation,
    GuardrailPassed,
)
from src.entities.patch import (
    PatchCompliancePercentage,
    PatchRunSummary,
)
from src.entities.projects import (
    ProjectAssigned,
    ProjectAssignedLeadTime,
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectLeadTime,
    ProjectRequested,
    ProjectRequestedPayload,
)


aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
guardrail_id = "".join(random.choices(string.ascii_letters, k=12))
account_id = aggregate_id
event_time = int(round(datetime.utcnow().timestamp()))

def test_project_requested_returns_no_metrics():
    assert (
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "time": event_time,
                "event_type": "project_requested",
            },
            [],
        )[1]
        == []
    )


def test_project_requested_returns_correct_type():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "time": event_time,
                "event_type": "project_requested",
            },
            [],
        )[0],
        ProjectRequested,
    )


def test_project_created_returns_correct_type():
    requested_event = ProjectRequested(
        aggregate_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(aggregate_id, event_time),
    )
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "time": event_time,
                "event_type": "project_created",
            },
            [requested_event],
        )[0],
        ProjectCreated,
    )


def test_project_assigned_returns_correct_type ():
    requested_event = ProjectRequested(
        aggregate_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(aggregate_id, event_time),
    )
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "time": event_time,
                "event_type": "project_assigned",
            },
            [requested_event],
        )[0],
        ProjectAssigned,
    )


def test_project_created_returns_lead_time():
    requested_event = ProjectRequested(
        aggregate_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(aggregate_id, event_time),
    )
    assert handle_event(
        {
            "aggregate_id": aggregate_id,
            "time": event_time,
            "event_type": "project_created",
        }, 
        [requested_event]
    )[1] == [ ProjectLeadTime(aggregate_id, 0)]


def test_project_assigned_returns_lead_time():
    requested_event = ProjectRequested(
        aggregate_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(aggregate_id, event_time),
    )
    assert handle_event(
        {
            "aggregate_id": aggregate_id,
            "time": event_time,
            "event_type": "project_assigned",
        }, 
        [requested_event]
    )[1] == [ProjectAssignedLeadTime(aggregate_id, 0)]


def test_project_assigned_returns_lead_time_with_multiple_aggregates():
    requested_event = ProjectRequested(
        aggregate_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(aggregate_id, event_time),
    )

    created_event = ProjectCreated(
        aggregate_id,
        "Project",
        2,
        uuid4(),
        1,
        ProjectCreatedPayload(aggregate_id, event_time),
    )
    assert handle_event(
        {
            "aggregate_id": aggregate_id,
            "time": event_time,
            "event_type": "project_assigned",
        },
        [created_event, requested_event]
    )[1] == [ProjectAssignedLeadTime(aggregate_id, 0)]


def test_project_created_handles_no_project_requested():
    assert isinstance(handle_event(
        {
            "aggregate_id": aggregate_id,
            "time": event_time,
            "event_type": "project_created",
        },
        []
    )[0], ProjectCreated)


def test_project_assigned_handles_no_project_requested():
    assert isinstance(handle_event(
        {
            "aggregate_id": aggregate_id,
            "time": event_time,
            "event_type": "project_assigned",
        },
        []
    )[0], ProjectAssigned)


def test_project_created_returns_no_metric_with_no_project_requested():
    assert handle_event(
        {
            "aggregate_id": aggregate_id,
            "time": event_time,
            "event_type": "project_created",
        },
        []
    )[1] == []


def test_project_assigned_returns_no_metric_with_no_project_requested():
    assert handle_event(
        {
            "aggregate_id": aggregate_id,
            "time": event_time,
            "event_type": "project_assigned",
        },
        []
    )[1] == []


# Patch Summary Events
def test_patch_summary_returns_correct_type():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "time": event_time,
                "failed_instances": "i-adslkjfds,i-89dsfkjdkfj",
                "successful_instances": "i-peoritdsfl",
                "event_type": "patch_run_summary",
            },
            [],
        )[0],
        PatchRunSummary,
    )


def test_patch_summary_returns_metric():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "time": event_time,
                "failed_instances": "i-adslkjfds,i-89dsfkjdkfj",
                "successful_instances": "i-peoritdsfl",
                "event_type": "patch_run_summary",
            },
            [],
        )[1][0],
        PatchCompliancePercentage,
    )


# Compliance Events
def test_resource_non_compliant_returns_correct_type():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "container_id": "123456789012",
                "time": event_time,
                "event_type": "resource_found_non_compliant",
            },
            [],
        )[0],
        ResourceFoundNonCompliant,
    )


def test_resource_non_compliant_returns_no_metric():
    assert (
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "container_id": "123456789012",
                "time": event_time,
                "event_type": "resource_found_non_compliant",
            },
            [],
        )[1]
        == []
    )


def test_resource_compliant_returns_correct_type():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "container_id": "123456789012",
                "time": event_time,
                "event_type": "resource_found_compliant",
            },
            [],
        )[0],
        ResourceFoundCompliant,
    )


def test_resource_compliant_returns_metric():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "container_id": "123456789012",
                "time": event_time,
                "event_type": "resource_found_compliant",
            },
            [
                ResourceFoundNonCompliant(
                    aggregate_id,
                    "Resource",
                    1,
                    uuid4(),
                    1,
                    ResourceFoundNonCompliantPayload(
                        container_id="123456789012", timestamp=event_time
                    ),
                )
            ],
        )[1][0],
        ResourceComplianceLeadTime,
    )


# Account Events
def test_account_requested_returns_no_metrics():
    assert (
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "time": event_time,
                "event_type": "account_requested",
            },
            [],
        )[1]
        == []
    )


def test_account_requested_returns_correct_event():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "time": event_time,
                "event_type": "account_requested",
            },
            [],
        )[0],
        AccountRequested,
    )


def test_account_created_returns_correct_event():
    requested_event = AccountRequested(
        aggregate_id,
        "Account",
        1,
        uuid4(),
        1,
        AccountRequestedPayload(aggregate_id, event_time),
    )
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "time": event_time,
                "event_type": "account_created",
            },
            [requested_event],
        )[0],
        AccountCreated,
    )


def test_account_created_returns_lead_time():
    requested_event = AccountRequested(
        aggregate_id,
        "Account",
        1,
        uuid4(),
        1,
        AccountRequestedPayload(aggregate_id, event_time),
    )
    assert handle_event(
        {
            "aggregate_id": aggregate_id,
            "time": event_time,
            "event_type": "account_created",
        },
        [requested_event]
    )[1] == [AccountLeadTime(aggregate_id, 0)]


def test_account_created_handles_no_project_requested():
    assert isinstance(handle_event(
        {
            "aggregate_id": aggregate_id,
            "time": event_time,
            "event_type": "account_created",
        },
        []
    )[0], AccountCreated)


def test_account_created_returns_no_metric_with_no_project_requested():
    assert handle_event(
        {
            "aggregate_id": aggregate_id,
            "time": event_time,
            "event_type": "account_created",
        },
        []
    )[1] == []


# Guardrail Events
def test_guardrail_activated_returns_correct_type():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "guardrail_id": guardrail_id,
                "time": event_time,
                "event_type": "guardrail_activated",
            },
            []
        )[0],
        GuardrailActivated,
    )


def test_guardrail_activated_returns_metric():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "guardrail_id": guardrail_id,
                "time": event_time,
                "event_type": "guardrail_activated",
            },
            [
                GuardrailActivated(
                    aggregate_id,
                    "Resource",
                    1,
                    uuid4(),
                    1,
                    GuardrailActivatedPayload(
                        guardrail_id=guardrail_id, timestamp=event_time
                    ),
                )
            ]
        )[1][0],
        GuardrailActivationCount
    )

def test_guardrail_passed_returns_correct_type():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "guardrail_id": guardrail_id,
                "time": event_time,
                "event_type": "guardrail_passed",
            },
            []
        )[0],
        GuardrailPassed,
    )


def test_guardrail_passed_returns_metric_lead_time():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "guardrail_id": guardrail_id,
                "time": event_time,
                "event_type": "guardrail_passed",
            },
            [
                GuardrailActivated(
                    aggregate_id,
                    "Resource",
                    1,
                    uuid4(),
                    1,
                    GuardrailActivatedPayload(
                        guardrail_id=guardrail_id, timestamp=event_time
                    ),
                )
            ],
        )[1][0],
        GuardrailLeadTime
    )

def test_guardrail_passed_returns_metric_max_activation():
    assert isinstance(
        handle_event(
            {
                "aggregate_id": aggregate_id,
                "guardrail_id": guardrail_id,
                "time": event_time,
                "event_type": "guardrail_passed",
            },
            [
                GuardrailActivated(
                    aggregate_id,
                    "Resource",
                    1,
                    uuid4(),
                    1,
                    GuardrailActivatedPayload(
                        guardrail_id=guardrail_id, timestamp=event_time
                    ),
                )
            ],
        )[1][1],
        GuardrailMaxActivation
    )


# Unknown Events
def test_handles_unknown_event():
    assert isinstance(
        handle_event(
            {
                "requested_time": 1659656680.789246,
                "aggregate_id": "the-armitagency",
                "event_type": "NotAnEvent",
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
                "requested_time": 1659656680.789246,
                "aggregate_id": "the-armitagency",
            },
            [],
        ),
        Exception,
    )



