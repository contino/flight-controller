Feature: Capture useful metrics about patching

    Scenario: Stores metric around patching compliance percentage
        When patch run summary is complete
        Then the compliance percentage is stored correctly