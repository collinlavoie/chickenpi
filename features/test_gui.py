# coding=utf-8
"""Temperature web page feature tests."""

import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys

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
 
@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    b = Firefox(options=options)
    b.implicitly_wait(10)
    yield b
    b.quit()


@given('I access the webpage')
def i_access_the_webpage(browser):
    """I access the webpage."""
    browser.get("http://192.168.250.20")

@when('I obtain the list of div elements')
def i_obtain_the_list_of_div_elements():
    """I obtain the list of div elements."""


@then('I should have a div with id "temperature"')
def i_should_have_a_div_with_id_temperature():
    """I should have a div with id "temperature"."""

