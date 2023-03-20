Feature: Capture useful metrics about resources

  Scenario: Stores resource compliance lead time
    Given a resource has been found non compliant
    When the resource is found compliant
    Then the compliance lead time is stored correctly
