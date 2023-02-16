from typing import Literal, Union

from src.entities.compliance import (
    ResourceFoundNonCompliant,
    ResourceFoundNonCompliantPayload,
)
from src.entities.patch import (
    PatchRunSummary,
    PatchRunSummaryPayload
)
from .projects import (
    ProjectCreated,
    ProjectCreatedPayload,
    ProjectRequestedPayload,
    ProjectRequested,
)
from src.entities.accounts import (
    AccountCreated,
    AccountCreatedPayload,
    AccountRequested,
    AccountRequestedPayload
)
from src.entities.guardrail import (
    GuardrailPassed,
    GuardrailPassedPayload,
    GuardrailActivated,
    GuardrailActivatedPayload

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

EventType: "TypeAlias" = Union[
    Literal["ProjectCreated"],
    Literal["ProjectRequested"],
    Literal["AccountCreated"],
    Literal["AccountRequested"],
    Literal["ResourceFoundNonCompliant"],
    Literal["PatchRunSummary"],
    Literal["GuardrailPassed"],
    Literal["GuardrailActivated"]
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
