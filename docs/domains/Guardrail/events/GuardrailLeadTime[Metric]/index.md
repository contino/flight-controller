---
name: GuardrailLeadTime[Metric]
version: 1
summary: |
  Leadtime from guardrail activation to pass.
producers:
    - Flight Controller
owners:
    - josharmi
---

## <u>Details</u>

Flight Controller looks at all previous pertinent guardrail activations for a resource and the guardrail, then calculates the time it took to resolve.

<NodeGraph title="Consumer / Producer Diagram" />
