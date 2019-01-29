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
    parsers,
)

@scenario('../features/gui/temp.feature', 'Temperature probe reading displayed in web page')
def test_probe_reading_displayed_in_web_page():
    """Viewing the page."""

# Fixtures

@given(parsers.parse('The probes read:\n{text}'))
@given(parsers.parse('The probes read: {text}'))
def probes_reading(mocker, text):
    mocker.patch("chickenstrumentation.app.probe.Reader.read_probes")
    Reader.read_probes.return_value = text

@given(parsers.parse('I browse to: {route}'), target_fixture="page_response")
def i_browse_to_view(client, route):
    rv = client.get(route)
    return rv

@then(parsers.parse('I should have a div with id: {div_id}'))
def i_have_div_with_id(page_response, div_id):
    html_doc = page_response.data
    soup = BeautifulSoup(html_doc, 'html.parser')
    assert soup.find("div", {"id": div_id})

@then(parsers.parse('I should see temperature: {temp}'))
def i_should_see_temperature(page_response, temp):
    html_doc = page_response.data
    soup = BeautifulSoup(html_doc, 'html.parser')
    assert re.match(ur"{} \u2103".format(temp), soup.find("div", {"id": "temp"}).text)

@then('I should see a temperature reading')
def i_see_a_temp_reading(page_response):
    html_doc = page_response.data
    soup = BeautifulSoup(html_doc, 'html.parser')
    expected = ur'\d+\.\d+ \u2103'
    assert re.match(expected, soup.find("div", {"id": "temp"}).text)
