Feature: Capture useful metrics about accounts

  Scenario: Stores account lead time
    Given an account has been requested
    Given an account has been assigned
    When the account has been created
    Then the lead time is stored correctly
