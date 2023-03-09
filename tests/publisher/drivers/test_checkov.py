from typing import Tuple

from publisher.drivers.checkov import Checkov
from publisher.entities.events import (
    GuardrailActivated,
    GuardrailPassed,
)

CHECKOV_SOURCE = Checkov()


def test_checkov_returns_correct_type():
    assert isinstance(CHECKOV_SOURCE.get_events("tests/examples/checkov.json"), Tuple)


def test_checkov_returns_guardrail_passedtype():
    assert isinstance(CHECKOV_SOURCE.get_events("tests/examples/checkov.json")[0], GuardrailPassed)


def test_checkov_returns_guardrail_activated_type():
    assert isinstance(CHECKOV_SOURCE.get_events("tests/examples/checkov.json")[2], GuardrailActivated)


def test_checkov_raises_exception_on_missing_file():
    assert isinstance(CHECKOV_SOURCE.get_events("not/a/real/file.json"), Exception)


def test_checkov_raises_exception_on_empty_file():
    assert isinstance(CHECKOV_SOURCE.get_events("tests/examples/no_results.json"), Exception)