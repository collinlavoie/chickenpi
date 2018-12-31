# coding=utf-8
"""Temperature web page feature tests."""

import pytest
import re

from bs4 import BeautifulSoup

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('gui.feature', 'Viewing the page')
def test_viewing_the_page():
    """Viewing the page."""

# Fixtures
 
@given('I access the webpage')
def i_access_the_webpage(client):
    """I access the webpage."""
    """Start with a blank database."""

    rv = client.get('/temp/')
    html_doc = rv.data
    soup = BeautifulSoup(html_doc, 'html.parser')
    expected = ur'\d+\.\d+ \u2103'
    actual = soup.find("div", {"id": "temp"}).text

    assert re.match(expected, actual)

@when('I obtain the list of div elements')
def i_obtain_the_list_of_div_elements():
    """I obtain the list of div elements."""


@then('I should have a div with id "temperature"')
def i_should_have_a_div_with_id_temperature():
    """I should have a div with id "temperature"."""

