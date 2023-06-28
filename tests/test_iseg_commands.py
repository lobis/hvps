"""
trip_action: 4
output_mode: 1
output_polarity: p
available_output_polarities: ['p', 'n']
voltage_set: 210.0
voltage_limit: 1955.292
voltage_nominal: 2000.0
available_output_modes: [1]
"""

import pytest
from typing import List

from hvps.commands.iseg import _parse_response
from hvps.commands.iseg.channel import (
    _get_set_channel_command,
    _get_mon_channel_command,
)

from hvps.commands.iseg.module import (
    _get_set_module_command,
    _get_mon_module_command,
)


# TODO: validate commands generation and response parsing


def test_iseg_module_get_commands():
    with pytest.raises(ValueError):
        # invalid parameter name
        _get_mon_module_command(":READ:MODULE:EVENT:MASK")

    command = _get_mon_module_command(":READ:MODULE:EVENT:MASK")
    assert command == b":READ:MODULE:EVENT:MASK? (@0)\r\n"


def test_iseg_module_set_commands():
    with pytest.raises(ValueError):
        # invalid parameter name
        _get_set_module_command("TEST", 16)

    with pytest.raises(ValueError):
        # invalid argument value
        _get_set_module_command(":CONF:AVER", 15)

    command = _get_set_module_command(":CONF:AVER", 16)
    assert command == b":CONF:AVER 16,(@0);*OPC?\r\n"


def test_iseg_channel_get_commands():
    with pytest.raises(ValueError):
        # invalid parameter name
        _get_mon_channel_command(0, "TEST")

    with pytest.raises(ValueError):
        # invalid channel number
        _get_mon_channel_command(-1, ":CONF:OUTPUT:POL:LIST")

    command = _get_mon_channel_command(0, ":CONF:OUTPUT:POL:LIST")
    assert command == b":CONF:OUTPUT:POL:LIST? (@0)\r\n"


def test_iseg_channel_set_commands():
    with pytest.raises(ValueError):
        # invalid parameter name
        _get_set_channel_command(0, "TEST")

    with pytest.raises(ValueError):
        # invalid argument value
        _get_set_channel_command(0, ":CONF:OUTPUT:POL", "v")

    with pytest.raises(ValueError):
        # invalid channel number
        _get_set_channel_command(-1, ":VOLT:BOUNDS", 10)

    command = _get_set_channel_command(0, ":VOLT:BOUNDS", 10)
    assert command == b":VOLT:BOUNDS 10,(@0);*OPC?\r\n"


def test_iseg_parse_response():
    response = b":VOLT:BOUNDS 10,(@0);*OPC?\r\n1\r\n"
    parsed_response = _parse_response(response, None)
    assert parsed_response == [1]

    response = b":CONF:OUTPUT:POL:LIST? (@0)\r\np,n\r\n"
    parsed_response = _parse_response(response, List[str])
    assert parsed_response == ["p", "n"]

    response = b":CONF:OUTPUT:POL? (@0)\r\np\r\n"
    parsed_response = _parse_response(response, str)
    assert parsed_response == ["p"]

    response = b":READ:VOLT?(@0)\r\n1.23400E3\r\n"
    parsed_response = _parse_response(response, float)
    assert parsed_response == [1.23400e3]

    response = b":READ:CHAN:STATUS?(@0)\r\n132\r\n"
    parsed_response = _parse_response(response, int)
    assert parsed_response == [132]
