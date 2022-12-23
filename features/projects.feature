Feature: Capture useful metrics about projects

  Scenario: Stores project lead time
    Given a project has been requested
    When the project has been created
    Then the lead time is stored correctly
