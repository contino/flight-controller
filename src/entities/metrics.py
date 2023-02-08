from typing import Unionfrom typing import Union
from src.entities.projects import ProjectLeadTime
from src.entities.accounts import AccountAssignedLeadTime
from src.entities.compliance import ResourceComplianceLeadTime

Metric: "TypeAlias" = Union[ProjectLeadTime, ResourceComplianceLeadTime, AccountAssignedLeadTime]
