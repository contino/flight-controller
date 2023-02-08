output "backend_configuration" {
  value = <<CONFIG
backend "s3" {
  bucket         = "${aws_s3_bucket.state.bucket}"
  key            = "$${replace_me()}/terraform.tfstate"
  region         = "${data.aws_region.current.name}"
  dynamodb_table = "${aws_dynamodb_table.lock_table.name}"
}
CONFIG
}
