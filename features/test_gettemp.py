# coding=utf-8
"""Temp feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('gettemp.feature', 'Obtaining the tempaerature')
def test_obtaining_the_tempaerature():
    """Obtaining the tempaerature."""


@given('That the temperature is 5 Celcius')
def that_the_temperature_is_5_celcius():
    """That the temperature is 5 Celcius."""


@when('I go to the temp page')
def i_go_to_the_temp_page():
    """I go to the temp page."""


@then('I should see 5 Celcius')
def i_should_see_5_celcius():
    """I should see 5 Celcius."""

