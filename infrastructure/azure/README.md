Azure implementation of the Flight Controller infrastructure and code deployment.

# Setup
In a new terminal session, run the followign commands while in the repository root:
```
make local
make clean
az login
export JSII_SILENCE_WARNING_UNTESTED_NODE_VERSION=1
```

Run the following following commands to synthesise, plan, apply and destroy the Azure resources:
```
make azure-synth
make azure-plan-core
make azure-deploy-core
make azure-destroy-core
```

The `plan` and `deploy` targets will be changed to the following once Grafana is deployable:
```
make azure-synth 
make azure-plan-all
make azure-deploy-all
make azure-destroy-all
```

# Resources
Following Azure resources are deployed:
- Resource group
- Storage account
- Storage container
- SQL server
- SQL database
- Service plan
- Function app
- Eventgrid topic

# Tasks
- [x]  Configure root CDKTF dependencies
- [x] Configure Azure provider (local)
- [x] Define Terraform resources for Flight Controller application and database infrastructure
- [x] Add `make` hooks to automate development environment configuration
- [ ] Add Azure-specific configuration abstractions for database and telemetry support 
- [ ] Grafana deployment
