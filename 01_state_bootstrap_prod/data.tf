data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "external" "git_repository" {
  program = ["./get_git_repo.sh"]
}
