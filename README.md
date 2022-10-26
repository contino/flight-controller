# Flight Controller on AWS Cloud Platform

This repository contains the code necessary for Flight Controller on GCP.

## What is Flight Controller?

Flight Controller is a unified, event-driven, data measurement service for capturing interesting events in a GCP environment.

The intent is to make it trivial to add new measures, allowing teams to be data driven and enable [SLO driven product development](https://www.youtube.com/watch?v=R_Uz5nkigdQ&list=PLIuxSyKxlQrAsbULewWndxvKIVW9y8LIK&index=20).

The approach to scaling a landing zone on AWS is [elaborated here](https://aws.amazon.com/blogs/mt/flight-controller-by-contino-a-solution-built-on-aws-control-tower/).

## Architecture

![Flight Controller Architecture](flight_controller.png)

For macOs get graphviz for the diagrams to work
    - brew install graphviz 



# Questions

- Do you want to go with Terraform, we can use AWS CDK or even terraform cdktf
- Do you want to use docker or Lambda or “dockerized lambda”?