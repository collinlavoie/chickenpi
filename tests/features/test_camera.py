# coding=utf-8
"""Interfacing with the camera feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('camera.feature', 'Obtain image from camera')
def test_obtain_image_from_camera():
    """Obtain image from camera."""


@given('An image is obtained from the camera')
def an_image_is_obtained_from_the_camera():
    """An image is obtained from the camera."""
    mocker.patch("chickenstrumentation.camera.Reader.get_image")
    image = Reader.get_image()
    Reader.read_probes.assert_called_once_with()

@when('I access the webpage')
def i_access_the_webpage():
    """I access the webpage."""


@then('I should see the image')
def i_should_see_the_image():
    """I should see the image."""

