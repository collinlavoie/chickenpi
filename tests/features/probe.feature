Feature: Temperature probe
    An interface for obtainin temperature from 2-wire probes

Scenario: Obtaining temperature from local probes
    Given I have a probe
    When I obtain the temperature reading
    Then I should obtain the temperature

Scenario: Obtaining temperature from web resource
    Given I obtain data from a web resource
    When I obtain the temperature reading
    Then I should obtain the temperature
