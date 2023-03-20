---
name: ResourceCoverage[Metric]
version: 1
summary: |
  Calculates the percentage of applicable resources covered by backup plans
producers:
    - Flight Controller
owners:
    - josharmi
---

## <u>Details</u>

Flight Controller looks at all ResourceCovered and ResourceUncovered events for the last 24 hours and calculates the percentage of resources covered for the given container (i.e. AWS Account or GCP Project).

<NodeGraph title="Consumer / Producer Diagram" />
