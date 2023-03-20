<h1 align="center">Flight Controller - Controller</h1>
<p align="center">Code for the controller part of Flight controller.</p>

## Development

### Start of the day

- Ensure you have refreshed you AWS account tokens.
  
### Local Environment Set Up

`make local`

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

<!-- ![Clean Architecture](../images/CleanArchitecture.jpeg) -->

The current layers are:

1. `Entities`, which contains domain objects
2. `Usecases`, which orchestrate domain objects
3. `Adapters`, which convert events and data into known types
4. `Drivers`, which interact with data storage
5. `Entrypoints`, which handle the event from AWS, retrieve and store data through drivers and call adapters to perform the needed business logic

### How to create a new metric?

1. First of all, you need to define a SLO. In this example we will work with 3 SLO's. These SLO's are related to creation of a Guardrail event.
    - "total amount of guardrail activations"
    - "time taken between a guardrail activated and guardrail passed"
    - "maximum guardrail activations before a guardrail pass"

2. Next you need to understand the "process" for a "guardrail". This includes actors, systems, and automation that contributes to the flagging of guardrails from activation to pass. From the process diagram we need to identify the events that are associated with each component of the "process". The "event" in the process should have minimum the following fields
    - `aggregate_id`: this is the id to all events that is being used to identify the instantiation of a process. For example, with guardrails the aggregate_id is the resource id, allowing all events to be grouped by the resources lifecycle.
    - `aggregate_type`: this is the type of aggregate used, for guardrail this is "Resource".
    - `aggregate_version`: the number of occurence for this aggregate_id
    - `event_id`: unique UUID for each event.
    - `event_version`: this is the version number of the event.
    - `event_type`: this is the type of event, this can be any string representing what happened.
    - `payload`: Any other details that the event requires for processing and calculation of metrics.

3. Map the event to entities by creating a python file for entities under `src/entities`, then updating the `events.py` and `metrics.py` files. See `guardrail.py` for example of entities. Entities come in two form:
    - Event Entites: corresponding to the events of the domain
    - Metric Entities: corresponding to the SLO's you have defined in step 1

    ![See diagram](../images/processDiagram.png)

4. Conversion of the incoming event and calculation of metrics are handled in the usescases. Insert a new use case under `src/usecases` that converts the event and calculates the metric you are after. You can see the example of how in the guardrails.py
5. Controller is what routes the incoming event to the correct usecase. This may be expanded on in the future but at this current time that is all it does.
6. Once you have finised the entites and usecases the rest should be able to handle your event/metrics. Ensure that you have built out the tests under `tests/` folder and confirm it all works. `src/controller/`, `src/drivers/`, `src/usecases/` and `features/` will all need new tests for your event/metric.

![See diagram](../images/UMLdiagram.png)

### Manually sending events from the console

After you deploy your infrastructure you can interact with the eventbridge on AWS by sending different messages by running the following from the 'infra_aws_cdk' folder:

- Send Project requested event
  - `aws events put-events --entries file://./tests/events/test-eventR.json`
- Send Project assigned event
  - `aws events put-events --entries file://./tests/events/test-eventA.json`
- Send Project created event 
  - `aws events put-events --entries file://./tests/events/test-eventC.json`
