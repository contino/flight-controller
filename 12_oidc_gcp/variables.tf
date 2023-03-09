variable "project_id" {
  type = string
  description = "The Google Project ID"
}

variable "region" {
  type = string
  description = "The Google Project region"
  default = "australia-southeast1"
}

variable "gh_repo" {
  type = string
  description = "The GitHub repo in the format <username/repo_name>"
}