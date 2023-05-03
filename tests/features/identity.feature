Feature: Capture useful metrics about identity requests

  @aws
  Scenario: Stores lead time for identity for aws
    Given an identity has been requested for aws
    When the identity has been created for aws
    Then the identity created lead time is stored correctly for aws

  @gcp
  Scenario: Stores lead time for identity for gcp
    Given an identity has been requested for gcp
    When the identity has been created for gcp
    Then the identity created lead time is stored correctly for gcp