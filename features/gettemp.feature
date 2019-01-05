Feature: Temp
    A site where you can get the temperature.

Scenario: Obtaining the tempaerature
    Given That the temperature is 5 Celcius
    When I go to the temp page
    Then I should see 5 Celcius 
