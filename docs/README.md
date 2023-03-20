<h1 align="center">Flight Controller - Event Catalog</h1>
<p align="center">Documentation for Flight Controller's Events</p>

## Link

[Flight Controller Event Catalog](https://legendary-spoon-f82c1640.pages.github.io)

## Documentation Structure

- Event Domains (EG. Account, Backup, Guardrail): `domains/`
- Domain Events (EG. AccountCreated, AccountRequested): `domains/${DOMAIN}/events/`
- Event Services (Account Vending Machine, Flight Controller): `services/`

## Development

Making changes to the Event Catalog Documentation is pretty straight forward. You will need to add and update the relevant files within the 3 folders listed above. See others for examples.  
More info in the official Event Catalog [documentation](https://www.eventcatalog.dev/docs/introduction).

### Running Locally

 `make docs_run`. This can be useful to confirm your changes.

### Make Commands

- `make docs_install` (npm install) Will install all NPM requirements
- `make docs_build` (npm install & npm run build) Will build the Event Catalog and output to the folder `docs/out`. This is used to confirm you changes are valid.
- `make docs_run` (npm install & npm run build & npm run dev) Will run a local dev instance of the site, so you can see you changes.
