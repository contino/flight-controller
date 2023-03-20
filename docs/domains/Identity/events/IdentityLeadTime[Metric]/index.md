---
name: IdentityLeadTime[Metric]
version: 1
summary: |
  Tracks the time between an identity being requested and it being created
producers:
    - Flight Controller
owners:
    - josharmi
---

## <u>Details</u>

Flight Controller looks at the last pertinent identity requested event and calculates the time from it being requested to created.

<NodeGraph title="Consumer / Producer Diagram" />
