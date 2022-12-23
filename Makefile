local: install-dependencies
	pipenv shell

install-dependencies:
	pipenv install --dev

unittest:
	pipenv run mypy src
	pipenv run pytest -m 'not integration' tests/

integration-test:
	pipenv run pytest -m 'integration' tests/

test:
	pipenv run pytest --cov=src --cov-fail-under=50 --cov-report term-missing tests/

e2e:
	pipenv run behave

build-tf-cdk:
	pipenv requirements | tee requirements.txt
	rsync -avu $(shell pwd)/src $(shell pwd)/infrastructure/all_files
	pip install -r requirements.txt --target=$(shell pwd)/infrastructure/all_files
	cd infrastructure;cdktf synth
	rm requirements.txt

deploy-tf-cdk: 
	cd infrastructure;cdktf deploy --auto-approve

destroy-tf-cdk:
	cd infrastructure;cdktf destroy --auto-approve
