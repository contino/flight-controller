COMMIT_SHA = $(shell git rev-parse HEAD)

local:
	pipenv install --dev
	pipenv shell
	terraform init

unittest:
	pytest -m 'not integration'
