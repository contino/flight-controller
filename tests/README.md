<h1 align="center">Flight Controller - Testing</h1>
<p align="center">Everything related to testing Flight Controller</p>

## Tests

- Flight Controller Custom Publisher Examples `examples/`
- Python Behave Tests (e2e Testing) `features/`
- Pytest Publisher Tests `publisher/`
- Pytest Controller Tests `src/`

## Make Commands

Testing is split into four commands:

- `make unittest` runs all the unit tests (i.e. tests that are not [marked as integration](https://docs.pytest.org/en/7.1.x/example/markers.html)).
- `make integration-test` run all the integration tests.
- `make test` runs all the tests and reports on coverage.
- `make e2e` runs the end to end BDD tests using [behave](https://github.com/behave/behave).
- `make watch` runs all the unit tests on file change. Allowing to test code while making live changes.

## Coverage
