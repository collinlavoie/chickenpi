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

@scenario('gui.feature', 'Viewing the page')
def test_viewing_the_page():
    """Viewing the page."""

# Fixtures

@given('The probes read 123')
def the_probes_read_123():
    """The probes read 123"""


@given(parsers.parse('The probes read:\n{text}'))
@given(parsers.parse('The probes read: {text}'))
def probes_reading(text):
    return text

@given('I access the page', target_fixture="page_response")
def i_access_the_page(mocker, client, probes_reading):
    mocker.patch("chickenstrumentation.app.probe.Reader.read_probes")
    Reader.read_probes.return_value = probes_reading
    rv = client.get('/temp/')
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
    assert re.match(ur"1.12 \u2103", soup.find("div", {"id": "temp"}).text)

@then('I should see a temperature reading')
def i_see_a_temp_reading(page_response):
    html_doc = page_response.data
    soup = BeautifulSoup(html_doc, 'html.parser')
    expected = ur'\d+\.\d+ \u2103'
    assert re.match(expected, soup.find("div", {"id": "temp"}).text)
