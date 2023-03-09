<h1 align="center">Flight Controller Custom Publisher</h1>
<p align="center">Allows you to publish custom events for flight controller to produce metrics.</p>

# Usage

## Prerequsites
- Python version 3.10
- Pipenv (version 2022.10.12 proven working)
- Ensure you have working AWS account creds/tokens.

`make local` - Install python prerequisites and enter the pip environment.

## Base command:
`python -m publisher.entrypoints.main`

## Arguments: 

| Option (Short) | Options (Long) |                                   Description                                  |
|:--------------:|:--------------:|:------------------------------------------------------------------------------:|
| -h             | --help         | Shows command help and all available options                                   |
| -so            | --source       | {open_policy_agent,checkov} - The source in which you want to get events from. |
| -f             | --file         | The json file in which to parse result into events.                            |
| -si            | --sink         | {event_bridge} - The sink in which you want to send events to.                 |

## Example Workflow:

You can test with the examples in `tests/examples` and just running the the publisher tool or by using in your workflow like below.

**Custom Checkov Guardrail Events** 
1. `terraform plan --out tfplan.binary; terraform show -json tfplan.binary > tfplan.json`
2. `checkov -f tfplan.json -o json checkov.json`
3. `python -m publisher.entrypoints.main -so checkov -f tests/examples/checkov.json -si event_bridge`

**Custom Open Policy Agent Events**  
`python -m publisher.entrypoints.main -so open_policy_agent -f tests/examples/opa.json -si event_bridge`

**Example Workflow**  
1. Run Checkov on your Infrastructure as Code and output this to a .json file
2. Run Flight Controller handler.py on this file to parse results and generate events.  
   
**This can be done with in your CICD**

# Developing

## Code Structure
The code is structured in the [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) pattern.

![Clean Architecture](../images/CleanArchitecture.jpeg)

The current layers are:

1. `Entities`, which contains domain objects
2. `Drivers`, which interact with data storage
3. `Entrypoints`, which handle the event from AWS, retrieve and store data through drivers and call adapters to perform the needed business logic

The core rule of Clean Architecture, is that a layer can only depend on the layers that have come before it. E.g. code in the `usecases` layer, may depend on `entities`, but cannot depend on `adapters` or `drivers`.

When developing, it is simplest to start at the first layer and work down ending up with the entrypoint. This forces you to focus on the domain objects first before considering external services.

## Adding more support

Adding support for a new source:  
`publisher/drivers/` 

Adding support for a new event type:  
`publisher/entities/`

Adding support for a new sink:  
`publisher/drivers/`