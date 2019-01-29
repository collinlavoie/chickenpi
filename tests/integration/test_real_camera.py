# coding=utf-8
"""Interfacing with the camera feature tests."""
import os
from chickenstrumentation.app import app

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from chickenstrumentation.camera import Reader

@scenario('../features/device/camera.feature', 'Obtain images from a real camera')
def test_obtain_image_from_camera():
    """Obtain image from camera."""

@scenario('../features/device/camera.feature', 'Obtain video from a real camera')
def test_obtain_video_from_camera():
        """Obtain video from camera."""

@given('An image is obtained from the camera', target_fixture="capture_image")
def an_image_is_obtained_from_the_camera(camera):
    """An image is obtained from the camera."""
    image_path = camera.get_image()
    return image_path

@then('The image should be saved to a file')
def the_image_is_saved_to_a_file(capture_image):
    """The image should be saved to a file"""
    assert os.path.exists(os.path.join(app.config['CAMERA'], capture_image))

