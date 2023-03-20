<h1 align="center">Flight Controller - Publisher</h1>
<p align="center">Allows you to publish custom events for flight controller to produce metrics.</p>

## Usage

### Prerequsites

- Python version 3.10
- Pipenv (version 2022.10.12 proven working)
- Ensure you have working AWS account creds/tokens.

`make local` - Install python prerequisites and enter the pip environment.

### Base command

`python -m publisher.entrypoints.main`

### Arguments

| Option (Short) | Options (Long) |                                   Description                                  |
|:--------------:|:--------------:|:------------------------------------------------------------------------------:|
| -h             | --help         | Shows command help and all available options                                   |
| -so            | --source       | {open_policy_agent,checkov} - The source in which you want to get events from. |
| -f             | --file         | The json file in which to parse result into events.                            |
| -si            | --sink         | {event_bridge} - The sink in which you want to send events to.                 |

### Example Workflow

You can test with the examples in `tests/examples` by running the the publisher tool against these output files.

#### Custom Checkov Guardrail Events

1. `checkov -d ${INFRA_FOLDER} -o json > checkov.json`
2. `python -m publisher.entrypoints.main -so checkov -f checkov.json -si event_bridge`

#### Custom Open Policy Agent Events

1. `python -m publisher.entrypoints.main -so open_policy_agent -f opa.json -si event_bridge`

#### Typical Workflow

1. Run your desired tool and output this to a .json file
2. Run Flight Controller handler.py on this file to parse results and generate events.  
**This can be done with in your CICD**

## Development

### Make Commands

- `make local` setup local environment and install dependencies.
- `make install-dependencies` install dependencies defined in the pipfile.
- `make unittest` runs all the unit tests (i.e. tests that are not [marked as integration](https://docs.pytest.org/en/7.1.x/example/markers.html)).
- `make integration-test` run all the integration tests.
- `make test` runs all the tests and reports on coverage.
- `make watch` runs all the unit tests on file change. Allowing the test code while making live changes.
- `make e2e` runs the end to end BDD tests using [behave](https://github.com/behave/behave).

### Code Structure

The code is structured in the [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) pattern.

The current layers are:

1. `Entities`, which contains domain objects (Events)
2. `Drivers`, which interact with data storage (File Source, Git, Event Bridge)
3. `Entrypoints`, which handle the command line arguments and passing data between layers.

*The core rule of Clean Architecture, is that a layer can only depend on the layers that have come before it. E.g. code in the `usecases` layer, may depend on `entities`, but cannot depend on `adapters` or `drivers`.* 

When developing, it is simplest to start at the first layer and work down ending up with the entrypoint. This forces you to focus on the domain objects first before considering external services.

### Adding more support

Adding support for a new source:  
`publisher/drivers/`

Adding support for a new event type:  
`publisher/entities/`

Adding support for a new sink:  
`publisher/drivers/`
