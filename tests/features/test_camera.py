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

@scenario('camera.feature', 'Obtain image from camera')
def test_obtain_image_from_camera():
    """Obtain image from camera."""


#@given('The camera takes a picture')
#def the_camera_takes_a_picture(mocker):
#    """An image is obtained from the camera."""
#    mocker.patch("chickenstrumentation.camera.Reader.capture_image")
#    image = Reader.get_image()
#    print image
#    Reader.capture_image.assert_called_once_with()

@given('An image is obtained from the camera')
def an_image_is_obtained_from_the_camera():
    """An image is obtained from the camera."""
    image_path = Reader.get_image()
    assert os.path.exists(image_path)
    return image_path

@when('I access the webpage')
def i_access_the_webpage():
    """I access the webpage."""


@then('I should see the image')
def i_should_see_the_image():
    """I should see the image."""

