# Local Commands
local: install-dependencies
	pipenv shell

install-dependencies:
	pipenv install --dev

docs-install:
	cd docs;npm install

docs-build: docs-install
	cd docs;npm run build

docs-run: docs-build
	cd docs;npm run dev

# Test Commands
unittest:
	pipenv run pytest -m 'not integration' tests/

integration-test:
	pipenv run pytest -m 'integration' tests/

test:
	pipenv run pytest --cov=src --cov-fail-under=81 --cov-report term-missing tests/

watch:
	ptw -- -m 'not integration' tests/

e2e:
	pipenv run behave

# Infrastructure Commands
build-python:
	pipenv requirements | tee requirements.txt
	rsync -avu $(shell pwd)/src $(shell pwd)/infrastructure/all_files
	pip install -r requirements.txt --target=$(shell pwd)/infrastructure/all_files

clean:
	cd infrastructure; rm -rf cdktf.out

synth-core:
	cd infrastructure;cdktf synth infra_tf_cdk

synth-grafana:
	cd infrastructure;cdktf synth grafana

synth: synth-core synth-grafana

build: build-python synth

plan-core:
	cd infrastructure;cdktf plan infra_tf_cdk

plan-grafana:
	cd infrastructure;cdktf plan grafana

plan: build-python plan-core plan-grafana

deploy: build-python
	cd infrastructure;cdktf deploy infra_tf_cdk grafana --auto-approve

destroy-core:
	cd infrastructure;cdktf destroy infra_tf_cdk

destroy-grafana:
	cd infrastructure;cdktf destroy grafana

destroy: destroy-core destroy-grafana
