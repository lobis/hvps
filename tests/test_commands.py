import pytest

from hvps.commands.caen import _parse_response, _get_set_module_command, _get_mon_module_command


def test_caen_channel_commands():
    with pytest.raises(ValueError):
        # invalid parameter name
        _get_mon_module_command(0, "TEST")

    with pytest.raises(ValueError):
        # invalid board number
        _get_mon_module_command(-1, "BDNAME")

    command = _get_mon_module_command(0, "BDNAME")
