---
name: GuardrailActivationCount[Metric]
version: 1
summary: |
  Amount of guardrail activations.
producers:
    - Flight Controller
owners:
    - josharmi
---

## <u>Details</u>

Flight Controller looks at all previous pertinent guardrail activations for a resource and the guardrail, then gives you the total amount.

<NodeGraph title="Consumer / Producer Diagram" />
