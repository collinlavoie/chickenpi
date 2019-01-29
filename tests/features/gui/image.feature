Feature: Camera imaging in web page
    Images can be obtained from the camera through the web interface

Scenario: Capture image route
    Given The app uses a mock camera
    And I browse to: /capture_image/
    Then I should see a path to a captured image

Scenario: Clicking capture button displays an image in the page
    Given The app uses a mock camera
    And I interact with web page: /view/
    When I click the capture button
    Then I should see an image in div id: capture

@todo
Scenario: Capturing an image
    Given I browse to: /view/
    And I click the capture button
    And I should see an image in the page

@todo
Scenario: Viewing an image in the page
    Given I obtain the following image from the camera:
        filename.gif
    And I browse to: /view/
    Then I should see the following image:
        filename.gif

@todo
Scenario: Camera throws an exception on unexpected capture data
    Given the camera recieves corrupt data
    Then the camera raises a ValueError exception
