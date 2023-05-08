Azure implementation of the Flight Controller infrastructure and code deployment.

# Setup
```
make local
make make clean && azure-synth && make azure-plan-core
make azure-deploy-core

```

These targets will be changed to the following once Grafana is deployable:
```
make local
make make clean && azure-synth && make azure-plan-all
make azure-deploy-all
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
