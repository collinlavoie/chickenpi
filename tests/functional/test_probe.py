# coding=utf-8
"""Temperature probe feature tests."""

import ast

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)

from chickenstrumentation.probe import Reader

@scenario('../features/device/probe.feature', 'Obtaining temperature from the probes')
def test_obtaining_temperature():
    """Obtaining temperature."""

@scenario('../features/device/probe.feature', 'Obtaining bad data from the probes')
def test_obtaining_bad_data():
    """Obtaining bad data from the probes."""

@scenario('../features/device/probe.feature', 'Obtaining good and bad data from the probes')
def test_obtaining_good_and_bad_data():
    """Obtaining good and bad data from the probes."""

@given('I have a mock probe')
def mock_probe(mocker):
    """I have a probe."""
    mocker.patch("chickenstrumentation.probe.Reader.read_probes")
    return Reader

@given(parsers.parse('I obtain the reading:\n{reading}'))
def data_output(mock_probe, reading):
    """I obtain the temperature reading."""
    mock_probe.read_probes.return_value = reading
    data_output = mock_probe.get_data()
    mock_probe.read_probes.assert_called_once_with()
    return data_output


@then(parsers.parse('I obtain the following data:\n{string_data}'))
def data_does_not_have_pattern(data_output, string_data):
    """I obtain the following data."""
    data = ast.literal_eval(string_data)
    assert data == data_output


