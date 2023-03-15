from typing import Dict

from publisher.drivers.file_source import FileSource

file_source = FileSource()


def test_file_source_returns_correct_type():
    assert isinstance(file_source.read_file("tests/examples/opa.json"), Dict)

def test_file_source_returns_exception_when_file_not_found():
    assert isinstance(file_source.read_file("Not/a/real/file.json"), FileNotFoundError)

def test_file_source_returns_exception_when_file_empty():
    assert isinstance(file_source.read_file("tests/examples/empty.json"), Exception)
