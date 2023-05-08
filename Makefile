INFRA_ARGS = 

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

watch:
	ptw -- -m 'not integration' tests/src tests/publisher

e2e:
	cd tests/; pipenv run behave

# Infrastructure Commands

# General
clean:
	cd infrastructure/aws; rm -rf cdktf.out
	cd infrastructure/gcp; rm -rf cdktf.out
	cd infrastructure/azure; rm -rf cdktf.out

synth: aws-synth gcp-synth azure-synth

plan: aws-plan-all gcp-plan-all azure-plan-all

deploy: aws-deploy-all gcp-deploy-all azure-deploy-all

destroy: aws-destroy-all gcp-destroy-all azure-destroy-all

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

gcp-build-image:
	@echo "\n\n---GCP-BUILD-IMAGE---\n"
	gcloud auth configure-docker australia-southeast1-docker.pkg.dev
	pipenv requirements | tee requirements.txt
	docker buildx build --platform=linux/amd64 --push . -t australia-southeast1-docker.pkg.dev/contino-squad0-fc/flight-contoller-event-receiver/event_receiver:latest

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

gcp-deploy-all: gcp-deploy-base gcp-build-image gcp-deploy-core #gcp-deploy-grafana

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

# Azure
azure-build-dependencies:
	@echo "\n\n---AZURE-BUILD-DEPENDENCIES---\n"
	cd infrastructure/azure;cdktf provider add grafana/grafana

azure-synth: azure-build-dependencies
	@echo "\n\n---AZURE-SYNTH---\n"
	cd infrastructure/azure;cdktf synth

azure-plan-core: 
	@echo "\n\n---AZURE-PLAN-CORE---\n"
	cd infrastructure/azure;cdktf plan azure_core

azure-plan-grafana:
	@echo "\n\n---AZURE-PLAN-GRAFANA---\n"
	cd infrastructure/azure;cdktf plan azure_grafana_dashboard

azure-plan-convert: 
	@echo "\n\n---Converting AZURE plans file to json---\n"
	cd infrastructure/azure/cdktf.out/stacks; \
	find . -type f -name 'plan' -exec dirname {} \; | while read file; do \
		cd "$$file"; \
		terraform show -json plan > plan.json; \
		cd -; \
	done

azure-plan-all: azure-build-dependencies azure-plan-core azure-plan-grafana azure-plan-convert

azure-deploy-core:
	@echo "\n\n---AZURE-DEPLOY-CORE---\n"
	cd infrastructure/azure;cdktf deploy azure_core ${INFRA_ARGS}

azure-deploy-grafana:
	@echo "\n\n---AZURE-DEPLOY-GRAFANA---\n"
	cd infrastructure/azure;cdktf deploy azure_grafana_dashboard ${INFRA_ARGS}

azure-deploy-all:
	@echo "\n\n---AZURE-DEPLOY-ALL---\n"
	cd infrastructure/azure;cdktf deploy azure_core azure_grafana_dashboard ${INFRA_ARGS}

azure-destroy-core:
	@echo "\n\n---AZURE-DESTROY-CORE---\n"
	cd infrastructure/azure;cdktf destroy azure_core

azure-destroy-grafana:
	@echo "\n\n---AZURE-DESTROY-GRAFANA---\n"
	cd infrastructure/azure;cdktf destroy azure_grafana_dashboard

azure-destroy-all: 
	@echo "\n\n---AZURE-DESTROY-ALL---\n"
	cd infrastructure/azure;cdktf destroy azure_core azure_grafana_dashboard