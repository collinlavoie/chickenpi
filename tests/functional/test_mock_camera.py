# coding=utf-8
"""Interfacing with the camera feature tests."""
import os

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)

from chickenstrumentation.camera import Reader

#@scenario('../features/device/camera.feature', 'Obtain video from the camera')
#def test_obtain_video_from_camera():
#        """Obtain video from camera."""

@given('I have a mock camera', target_fixture="mock_camera")
def i_have_a_mock_camera(mocker):
    """I have a mock camera"""
    mocker.patch.object(Reader, 'capture_image', autospec=True)
    mocker.patch.object(Reader, 'capture_video', autospec=True)
    mock_camera = Reader()
    return mock_camera

@when('I take a mock picture')
def the_camera_takes_a_picture(mock_camera):
    """I take a picture"""
    mock_camera.capture_image()

@when('I record a mock video')
def i_record_a_video(mock_camera):
    """I record a video"""
    mock_camera.capture_video()

@then(parsers.parse("The {name}() method is called"))
def the_capture_image_method_is_called(mock_camera, name):
    getattr(mock_camera, name).assert_called_once_with(mock_camera)
