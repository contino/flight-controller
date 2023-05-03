import argparse
from unittest.mock import patch

import pytest

from publisher.entrypoints.main import main
from publisher.drivers.sink import EventBridge
from publisher.drivers.source import OpenPolicyAgent

ARGS = argparse.Namespace()

@pytest.mark.aws
@pytest.mark.integration
def test_main_returns_no_exception():
    ARGS.source = "open_policy_agent"
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = "event_bridge"
    assert not isinstance(main(ARGS), Exception)


def test_main_returns_exception_when_no_source():
    ARGS.source = ""
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = "event_bridge"
    assert isinstance(main(ARGS), Exception)


def test_main_returns_exception_when_no_file():
    ARGS.source = "open_policy_agent"
    ARGS.file = ""
    ARGS.sink = "event_bridge"
    assert isinstance(main(ARGS), Exception)


def test_main_returns_exception_when_no_sink():
    ARGS.source = "open_policy_agent"
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = ""
    assert isinstance(main(ARGS), Exception)


def test_main_returns_exception_when_unsupported_source():
    ARGS.source = "not_supported"
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = "event_bridge"
    assert isinstance(main(ARGS), Exception)


def test_main_returns_exception_unsupported_sink():
    ARGS.source = "open_policy_agent"
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = "not_supported"
    assert isinstance(main(ARGS), Exception)


@patch("publisher.drivers.file_source.FileSource.read_file")
def test_main_returns_exception_when_file_source_returns_exception(mock_read_file):
    ARGS.source = "open_policy_agent"
    ARGS.file = "not/a/real/file.json"
    ARGS.sink = "event_bridge"
    mock_read_file.return_value = Exception()
    assert isinstance(main(ARGS), Exception)


@patch("publisher.drivers.git.Git.get_repo_name")
def test_main_returns_exception_when_git_returns_exception(mock_get_repo_name):
    ARGS.source = "open_policy_agent"
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = "event_bridge"
    mock_get_repo_name.return_value = Exception()
    assert isinstance(main(ARGS), Exception)


@patch.object(OpenPolicyAgent, "get_events")
def test_main_returns_exception_when_source_returns_exception(mock_get_events):
    ARGS.source = "open_policy_agent"
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = "event_bridge"
    mock_get_events.return_value = Exception()
    assert isinstance(main(ARGS), Exception)

@pytest.mark.aws
@pytest.mark.integration
@patch.object(EventBridge, "send_events")
def test_main_returns_exception_when_sink_returns_exception(mock_send_events):
    ARGS.source = "open_policy_agent"
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = "event_bridge"
    mock_send_events.return_value = Exception()
    assert isinstance(main(ARGS), Exception)
