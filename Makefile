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

local-grafana:
	docker run -d -p 3000:3000 mirror.gcr.io/grafana/grafana:latest

# Test Commands
unittest:
	pipenv run pytest -m 'not integration' tests/src tests/publisher

integration-test:
	pipenv run pytest -m 'integration' tests/src tests/publisher

test:
	pipenv run pytest --cov=src --cov=publisher --cov-fail-under=81 --cov-report term-missing tests/src tests/publisher

watch:
	ptw -- -m 'not integration' tests/src tests/publisher

e2e:
	cd tests/; pipenv run behave

# Infrastructure Commands
build-python:
	pipenv requirements | tee requirements.txt
	rsync -avu $(shell pwd)/src $(shell pwd)/infrastructure/aws/all_files
	pip install -r requirements.txt --target=$(shell pwd)/infrastructure/aws/all_files
	pip install boto3 --target=$(shell pwd)/infrastructure/aws/api_key_rotation
	cd infrastructure/aws; cdktf provider add grafana/grafana
	cd infrastructure/gcp; cdktf provider add grafana/grafana

clean:
	cd infrastructure/aws; rm -rf cdktf.out
	cd infrastructure/gcp; rm -rf cdktf.out

synth-aws:
	cd infrastructure/aws;cdktf synth aws_infra_cdktf

synth-grafana:
	cd infrastructure/aws;cdktf synth grafana

synth-gcp:
	cd infrastructure/gcp; cdktf provider add grafana/grafana
	cd infrastructure/gcp; cdktf synth base_gcp_infra
	cd infrastructure/gcp; cdktf synth main_gcp_infra

synth: synth-aws synth-grafana synth-gcp

build: build-python synth

plan-aws:
	cd infrastructure/aws;cdktf plan aws_infra_cdktf

plan-grafana:
	cd infrastructure/aws;cdktf plan grafana

plan-gcp:
	cd infrastructure/gcp;cdktf plan base_gcp_infra main_gcp_infra

plan-gcp-grafana:
	cd infrastructure/gcp;cdktf plan grafana 

plan: build-python plan-aws plan-grafana plan-gcp

plan-gcpstack: plan-gcp plan-grafana

deploy:
	cd infrastructure/aws;cdktf deploy aws_infra_cdktf grafana --auto-approve

destroy-aws:
	cd infrastructure/aws;cdktf destroy aws_infra_cdktf

destroy-grafana:
	cd infrastructure/aws;cdktf destroy grafana

destroy: destroy-core destroy-grafana

deploy-base-gcp:
	cd infrastructure/gcp; cdktf deploy base_gcp_infra --auto-approve

deploy-main-gcp:
	cd infrastructure/gcp; cdktf deploy base_gcp_infra main_gcp_infra --auto-approve

build-image:
	gcloud auth configure-docker australia-southeast1-docker.pkg.dev
	pipenv requirements | tee requirements.txt
	docker buildx build --platform=linux/amd64 --push . -t australia-southeast1-docker.pkg.dev/contino-squad0-fc/flight-contoller-event-receiver/event_receiver:latest