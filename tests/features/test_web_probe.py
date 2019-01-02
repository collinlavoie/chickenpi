# coding=utf-8
"""Temperature probe feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from chickenstrumentation.probe import WebReader

@scenario('probe.feature', 'Obtaining temperature from web resource')
def test_obtaining_temperature():
    """Obtaining temperature."""

@given('I have a probe')
def i_have_a_probe():
    """I have a probe."""

@given('I obtain data from a web resource')
def i_obtain_the_temperature_reading(mocker):
    """I obtain the temperature reading."""
    mocker.patch("chickenstrumentation.probe.WebReader.read_probes")
    data = WebReader.get_data()
    WebReader.read_probes.assert_called_once_with()

@when('I obtain the temperature reading')

@then('I should obtain the temperature')
def i_should_obtain_the_temperature():
    """I should obtain the temperature."""
