Feature: Interfacing with the camera
    The camera captures images and video

Scenario: Obtain images from the camera
    Given I have a mock camera
    When I take a picture
    Then The capture_image() method is called

Scenario: Obtain video from the camera
    Given I have a mock camera
    When I record a video
    Then The capture_video() method is called

Scenario: Obtain images from the camera
    Given An image is obtained from the camera
    Then The image should be saved to a file
