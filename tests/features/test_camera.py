# coding=utf-8
"""Interfacing with the camera feature tests."""
import os

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from chickenstrumentation.camera import Reader

@scenario('camera.feature', 'Obtain images from the camera')
def test_obtain_image_from_camera():
    """Obtain image from camera."""

@scenario('camera.feature', 'Obtain video from the camera')
def test_obtain_video_from_camera():
        """Obtain video from camera."""

@given('I have a mock camera', target_fixture="mock_camera")
def i_have_a_mock_camera(mocker):
    """I have a mock camera"""
    mocker.patch.object(Reader, 'capture_image', autospec=True)
    mocker.patch.object(Reader, 'capture_video', autospec=True)
    mock_camera = Reader()
    return mock_camera

@when('I take a picture')
def the_camera_takes_a_picture(mock_camera):
    """I take a picture"""
    mock_camera.capture_image()

@when('I record a video')
def i_record_a_video(mock_camera):
    """I record a video"""
    mock_camera.capture_video()

# TODO: Fins a way to pass in the method name
@then("The capture_image() method is called")
def the_capture_image_method_is_called(mock_camera):
   mock_camera.capture_image.assert_called_once_with(mock_camera) 

@then("The capture_video() method is called")
def the_capture_video_method_is_called(mock_camera):
   mock_camera.capture_video.assert_called_once_with(mock_camera) 

@given('An image is obtained from the camera', target_fixture="capture_image")
def an_image_is_obtained_from_the_camera(camera):
    """An image is obtained from the camera."""
    image_path = camera.get_image()
    return image_path

@then('The image should be saved to a file')
def the_image_is_saved_to_a_file(capture_image):
    """The image should be saved to a file"""
    assert os.path.exists(capture_image)

