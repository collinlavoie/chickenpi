Feature: Camera imaging in web page
    Images can be obtained from the camera through the web interface

#Scenario: Viewing the page
#    Given I access the page
#    Then I should have a div with id: camera
#   And I should have a div with id: capture

Scenario: Viewing the page
    Given I want to interact with web page: /view/ 
    When I click the capture button
    Then I should see an image in div id: capture

#Scenario: Viewing the page
#    Given I obtain the following image from the camera:
#        filename.gif
#    And I access the page
#    Then I should see the following image:
#        filename.gif

# Add Scenario for camera to throw exception on unexpected data from capture
