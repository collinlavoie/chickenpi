# coding=utf-8
"""Camera imaging in web page feature tests."""

from chickenstrumentation.camera import Reader

import re
import os
import time
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)

#@scenario('../features/gui/image.feature', 'Capture image route')
#def test_capture_image_route():
#    """Capture image route."""

@scenario('../features/gui/image.feature', 'Clicking capture button displays an image in the page')
def test_click_capture_displays_image():
    """Viewing the page."""

@scenario('../features/gui/image.feature', 'Capturing an image')
def test_capturing_an_image():
    """Capturing an image."""

#@given('I have a mock camera', target_fixture="mock_camera")
#def i_have_a_mock_camera(mocker):
#    """I have a mock camera"""
    #mocker.patch.object(Reader, 'capture_image', autospec=True)
    #mocker.patch.object(Reader, 'capture_video', autospec=True)
    #mocker.patch("chickenstrumentation.camera.Reader.capture_image")
    #mock_camera = Reader()
    #return mock_camera

@given(parsers.parse('I interact with web page: {route}'), target_fixture="brower")
def interact_with_page(server, route, browser):
    url = server.check_url + route
    browser.get(url)
    return browser

@when("I click the capture button")
def i_click_the_capture_button(interact_with_page):
    interact_with_page.save_screenshot('{}.before.click.capture.link.png'.format(
        time.strftime("%Y%m%dT%Hh%Mm%Ss")))
    interact_with_page.find_element_by_id("capture").click()

@when("The mock camera captures an image")
def the_mock_camera_captures_an_image(mock_camera):
    return mock_camera.get_image()

@then('I should see an image in the page')
def I_should_see_an_image_in_the_page(interact_with_page):
    interact_with_page.save_screenshot('{}.after.click.capture.link.png'.format(
        time.strftime("%Y%m%dT%Hh%Mm%Ss")))
    capture_div = interact_with_page.find_element_by_id("capture")


@then(parsers.parse("I should see an image in div id: {div_id}"))
def i_should_see_an_image_in(div_id, interact_with_page):
    interact_with_page.save_screenshot('{}.after.click.capture.link_x.png'.format(
        time.strftime("%Y%m%dT%Hh%Mm%Ss")))

@given(parsers.parse('I browse to: {route}'), target_fixture="page_response")
def i_browse_to_view(route, client):
    """I browse to: route."""
    rv = client.get(route)
    return rv

@given('I obtain a capture image', target_fixture="capture_image")
def i_obtain_a_capture_image(camera):
    """I obtain a capture image."""
    image_path = camera.get_image()
    assert os.path.exists(image_path)
    return image_path

@then(parsers.parse('I should have a div with id: {div_id}'))
def i_should_have_a_div_with_id_capture(page_response, div_id):
    """I should have a div with id: capture."""
    html_doc = page_response.data
    soup = BeautifulSoup(html_doc, 'html.parser')
    assert soup.find("div", {"id": div_id})

@given('The app uses a mock camera')
def the_app_uses_a_mock_camera(mocker, mock_camera):
    """The app uses a mock camera"""
    mocker.patch("chickenstrumentation.app.camera.Reader.capture_image",
                 side_effect=mock_camera.capture_image)

@then('I should see a path to a captured image')
def i_should_see_a_path_to_a_captured_image(page_response):
    """I should see a path to a captured image."""
    image_path = page_response.data
    assert os.path.exists(image_path)
