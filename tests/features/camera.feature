Feature: Interfacing with the camera
    The camera can be activated throught the web interface

Scenario: Obtain image from camera
    Given An image is obtained from the camera
    When I access the webpage
    Then I should see the image
