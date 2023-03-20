Feature: Capture useful metrics around guardrail compliance

  Scenario: Guardrail is activated and activation count is stored correctly.
    When a guardrail has been activated
    Then the activation count is stored correctly

  Scenario: Guardrail is activated and then passes. Store the lead time.
    Given a guardrail has been activated
    When a guardrail passes
    Then the guardrail lead time is stored correctly

  Scenario: Guardrail is activated and then passes. Store the max activation count.
    Given a guardrail has been activated
    When a guardrail passes
    Then the max activation count is stored correctly

