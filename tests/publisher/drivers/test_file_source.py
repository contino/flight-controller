from typing import Dict

from publisher.drivers.file_source import FileSource

file_source = FileSource()

def test_file_source_returns_correct_type():
    assert isinstance(file_source.read_file("tests/examples/opa.json"), Dict)

def test_file_source_file_not_found_returns_exception():
    assert isinstance(file_source.read_file("Not/a/real/file.json"), FileNotFoundError)

def test_file_source_empty_file_returns_exception():
    assert isinstance(file_source.read_file("tests/examples/empty.json"), Exception)