local: install-dependencies
	pipenv shell

install-dependencies:
	pipenv install --dev

unittest:
	pipenv run pytest -m 'not integration' tests/

integration-test:
	pipenv run pytest -m 'integration' tests/

test:
	pipenv run pytest --cov=src --cov-fail-under=50 --cov-report term-missing tests/

e2e:
	pipenv run behave

build-python:
	pipenv requirements | tee requirements.txt
	rsync -avu $(shell pwd)/src $(shell pwd)/infrastructure/all_files
	pip install -r requirements.txt --target=$(shell pwd)/infrastructure/all_files

synth:
	cd infrastructure;cdktf synth

build: build-python synth

plan: 
	cd infrastructure;cdktf plan

deploy: 
	cd infrastructure;cdktf deploy --auto-approve

destroy:
	cd infrastructure;cdktf destroy --auto-approve
