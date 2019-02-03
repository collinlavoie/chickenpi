Feature: Temperature probe
    An interface for obtainin temperature from 2-wire probes

Scenario: Obtaining temperature from the probes
    Given I have a mock probe
    And I obtain the reading:
        2019-01-13 22:30:01,28-0000079ff834,7.125
    Then I obtain the following data:
        [{'sensor': u'28-0000079ff834', 'temp': u'7.125', 'time': u'2019-01-13 22:30:01'}]

Scenario: Obtaining bad data from the probes
    Given I have a mock probe
    And I obtain the reading:
        xxxx-01-13 22:30:01,28-0000079ff834,7.125
    Then I obtain the following data:
        []

Scenario: Obtaining good and bad data from the probes
    Given I have a mock probe
    And I obtain the reading:
        xxxx-01-13 22:30:01,28-0000079ff834,7.125
        2019-01-13 22:30:01,28-0000079ff834,7.125
    Then I obtain the following data:
        [{'sensor': u'28-0000079ff834', 'temp': u'7.125', 'time': u'2019-01-13 22:30:01'}]
