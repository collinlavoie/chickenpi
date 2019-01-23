Feature: Temperature web page
    A site where you can view the current temperature

Scenario: Viewing the page
    Given The probes read: 2019-01-13 19:50:16,28-000007a81e55,1.125
    And I access the page
    Then I should have a div with id: temp
    And I should see temperature: 1.12

Scenario: Viewing the page
    Given The probes read:
        2019-01-13 22:30:01,28-0000079ff834,7.125
        2019-01-13 22:30:02,28-000007a81e55,-.687
        2019-01-13 22:45:01,28-0000079ff834,7.062
        2019-01-13 22:45:02,28-000007a81e55,-.562
        2019-01-13 23:00:01,28-0000079ff834,7.062
        2019-01-13 23:00:03,28-000007a81e55,-.562
        2019-01-13 23:15:01,28-0000079ff834,7.062
        2019-01-13 23:15:02,28-000007a81e55,-.875
        2019-01-13 23:30:01,28-0000079ff834,7.000
        2019-01-13 23:30:02,28-000007a81e55,-.875
    And I access the page
    Then I should see a temperature reading

@todo
Scenario: Camera throws an exception on unexpected capture data
    Given the camera recieves corrupt data
    Then the camera raises a ValueError exception
