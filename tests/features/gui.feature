Feature: Temperature web page
    A site where you can view the current temperature

Scenario: Viewing the page
    Given I access the webpage
    When I obtain the list of div elements 
    Then I should have a div with id "temperature"
