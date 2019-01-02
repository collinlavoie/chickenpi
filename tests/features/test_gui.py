# coding=utf-8
"""Temperature web page feature tests."""

from chickenstrumentation.probe import Reader
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
def i_access_the_webpage(client, mocker):
    """I obtain the temperature reading."""

    output=[{"sensor": "28-000007a81e55",
           "temp": "6.500",
           "time": "2019-01-08 23:05:02"}]
    mocker.patch("chickenstrumentation.app.probe.Reader.get_data")
    Reader.get_data.return_value = output

    rv = client.get('/temp/')
    html_doc = rv.data
    soup = BeautifulSoup(html_doc, 'html.parser')
    Reader.get_data.assert_called_once_with()
    assert soup.find("div", {"id": "temp"})
    expected = ur'\d+\.\d+ \u2103'
    assert re.match(expected, soup.find("div", {"id": "temp"}).text)
    assert re.match(ur"6.50 \u2103", soup.find("div", {"id": "temp"}).text)


@when('I obtain the list of div elements')
def i_obtain_the_list_of_div_elements():
    """I obtain the list of div elements."""


@then('I should have a div with id "temperature"')
def i_should_have_a_div_with_id_temperature():
    """I should have a div with id "temperature"."""

