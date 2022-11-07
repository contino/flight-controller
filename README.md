# Flight Controller on AWS Cloud Platform

This repository contains the code necessary for Flight Controller on GCP.

## What is Flight Controller?

Flight Controller is a unified, event-driven, data measurement service for capturing interesting events in a GCP environment.

The intent is to make it trivial to add new measures, allowing teams to be data driven and enable [SLO driven product development](https://www.youtube.com/watch?v=R_Uz5nkigdQ&list=PLIuxSyKxlQrAsbULewWndxvKIVW9y8LIK&index=20).

The approach to scaling a landing zone on AWS is [elaborated here](https://aws.amazon.com/blogs/mt/flight-controller-by-contino-a-solution-built-on-aws-control-tower/).

## Architecture

![Flight Controller Architecture](flight_controller.png)

## Development

### Prerequisites

- Python version 3.10
- Pipenv (version 2022.10.12 proven working)
- Terraform version 1.2.7
- Docker installed

- AWS CDK
    - NVM -> npm and node https://github.com/nvm-sh/nvm#usage 
    - AWS CLI https://docs.aws.amazon.com/cli/latest/userguide/getting-started-prereqs.html
    - AWS CDK https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html

Optional

For macOs get graphviz for the diagrams to work
    - brew install graphviz 

### start of day

- assume role using https://granted.dev/
    - $ assume

- set up aws cdk
    - $ cd infra_aws_cdk; source .venv/bin/activate 

- set up pipenv
    - pipenv shell

- synthsis and deploy infra
    - cdk synthesize
    - cdk deploy

### Local Environment Set Up

`make local`

### Testing

Testing is split into four commands:

- `make unittest` runs all the unit tests (i.e. tests that are not [marked as integration](https://docs.pytest.org/en/7.1.x/example/markers.html))
- `make integration-test` run all the integration tests (TODO)
- `make test` runs all the tests and reports on coverage (TODO)
- `make e2e` runs the end to end BDD tests using [behave](https://github.com/behave/behave) (TODO)

### Code Structure

The code is structured in the [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) pattern.

![Clean Architecture](CleanArchitecture.jpeg)

The current layers are:

1. `Entities`, which contains domain objects
2. `Usecases`, which orchestrate domain objects
3. `Adapters`, which convert events and data into known types
4. `Drivers`, which interact with data storage
5. `Entrypoints`, which handle the event from GCP, retrieve and store data through drivers and call adapters to perform the needed business logic

The core rule of Clean Architecture, is that a layer can only depend on the layers that have come before it. E.g. code in the `usecases` layer, may depend on `entities`, but cannot depend on `adapters` or `drivers`.

When developing, it is simplest to start at the first layer and work down ending up with the entrypoint. This forces you to focus on the domain objects first before considering external services.

### Deploying a change

To deploy a change run `make build`, this command:

1. Creates a commit of your current state with the current timestamp as the message
2. Regenerates the `requirements.txt` file
3. Builds a new Docker image labelled with the current commit SHA
4. Applies the Terraform changes which will include moving the Cloud Run service to the new container

### Merging changes

At the current time there are no branch protections. However, as the build process creates a commit for every build, to keep the git history clean, please `rebase/squash` your commits before pushing. You can do this by running `git fetch origin main && git rebase -i origin/main`, `edit`ing the first commit, and applying `fixup` to all following commits.

# Roadmap

- create time stream
- create dashboard integration
- refactor code
- Update integration and autoamtion tests
- Create tfcdk build
- Integrate Dockerized lambda code for product creation metric

# Questions
- account oyu have created is not working. gives https://portal.aws.amazon.com/billing/signup/incomplete.
- Also how to use https://granted.dev/ without copying the session keys from browser because this is not SSO :(
- how to set up the contoino-dev SSO
