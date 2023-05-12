INFRA_ARGS = 
COMMIT := $(shell git rev-parse --short HEAD)

# Local Commands
local: install-dependencies
	pipenv shell

install-dependencies:
	pipenv clean
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

aws-test:
	pipenv run pytest -m 'not gcp' --cov=src --cov=publisher --cov-fail-under=75 --cov-report term-missing tests/src tests/publisher

gcp-test:
	pipenv run pytest -m 'not aws' --cov=src --cov=publisher --cov-fail-under=75 --cov-report term-missing tests/src tests/publisher

watch:
	ptw -- -m 'not integration' tests/src tests/publisher

e2e:
	cd tests/; pipenv run behave

aws-e2e:
	cd tests/; pipenv run behave --tags=aws

gcp-e2e:
	cd tests/; pipenv run behave --tags=gcp

# Infrastructure Commands

# General
clean:
	cd infrastructure/aws; rm -rf cdktf.out
	cd infrastructure/gcp; rm -rf cdktf.out

synth: aws-synth gcp-synth

plan: aws-plan-all gcp-plan-all

deploy: aws-deploy-all gcp-deploy-all

destroy: aws-destroy-all gcp-destroy-all

# AWS
aws-build-dependencies:
	@echo "\n\n---AWS-BUILD-DEPENDENCIES---\n"
	rsync -avu $(shell pwd)/src $(shell pwd)/infrastructure/aws/controller_core
	pipenv requirements | tee requirements.txt
	pip install -r requirements.txt --target=$(shell pwd)/infrastructure/aws/controller_core
	pip install boto3 --target=$(shell pwd)/infrastructure/aws/api_key_rotation
	cd infrastructure/aws; cdktf provider add grafana/grafana
	
aws-synth: aws-build-dependencies
	@echo "\n\n---AWS-SYNTH---\n"
	cd infrastructure/aws;cdktf synth

aws-plan-core: 
	@echo "\n\n---AWS-PLAN-CORE---\n"
	cd infrastructure/aws;cdktf plan aws_core

aws-plan-grafana:
	@echo "\n\n---AWS-PLAN-GRAFANA---\n"
	cd infrastructure/aws;cdktf plan aws_grafana_dashboard

aws-plan-all: aws-build-dependencies aws-plan-core aws-plan-grafana aws-plan-convert

aws-plan-convert: 
	@echo "\n\n---Converting AWS plans file to json---\n"
	cd infrastructure/aws/cdktf.out/stacks; \
	find . -type f -name 'plan' -exec dirname {} \; | while read file; do \
		cd "$$file"; \
		terraform show -json plan > plan.json; \
		cd -; \
	done

aws-deploy-core:
	@echo "\n\n---AWS-DEPLOY-CORE---\n"
	cd infrastructure/aws;cdktf deploy aws_core ${INFRA_ARGS}

aws-deploy-grafana:
	@echo "\n\n---AWS-DEPLOY-GRAFANA---\n"
	cd infrastructure/aws;cdktf deploy aws_grafana_dashboard ${INFRA_ARGS}

aws-deploy-all:
	@echo "\n\n---AWS-DEPLOY-ALL---\n"
	cd infrastructure/aws;cdktf deploy aws_core aws_grafana_dashboard ${INFRA_ARGS}

aws-destroy-core:
	@echo "\n\n---AWS-DESTROY-CORE---\n"
	cd infrastructure/aws;cdktf destroy aws_core

aws-destroy-grafana:
	@echo "\n\n---AWS-DESTROY-GRAFANA---\n"
	cd infrastructure/aws;cdktf destroy aws_grafana_dashboard

aws-destroy-all: 
	@echo "\n\n---AWS-DESTROY-ALL---\n"
	cd infrastructure/aws;cdktf destroy aws_core aws_grafana_dashboard

# GCP
gcp-build-dependencies:
	@echo "\n\n---GCP-BUILD-DEPENDENCIES---\n"
	cd infrastructure/gcp; cdktf provider add grafana/grafana

gcp-core-image:
	@echo "\n\n---GCP-BUILD-IMAGE---\n"
	gcloud auth configure-docker australia-southeast1-docker.pkg.dev
	pipenv requirements | tee requirements.txt
	docker buildx build --platform=linux/amd64 -f infrastructure/gcp/Core.Dockerfile . --push  -t australia-southeast1-docker.pkg.dev/contino-squad0-fc/flight-controller-event-receiver/event_receiver:${COMMIT}

gcp-grafana-image:
	@echo "\n\n---BUILD-GRAFANA-IMAGE---\n"
	cd infrastructure/gcp
	gcloud auth configure-docker australia-southeast1-docker.pkg.dev
	docker buildx build --platform=linux/amd64 --build-arg GRAFANA_PASSWORD=${GRAFANA_PASSWORD} -f infrastructure/gcp/Grafana.Dockerfile . --push  -t australia-southeast1-docker.pkg.dev/contino-squad0-fc/flight-controller-event-receiver/grafana:${COMMIT}

gcp-synth: gcp-build-dependencies
	@echo "\n\n---GCP-SYNTH---\n"
	cd infrastructure/gcp; cdktf synth

gcp-plan-base:
	@echo "\n\n---GCP-PLAN-BASE---\n"
	cd infrastructure/gcp;cdktf plan gcp_base

gcp-plan-core:
	@echo "\n\n---GCP-PLAN-CORE---\n"
	cd infrastructure/gcp;cdktf plan gcp_core

gcp-plan-grafana:
	@echo "\n\n---GCP-PLAN-GRAFANA---\n"
	cd infrastructure/gcp;cdktf plan gcp_grafana 

gcp-plan-all: gcp-build-dependencies gcp-plan-base gcp-plan-core gcp-plan-convert

gcp-plan-convert: 
	@echo "\n\n---Converting GCP plans file to json---\n"
	cd infrastructure/gcp/cdktf.out/stacks; \
	find . -type f -name 'plan' -exec dirname {} \; | while read file; do \
		cd "$$file"; \
		terraform show -json plan > plan.json; \
		cd -; \
	done

gcp-deploy-base:
	@echo "\n\n---GCP-DEPLOY-BASE---\n"
	cd infrastructure/gcp;cdktf deploy gcp_base ${INFRA_ARGS}

gcp-deploy-core:
	@echo "\n\n---GCP-DEPLOY-CORE---\n"
	cd infrastructure/gcp;cdktf deploy gcp_base gcp_core ${INFRA_ARGS}

gcp-deploy-grafana:
	@echo "\n\n---GCP-DEPLOY-GRAFANA---\n"
	cd infrastructure/gcp;cdktf deploy gcp_grafana ${INFRA_ARGS}

gcp-deploy-all: gcp-deploy-base gcp-core-image gcp-grafana-image gcp-deploy-core gcp-deploy-grafana

gcp-destroy-base:
	@echo "\n\n---GCP-DESTROY-BASE---\n"
	cd infrastructure/gcp;cdktf destroy gcp_base

gcp-destroy-core:
	@echo "\n\n---GCP-DESTROY-CORE---\n"
	cd infrastructure/gcp;cdktf destroy gcp_core
	
gcp-destroy-grafana:
	@echo "\n\n---GCP-DESTROY-GRAFANA---\n"
	cd infrastructure/gcp;cdktf destroy gcp_grafana 

gcp-destroy-all:
	@echo "\n\n---GCP-DESTROY-ALL---\n"
	cd infrastructure/gcp;cdktf destroy gcp_base gcp_core gcp_grafana 