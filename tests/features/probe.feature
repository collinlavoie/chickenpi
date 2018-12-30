Feature: Temperature probe
    An interface for obtainin temperature from 2-wire probes

Scenario: Obtaining temperature
    Given I have a probe
    When I obtain the temperature reading
    Then I should obtain the temperature
