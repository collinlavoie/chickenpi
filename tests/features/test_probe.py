# coding=utf-8
"""Temperature probe feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from chickenstrumentation.probe import Reader

@scenario('probe.feature', 'Obtaining temperature')
def test_obtaining_temperature():
    """Obtaining temperature."""

@given('I have a probe')
def i_have_a_probe():
    """I have a probe."""


@when('I obtain the temperature reading')
def i_obtain_the_temperature_reading(mocker):
    """I obtain the temperature reading."""
    mocker.patch("chickenstrumentation.probe.Reader.read_probes")
    data = Reader.get_data()
    Reader.read_probes.assert_called_once_with()


@then('I should obtain the temperature')
def i_should_obtain_the_temperature():
    """I should obtain the temperature."""

