import argparse
import os

from publisher.entrypoints.main import main

ARGS = argparse.Namespace()


def test_main_no_source_returns_exception():
    ARGS.source = ""
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = "event_bridge"
    assert isinstance(main(ARGS), Exception)

def test_main_no_file_returns_exception():
    ARGS.source = "open_policy_agent"
    ARGS.file = ""
    ARGS.sink = "event_bridge"
    assert isinstance(main(ARGS), Exception)

def test_main_no_sink_returns_exception():
    ARGS.source = "open_policy_agent"
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = ""
    assert isinstance(main(ARGS), Exception)

def test_main_returns_no_exception():
    ARGS.source = "open_policy_agent"
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = "event_bridge"
    assert not isinstance(main(ARGS), Exception)

def test_main_incorrect_file_returns_exception():
    ARGS.source = "open_policy_agent"
    ARGS.file = "not/a/real/file.json"
    ARGS.sink = "event_bridge"
    assert isinstance(main(ARGS), Exception)

def test_main_incorrect_file_returns_exception():
    ARGS.source = "open_policy_agent"
    ARGS.file = "not/a/real/file.json"
    ARGS.sink = "event_bridge"
    assert isinstance(main(ARGS), Exception)

def test_main_unsupported_source_returns_exception():
    ARGS.source = "not_supported"
    ARGS.file = "not/a/real/file.json"
    ARGS.sink = "event_bridge"
    assert isinstance(main(ARGS), Exception)

def test_main_unsupported_sink_returns_exception():
    ARGS.source = "open_policy_agent"
    ARGS.file = "tests/examples/opa.json"
    ARGS.sink = "not_supported"
    assert isinstance(main(ARGS), Exception)
