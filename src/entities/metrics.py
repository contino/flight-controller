from typing import Union
from src.entities.projects import ProjectLeadTime
from src.entities.compliance import ResourceComplianceLeadTime

Metric: "TypeAlias" = Union[ProjectLeadTime, ResourceComplianceLeadTime]
