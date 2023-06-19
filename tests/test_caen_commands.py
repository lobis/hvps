import pytest

from hvps.commands.caen import (
    _parse_response,
    _get_set_module_command,
    _get_mon_module_command,
)


def test_caen_module_get_commands():
    with pytest.raises(ValueError):
        # invalid parameter name
        _get_mon_module_command(0, "TEST")

    with pytest.raises(ValueError):
        # invalid board number
        _get_mon_module_command(-1, "BDNAME")

    command = _get_mon_module_command(0, "BDNAME")


def test_caen_module_set_commands():
    pass


def test_caen_channel_get_commands():
    pass


def test_caen_channel_set_commands():
    pass


def test_caen_parse_response():
    pass
