Feature: Capture useful metrics around guardrail compliance

  @aws
  Scenario: Guardrail is activated and activation count is stored correctly for aws
    When a guardrail has been activated for aws
    Then the activation count is stored correctly for aws

  @aws
  Scenario: Guardrail is activated and then passes. Store the lead time for aws
    Given a guardrail has been activated for aws
    When a guardrail passes for aws
    Then the guardrail lead time is stored correctly for aws

  @aws
  Scenario: Guardrail is activated and then passes. Store the max activation count for aws
    Given a guardrail has been activated for aws
    When a guardrail passes for aws
    Then the max activation count is stored correctly for aws

  @gcp
  Scenario: Guardrail is activated and activation count is stored correctly for gcp
  When a guardrail has been activated for gcp
  Then the activation count is stored correctly for gcp

  @gcp
  Scenario: Guardrail is activated and then passes. Store the lead time for gcp
    Given a guardrail has been activated for gcp
    When a guardrail passes for gcp
    Then the guardrail lead time is stored correctly for gcp

  @gcp
  Scenario: Guardrail is activated and then passes. Store the max activation count for gcp
    Given a guardrail has been activated for gcp
    When a guardrail passes for gcp
    Then the max activation count is stored correctly for gcp

