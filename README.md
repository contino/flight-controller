<h1 align="center">Flight Controller</h1>
<p align="center">This repository contains the code necessary for Flight Controller</p>

## What is Flight Controller?

Flight Controller is a unified, event-driven, data measurement service for capturing interesting events in a AWS environment.
  
The intent is to make it trivial to add new measures, allowing teams to be data driven and enable [SLO driven product development](https://www.youtube.com/watch?v=R_Uz5nkigdQ&list=PLIuxSyKxlQrAsbULewWndxvKIVW9y8LIK&index=20).  

The approach to scaling a landing zone on AWS is [elaborated here](https://aws.amazon.com/blogs/mt/flight-controller-by-contino-a-solution-built-on-aws-control-tower/).  

## Repository Structure

- [Flight Controller Event Catalog](https://legendary-spoon-f82c1640.pages.github.io): `docs/`
  - [README.md](docs/README.md)
- Flight Controller Infrastructure Terraform CDK Code - `infrastructure/`
  - [README.md](infrastructure/README.md)
- Flight Controller Custom Publisher Code - `publisher/`
  - [README.md](publisher/README.md)
- Flight Controller Code - `src/`
  - [README.md](src/README.md)
- Flight Controller Tests - `tests/`
  - [README.md](tests/README.md)

## Development

### Prerequisites

- Python version 3.10
- Pipenv (version 2022.10.12 proven working)
- Terraform CDK version 0.15.5
- Docker

#### Optional

- For macOS get graphviz for the diagrams to work
  - brew install graphviz  
- [Granted](https://granted.dev/)
  - brew tap common-fate/granted
  - brew install granted
  - granted registry add https://github.com/contino/apac-scaffolding-granted-registry.git/granted.yml

### Start of the day

- Ensure you have refreshed you AWS account tokens.
  
### Local Environment Set Up

`make local`

### General Make Commands

- `make local` setup local environment and install dependencies.
- `make docs-run` install, build and run a dev version of the docs.
- `make synth` synth all cloud stacks with TF CDK.
- `make plan` plans all cloud stacks with TF CDK
- `make deploy` deploys all cloud stacks with TF CDK
- `make destroy` destroys all cloud stacks with TF CDK.
- `make clean` remove the cdktf.out folders for all clouds.

Testing is split into four commands:

- `make unittest` runs all the unit tests (i.e. tests that are not [marked as integration](https://docs.pytest.org/en/7.1.x/example/markers.html)).
- `make integration-test` run all the integration tests.
- `make test` runs all the tests and reports on coverage. 
- `make e2e` runs the end to end BDD tests using [behave](https://github.com/behave/behave).
- `make watch` runs all the unit tests on file change. Allowing the test code while making live changes.

### Merging changes

At the current time there are no branch protections. However, as the build process creates a commit for every build, to keep the git history clean, please `rebase/squash` your commits before pushing. You can do this by running `git fetch origin main && git rebase -i origin/main`, `edit`ing the first commit, and applying `fixup` to all following commits.

### Code Structure

The code is structured in the [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) pattern.

![Clean Architecture](images/CleanArchitecture.jpeg)

The core rule of Clean Architecture, is that a layer can only depend on the layers that have come before it. E.g. code in the `usecases` layer, may depend on `entities`, but cannot depend on `adapters` or `drivers`.

When developing, it is simplest to start at the first layer and work down ending up with the entrypoint. This forces you to focus on the domain objects first before considering external services.

# Roadmap

- [ ] Update integration and automation tests
- [ ] Create Dockerized lambda code for product creation metric

# Frequently Asked Questions

- How do I create a new metric?
  - [README.md](src/README.md#how-to-create-a-new-metric)
- How do I update the Grafana Panels?
  - TF CDK is used to build and modify Grafana dashboard and the panels that goes inside dashboard. Dashboard configuration is  managed via `dashboard.json` located within the `infrastructure` folder. Export the new configuration from grafana after making your changes, now update the dashboard.json with the updated configuration.

- How do I update the Event Docs?
  - [README.md](docs/README.md)
