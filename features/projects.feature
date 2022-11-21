Feature: Capture useful metrics about projects

  Scenario: Stores project lead time
    Given a project has been requested
    Given a project has been assigned
    When the project has been created
    Then the lead time is stored correctly
