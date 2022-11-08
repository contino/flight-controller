COMMIT_SHA = $(shell git rev-parse HEAD)

local:
	pipenv install --dev
	pipenv shell
	terraform init

unittest:
	pytest -m 'not integration' tests/

integration-test:
	pytest -m 'integration' tests/

test:
	pytest --cov=src --cov-fail-under=50 --cov-report term-missing tests/
