# coding=utf-8
"""Camera imaging in web page feature tests."""

from chickenstrumentation.camera import Reader

import re
import os
from bs4 import BeautifulSoup

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)


@scenario('gui_image.feature', 'Viewing the page')
def test_viewing_the_page():
    """Viewing the page."""


@given(parsers.parse('I want to interact with web page: {route}'), target_fixture="brower")
def interact_with_page(server, route, browser):
    print "Interact with page: {}".format(route)
    url = server.check_url + route
    print url
    browser.get(url)
    browser.save_screenshot('screenshot.png')

@when("I click the capture button")
def i_click_the_capture_button(server, browser):
    pass

@then(parsers.parse("I should see an image in div id: {div_id}"))
def i_should_see_an_image_in(div_id):
    pass

@given(parsers.parse('I browse to: {route}'), target_fixture="page_response")
def i_browse_to_view(route, client):
    """I browse to: route."""
    rv = client.get(route)
    return rv

#@given('I obtain a capture image')
@given('I obtain a capture image', target_fixture="capture_image")
def i_obtain_a_capture_image(camera):
    """I obtain a capture image."""
    image_path = camera.get_image()
    assert os.path.exists(image_path)
    return image_path

@then(parsers.parse('I should have a div with id: {div_id}'))
def i_should_have_a_div_with_id_capture(page_response, div_id, capture_image):
    """I should have a div with id: capture."""
    html_doc = page_response.data
    soup = BeautifulSoup(html_doc, 'html.parser')
    assert soup.find("div", {"id": div_id})
    assert os.path.exists(capture_image)


