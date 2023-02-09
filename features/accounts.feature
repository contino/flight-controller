Feature: Capture useful metrics about accounts

  Scenario: Stores account lead time
    Given an account has been requested
    When the account has been created
    Then the account created lead time is stored correctly
