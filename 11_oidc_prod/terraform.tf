terraform {
  backend "s3" {
    bucket         = "103417687554-apac-flight-controller-aws"
    key            = "11_oidc_prod/terraform.tfstate"
    region         = "ap-southeast-2"
    dynamodb_table = "103417687554-apac-flight-controller-aws"
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

