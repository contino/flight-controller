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

Event: "TypeAlias" = Union[ProjectCreated, ProjectRequested, AccountCreated, AccountRequested, ResourceFoundNonCompliant, PatchRunSummary]

EventType: "TypeAlias" = Union[
    
    Literal["ProjectCreated"],
   
    Literal["ProjectRequested"],
    Literal["AccountCreated"],
    Literal["AccountRequested"]
    ,
    Literal["ResourceFoundNonCompliant"],
    Literal["PatchRunSummary"]
]

Payload: "TypeAlias" = Union[
    ProjectCreatedPayload, ProjectRequestedPayload, AccountCreatedPayload, AccountRequestedPayload, ResourceFoundNonCompliantPayload, PatchRunSummaryPayload
]
