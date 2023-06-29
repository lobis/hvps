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
from typing import List, Set

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
        _get_mon_module_command("TEST")

    command = _get_mon_module_command(":READ:MODULE:EVENT:MASK")
    assert command == b":READ:MODULE:EVENT:MASK?\r\n"


def test_iseg_module_set_commands():
    with pytest.raises(ValueError):
        # invalid parameter name
        _get_set_module_command("TEST", 16)

    command = _get_set_module_command(":CONF:AVER", 16)
    assert command == b":CONF:AVER 16;*OPC?\r\n"


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
        _get_set_channel_command(0, "TEST", 0)

    with pytest.raises(ValueError):
        # invalid channel number
        _get_set_channel_command(-1, ":VOLT:BOUNDS", 10)

    command = _get_set_channel_command(0, ":VOLT:BOUNDS", 10)
    assert command == b":VOLT:BOUNDS 10,(@0);*OPC?\r\n"


def test_iseg_parse_response():
    response = b"1\r\n"
    parsed_response = _parse_response(response, None)
    assert parsed_response == ["1"]

    response = b"p,n\r\n"
    parsed_response = _parse_response(response, List[str])
    assert parsed_response == ["p", "n"]

    response = b"p\r\n"
    parsed_response = _parse_response(response, str)
    assert parsed_response == ["p"]

    response = b"1.23400E3\r\n"
    parsed_response = _parse_response(response, float)
    assert parsed_response == ["1.23400E3"]

    response = b"132\r\n"
    parsed_response = _parse_response(response, int)
    assert parsed_response == ["132"]

    # non-supported type
    with pytest.raises(ValueError):
        _parse_response(b"{1, 2}", Set[int])

    # type missmatch
    with pytest.raises(ValueError):
        _parse_response(b"1.23400E^3", float)
