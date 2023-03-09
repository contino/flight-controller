terraform {
  backend "gcs" {
    bucket = "flight-controller-state"
    prefix = "oidc/terraform.tfstate"
  }

  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.57.0"
    }
  }
}

 # Configure project and region
provider "google" {
  region = var.region
  project = var.project_id
}
