# coding=utf-8
"""Temperature web page feature tests."""

from chickenstrumentation.probe import WebReader
import pytest
import re

from bs4 import BeautifulSoup

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('gui_resource.feature', 'Viewing the page')
def test_viewing_the_page():
    """Viewing the page."""

# Fixtures

@given('I access the webpage')
def i_access_the_webpage(client, mocker):
    """I obtain the temperature reading."""

    rv = client.get('/web_temp/')
    html_doc = rv.data
    soup = BeautifulSoup(html_doc, 'html.parser')
    assert soup.find("div", {"id": "temp"})
    expected_pattern = ur'-?\d+\.\d+ \u2103'
    assert re.match(expected_pattern, soup.find("div", {"id": "temp"}).text)


@when('I obtain the list of div elements')
def i_obtain_the_list_of_div_elements():
    """I obtain the list of div elements."""


@then('I should have a div with id "temperature"')
def i_should_have_a_div_with_id_temperature():
    """I should have a div with id "temperature"."""

