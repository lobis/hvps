import pytest


from hvps.commands.caen import (
    _parse_response,
    _get_set_module_command,
    _get_mon_module_command,
    _get_set_channel_command,
    _get_mon_channel_command,
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
    def test_caen_module_set_commands():
        with pytest.raises(ValueError):
            # invalid parameter name
            _get_set_module_command(0, "TEST", 10)

        with pytest.raises(ValueError):
            # invalid board number
            _get_set_module_command(-1, "BDNAME", 10)

        command = _get_set_module_command(0, "BDNAME", 10)
        assert command == b"$BD:00,CMD:SET,PAR:BDNAME,VAL:10\r\n"


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
    response = b"#BD:01,CMD:OK,VAL:42"
    result = _parse_response(response, bd=1)
    assert result == "42"

    response = b"#BD:99,CMD:OK,VAL:Hello World"
    result = _parse_response(response, bd=99)
    assert result == "Hello World"

    with pytest.raises(ValueError):
        # Invalid response format
        response = b"Invalid response"
        _parse_response(response)

    with pytest.raises(ValueError):
        # Mismatched bd value
        response = b"#BD:42,CMD:OK,VAL:Invalid"
        _parse_response(response, bd=99)
