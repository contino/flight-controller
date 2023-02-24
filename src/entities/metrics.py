from typing import Literal, Union

from src.entities.accounts import AccountLeadTime
from src.entities.compliance import ResourceComplianceLeadTime
from src.entities.guardrail import (
    GuardrailActivationCount,
    GuardrailLeadTime,
    GuardrailMaxActivation,
    )
from src.entities.patch import PatchCompliancePercentage
from src.entities.projects import ProjectLeadTime


Metric: "TypeAlias" = Union[
    ProjectLeadTime, 
    ResourceComplianceLeadTime, 
    AccountLeadTime, 
    PatchCompliancePercentage,
    GuardrailActivationCount,
    GuardrailMaxActivation,
    GuardrailLeadTime
    ]

Metric_Type: "TypeAlias" = Union[
    Literal["project_lead_time"],
    Literal["resource_compliance_lead_time"],
    Literal["account_lead_time"],
    Literal["patch_compliance_percentage"],
    Literal["guardrail_activation_count"],
    Literal["guardrail_max_activation"],
    Literal["guardrail_lead_time"],
    ]
