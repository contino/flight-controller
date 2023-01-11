terraform {
  backend "s3" {
    bucket         = "099267815798-apac-flight-controller-aws"
    key            = "10_oidc/terraform.tfstate"
    region         = "ap-southeast-2"
    dynamodb_table = "099267815798-apac-flight-controller-aws"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "ap-southeast-2"
}

