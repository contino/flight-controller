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

e2e:
	behave

build-aws-cdk: 
	cd infra_aws_cdk;cdk synthesize

test-aws-cdk:
	pytest infra_aws_cdk/tests/

deploy-aws-cdk: 
	cd infra_aws_cdk;cdk deploy

build-tf-cdk: 
	cd infra_tf_cdk;cdktf synth

test-tf-cdk:
	cd infra_tf_cdk;pytest main-test.py

deploy-tf-cdk: 
	cd infra_tf_cdk;cdk deploy