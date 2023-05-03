Feature: Capture useful metrics about resources

  @aws
  Scenario: Stores resource compliance lead time for aws
    Given a resource has been found non compliant for aws
    When the resource is found compliant for aws
    Then the compliance lead time is stored correctly for aws

  @gcp
  Scenario: Stores resource compliance lead time for gcp
    Given a resource has been found non compliant for gcp
    When the resource is found compliant for gcp
    Then the compliance lead time is stored correctly for gcp
