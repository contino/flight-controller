Feature: Capture useful metrics about accounts

  @aws
  Scenario: Stores account lead time for aws
    Given an account has been requested for aws
    When the account has been created for aws
    Then the account created lead time is stored correctly for aws

  @gcp
  Scenario: Stores account lead time for gcp
    Given an account has been requested for gcp
    When the account has been created for gcp
    Then the account created lead time is stored correctly for gcp
