Feature: Camera imaging in web page
    Images can be obtained from the camera through the web interface

#Scenario: Viewing the page
#    Given I access the page
#    Then I should have a div with id: camera
#   And I should have a div with id: capture

Scenario: Viewing the page
    Given I obtain a capture image
    #And I access the page
    #And I should see a capture image in div with id: capture

			    

#Scenario: Viewing the page
#    Given I obtain the following image from the camera:
#        filename.gif
#    And I access the page
#    Then I should see the following image:
#        filename.gif

# Add Scenario for camera to throw exception on unexpected data from capture
