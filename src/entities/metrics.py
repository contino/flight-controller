from typing import Literal, Union

from src.entities.accounts import AccountLeadTime
from src.entities.compliance import ResourceComplianceLeadTime
from src.entities.guardrail import (
    GuardrailActivationCount,
    GuardrailLeadTime,
    GuardrailMaxActivation,
)
from src.entities.identity import IdentityLeadTime
from src.entities.patch import PatchCompliancePercentage
from src.entities.projects import (
    ProjectLeadTime,
    ProjectAssignedLeadTime,
)


Metric = Union[
    ProjectAssignedLeadTime,
    ProjectLeadTime,
    ResourceComplianceLeadTime,
    AccountLeadTime,
    PatchCompliancePercentage,
    GuardrailActivationCount,
    GuardrailMaxActivation,
    GuardrailLeadTime,
    IdentityLeadTime,
]

Metric_Type = Union[
    Literal["project_assigned_lead_time"],
    Literal["project_lead_time"],
    Literal["resource_compliance_lead_time"],
    Literal["account_lead_time"],
    Literal["patch_compliance_percentage"],
    Literal["guardrail_activation_count"],
    Literal["guardrail_max_activation"],
    Literal["guardrail_lead_time"],
]

METRIC_CLASSES = {
    "project_assigned_lead_time": ProjectAssignedLeadTime,
    "project_lead_time": ProjectLeadTime,
    "resource_compliance_lead_time": ResourceComplianceLeadTime,
    "account_lead_time": AccountLeadTime,
    "patch_compliance_percentage": PatchCompliancePercentage,
    "guardrail_activation_count": GuardrailActivationCount,
    "guardrail_max_activation": GuardrailMaxActivation,
    "guardrail_lead_time": GuardrailLeadTime,
}
