resource "aws_dynamodb_table" "lock_table" {
  name         = "${data.aws_caller_identity.current.account_id}-${data.external.git_repository.result.name}"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true
  }

  server_side_encryption {
    enabled     = true
    kms_key_arn = aws_kms_key.key.arn
  }
}
