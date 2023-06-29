import pytest

from hvps.commands.caen import _parse_response
from hvps.commands.caen.channel import (
    _get_set_channel_command,
    _get_mon_channel_command,
)

from hvps.commands.caen.module import (
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
    assert command == b"$BD:00,CMD:MON,PAR:BDNAME\r\n"


def test_caen_module_set_commands():
    with pytest.raises(ValueError):
        # invalid parameter name
        _get_set_module_command(0, "TEST", 10)

    with pytest.raises(ValueError):
        # invalid board number
        _get_set_module_command(-1, "BDILKM", 10)

    command = _get_set_module_command(0, "BDILKM", 10)
    assert command == b"$BD:00,CMD:SET,PAR:BDILKM,VAL:10\r\n"


def test_caen_channel_get_commands():
    with pytest.raises(ValueError):
        # invalid parameter name
        _get_mon_channel_command(0, 1, "TEST")

    with pytest.raises(ValueError):
        # invalid board number
        _get_mon_channel_command(-1, 1, "BDNAME")

    with pytest.raises(ValueError):
        # invalid channel number
        _get_mon_channel_command(0, -1, "BDNAME")

    command = _get_mon_channel_command(0, 1, "VSET")
    assert command == b"$BD:00,CMD:MON,CH:1,PAR:VSET\r\n"


def test_caen_channel_set_commands():
    with pytest.raises(ValueError):
        # invalid parameter name
        _get_set_channel_command(0, 1, "TEST", 10)

    with pytest.raises(ValueError):
        # invalid parameter value
        _get_set_channel_command(0, 1, "IMRANGE", "INVALID")

    with pytest.raises(ValueError):
        # invalid board number
        _get_mon_channel_command(-1, 1, "BDNAME")

    with pytest.raises(ValueError):
        # invalid channel number
        _get_mon_channel_command(0, -1, "BDNAME")

    command = _get_set_channel_command(0, 1, "ON", None)
    assert command == b"$BD:00,CMD:SET,CH:1,PAR:ON\r\n"

    command = _get_set_channel_command(0, 1, "IMRANGE", "LOW")
    assert command == b"$BD:00,CMD:SET,CH:1,PAR:IMRANGE,VAL:LOW\r\n"

    command = _get_set_channel_command(0, 1, "PDWN", "KILL")
    assert command == b"$BD:00,CMD:SET,CH:1,PAR:PDWN,VAL:KILL\r\n"


def test_caen_parse_response():
    response = b"#BD:01,CMD:OK,VAL:42\r\n"
    bd, value = _parse_response(response)
    assert bd == 1
    assert value == "42"

    response = b"#BD:99,CMD:OK,VAL:Hello World\r\n"
    bd, value = _parse_response(response)
    assert bd == 99
    assert value == "Hello World"

    with pytest.raises(ValueError):
        # Invalid response format
        response = b"Invalid response\r\n"
        _parse_response(response)

    response = b"#BD:09,CMD:OK\r\n"
    bd, value = _parse_response(response)
    assert bd == 9
    assert value is None

    with pytest.raises(ValueError):
        # number needs to be two digits
        response = b"#BD:9,CMD:OK\r\n"
        _parse_response(response)

    with pytest.raises(ValueError):
        # add additional ','
        response = b"#BD:9,CMD:OK,\r\n"
        _parse_response(response)
