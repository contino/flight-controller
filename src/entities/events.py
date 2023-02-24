from typing import Literal, Union

from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountRequested,
    AccountRequestedPayload
)
from src.entities.compliance import (
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)
from src.entities.guardrail import (
    GuardrailActivated,
    GuardrailActivatedPayload,
    GuardrailPassed,
    GuardrailPassedPayload,

)
from src.entities.patch import (
    PatchRunSummary,
    PatchRunSummaryPayload
)
from src.entities.projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequestedPayload,
    ProjectRequested,
)


Event: "TypeAlias" = Union[
    ProjectCreated, 
    ProjectRequested, 
    AccountCreated, 
    AccountRequested, 
    ResourceFoundNonCompliant, 
    PatchRunSummary, 
    GuardrailPassed,
    GuardrailActivated
    ]

Event_Type: "TypeAlias" = Union[
    Literal["project_created"],
    Literal["project_requested"],
    Literal["account_created"],
    Literal["account_requested"],
    Literal["resource_found_non_compliant"],
    Literal["patch_run_summary"],
    Literal["guardrail_passed"],
    Literal["guardrail_activated"]
]

Payload: "TypeAlias" = Union[
    ProjectCreatedPayload, 
    ProjectRequestedPayload, 
    AccountCreatedPayload, 
    AccountRequestedPayload, 
    ResourceFoundNonCompliantPayload, 
    PatchRunSummaryPayload, 
    GuardrailPassedPayload,
    GuardrailActivatedPayload
]
