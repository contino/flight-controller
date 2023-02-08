from typing import Union
from src.entities.projects import ProjectLeadTime
from src.entities.compliance import ResourceComplianceLeadTime
from src.entities.patch import PatchCompliancePercentage

Metric: "TypeAlias" = Union[ProjectLeadTime, ResourceComplianceLeadTime, PatchCompliancePercentage]
