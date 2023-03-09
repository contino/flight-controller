from typing import Tuple

from publisher.drivers.open_policy_agent import OpenPolicyAgent
from publisher.entities.events import (
    GuardrailActivated,
    GuardrailPassed,
)

OPA_SOURCE = OpenPolicyAgent()


def test_open_policy_agent_returns_correct_type():
    assert isinstance(OPA_SOURCE.get_events("tests/examples/opa.json"), Tuple)


def test_open_policy_agent_returns_guardrail_passedtype():
    assert isinstance(OPA_SOURCE.get_events("tests/examples/opa.json")[0], GuardrailPassed)


def test_open_policy_agent_returns_guardrail_activated_type():
    assert isinstance(OPA_SOURCE.get_events("tests/examples/opa.json")[1], GuardrailActivated)


def test_checkov_raises_exception_on_missing_file():
    assert isinstance(OPA_SOURCE.get_events("not/a/real/file.json"), Exception)


def test_checkov_raises_exception_on_empty_file():
    assert isinstance(OPA_SOURCE.get_events("tests/examples/no_results.json"), Exception)