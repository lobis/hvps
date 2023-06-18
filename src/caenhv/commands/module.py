from __future__ import annotations

# Dictionary mapping monitor module parameters to their descriptions
_mon_module_parameters = {
    "BDNAME": "Read out module name (N1471)",
    "BDNCH": "Read out number of Channels present (4)",
    "BDFREL": "Read out Firmware Release (XX.X)",
    "BDSNUM": "Read out value serial number (XXXXX)",
    "BDILK": "Read out INTERLOCK status (YES/NO)",
    "BDILKM": "Read out INTERLOCK mode (OPEN/CLOSED)",
    "BDCTR": "Read out Control Mode (LOCAL / REMOTE)",
    "BDTERM": "Read out LOCAL BUS Termination status (ON/OFF)",
    "BDALARM": "Read out Board Alarm status value (XXXXX)",
}

# Dictionary mapping set module parameters to their descriptions
_set_module_parameters = {
    "BDILKM": "VAL:OPEN/CLOSED Set Interlock Mode",
    "BDCLR": "Clear alarm signal",
}


def _get_mon_module_command(bd: int, parameter: str) -> bytes:
    """
    Generate a command string to monitor a specific module parameter.

    Args:
        bd (int): The board number.
        parameter (str): The parameter to monitor.

    Returns:
        bytes: The command string encoded as bytes.

    Raises:
        ValueError: If the provided parameter is not valid.
    """
    parameter = parameter.upper()
    if parameter not in _mon_module_parameters:
        valid_parameters = ", ".join(_mon_module_parameters.keys())
        raise ValueError(
            f"Invalid parameter '{parameter}'. Valid parameters are: {valid_parameters}"
        )
    return f"$BD:{bd:02d},CMD:MON,PAR:{parameter}\r\n".encode("utf-8")


def _get_set_module_command(bd: int, parameter: str, value: str | int | float) -> bytes:
    """
    Generate a command string to set a specific module parameter to a given value.

    Args:
        bd (int): The board number.
        parameter (str): The parameter to set.
        value (str | int | float): The value to set the parameter to.

    Returns:
        bytes: The command string encoded as bytes.

    Raises:
        ValueError: If the provided parameter or value is not valid.
    """
    parameter = parameter.upper()
    if parameter not in _set_module_parameters:
        valid_parameters = ", ".join(_set_module_parameters.keys())
        raise ValueError(
            f"Invalid parameter '{parameter}'. Valid parameters are: {valid_parameters}"
        )
    return f"$BD:{bd:02d},CMD:SET,PAR:{parameter},VAL:{value}\r\n".encode("utf-8")
