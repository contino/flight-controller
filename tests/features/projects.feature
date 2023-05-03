Feature: Capture useful metrics about projects

    @aws
    Scenario: Stores project lead time for aws
        Given a project has been requested for aws
        When the project has been created for aws
        Then the lead time is stored correctly for aws

    @gcp
    Scenario: Stores project lead time for gcp
        Given a project has been requested for gcp
        When the project has been created for gcp
        Then the lead time is stored correctly for gcp
