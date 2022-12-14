COMMIT_SHA = $(shell git rev-parse HEAD)

local:
	pip install pytest-cov
	pip install behave
	pip install boto3

unittest:
	cd code;pip install -r requirements.txt --target=/home/runner/work/apac-flight-controller-aws/apac-flight-controller-aws/code
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
	rsync -avu "/home/runner/work/apac-flight-controller-aws/apac-flight-controller-aws/code/src" "/home/runner/work/apac-flight-controller-aws/apac-flight-controller-aws/infra_tf_cdk/all_files"
	cd code;pip install -r requirements.txt --target=/home/runner/work/apac-flight-controller-aws/apac-flight-controller-aws/infra_tf_cdk/all_files
	cd infra_tf_cdk;pipenv install
	cd infra_tf_cdk;cdktf synth

test-tf-cdk:
	pip install pytest
	cd infra_tf_cdk;pip install cdktf
	cd infra_tf_cdk;pip install cdktf_cdktf_provider_aws
	cd infra_tf_cdk;pytest main-test.py

deploy-tf-cdk: 
	cd infra_tf_cdk;cdktf deploy --auto-approve

destroy-tf-cdk:
	cd infra_tf_cdk;cdktf destroy --auto-approve