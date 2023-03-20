Feature: Capture useful metrics about identity requests

  Scenario: Stores lead time for identity
    Given an identity has been requested
    When the identity has been created
    Then the identity created lead time is stored correctly
