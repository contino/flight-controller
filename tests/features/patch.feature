Feature: Capture useful metrics about patching

    @aws
    Scenario: Stores metric around patching compliance percentage for aws
        When patch run summary is complete for aws
        Then the compliance percentage is stored correctly for aws

    @gcp
    Scenario: Stores metric around patching compliance percentage for gcp
        When patch run summary is complete for gcp
        Then the compliance percentage is stored correctly for gcp