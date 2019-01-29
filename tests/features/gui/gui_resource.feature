Feature: Temperature web page
    A site where you can view the current temperature

Scenario: Viewing the page
    Given I access the webpage
    When I obtain the list of div elements 
    Then I should have a div with id "temperature"

Scenario: Obtaining temperature from web resource
    Given I obtain data from a web resource
    When I obtain the temperature reading
    Then I should obtain the temperature
