from typing import Literal, Union

from src.entities.projects import ProjectLeadTime
from src.entities.accounts import AccountLeadTime
from src.entities.compliance import ResourceComplianceLeadTime
from src.entities.patch import PatchCompliancePercentage
from src.entities.guardrail import (
    GuardrailActivationCount,
    GuardrailMaxActivation,
    GuardrailLeadTime
    )

Metric: "TypeAlias" = Union[
    ProjectLeadTime, 
    ResourceComplianceLeadTime, 
    AccountLeadTime, 
    PatchCompliancePercentage,
    GuardrailActivationCount,
    GuardrailMaxActivation,
    GuardrailLeadTime
    ]

MetricType: "TypeAlias" = Union[
    Literal["ProjectLeadTime"],
    Literal["ResourceComplianceLeadTime"],
    Literal["AccountLeadTime"],
    Literal["PatchCompliancePercentage"],
    Literal["GuardrailActivationCount"],
    Literal["GuardrailMaxActivation"],
    Literal["GuardrailLeadTime"],
    ]
