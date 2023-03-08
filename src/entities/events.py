from typing import Literal, Union

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
from src.entities.patch import PatchRunSummary, PatchRunSummaryPayload
from src.entities.projects import (
    ProjectAssigned,
    ProjectAssignedPayload,
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
)

Event = Union[
    ProjectAssigned,
    ProjectCreated,
    ProjectRequested,
    AccountCreated,
    AccountRequested,
    ResourceFoundCompliant,
    ResourceFoundNonCompliant,
    PatchRunSummary,
    GuardrailPassed,
    GuardrailActivated,
]

Event_Type = Union[
    Literal["project_assigned"],
    Literal["project_created"],
    Literal["project_requested"],
    Literal["account_created"],
    Literal["account_requested"],
    Literal["resource_found_compliant"],
    Literal["resource_found_non_compliant"],
    Literal["patch_run_summary"],
    Literal["guardrail_passed"],
    Literal["guardrail_activated"],
    Literal["identity_requested"],
    Literal["identity_created"],
]

Payload = Union[
    ProjectAssigned,
    ProjectCreatedPayload,
    ProjectRequestedPayload,
    AccountCreatedPayload,
    AccountRequestedPayload,
    ResourceFoundCompliant,
    ResourceFoundNonCompliantPayload,
    PatchRunSummaryPayload,
    GuardrailPassedPayload,
    GuardrailActivatedPayload,
    IdentityCreatedPayload,
    IdentityRequestedPayload,
]

EVENT_CLASSES = {
    "project_requested": (ProjectRequested, ProjectRequestedPayload),
    "project_assigned": (ProjectAssigned, ProjectAssignedPayload),
    "project_created": (ProjectCreated, ProjectCreatedPayload),
    "resource_found_compliant": (ResourceFoundCompliant, ResourceFoundCompliantPayload),
    "resource_found_non_compliant": (
        ResourceFoundNonCompliant,
        ResourceFoundNonCompliantPayload,
    ),
    "patch_run_summary": (PatchRunSummary, PatchRunSummaryPayload),
    "account_requested": (AccountRequested, AccountRequestedPayload),
    "account_created": (AccountCreated, AccountCreatedPayload),
    "guardrail_passed": (GuardrailPassed, GuardrailPassedPayload),
    "guardrail_activated": (GuardrailActivated, GuardrailActivatedPayload),
    "identity_created": (IdentityCreated, IdentityCreatedPayload),
    "identity_requested": (IdentityRequested, IdentityRequestedPayload),
}
