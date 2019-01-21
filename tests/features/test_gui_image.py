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


@given('I access the page', target_fixture="page_response")
def i_access_the_page(mocker, client):
    """I access the page."""
    rv = client.get('/temp/')
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


