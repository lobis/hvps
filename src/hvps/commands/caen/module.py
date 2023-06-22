from __future__ import annotations

# Dictionary mapping monitor module parameters to their descriptions
_mon_module_parameters = {
    "BDNAME": "Read out module name (N1471)",
    "BDNCH": "Read out number of Channels present (4)",
    "BDFREL": "Read out Firmware Release (XX.X)",
    "BDSNUM": "Read out value serial number (XXXXX)",
    "BDILK": "Read out INTERLOCK status (YES/NO)",
    "BDILKM": "Read out INTERLOCK mode (OPEN/CLOSED)",
    "BDCTR": "Read out Control Mode (LOCAL/REMOTE)",
    "BDTERM": "Read out LOCAL BUS Termination status (ON/OFF)",
    "BDALARM": "Read out Board Alarm status value (XXXXX)",
}

# Dictionary mapping set module parameters to their descriptions
_set_module_parameters = {
    "BDILKM": "VAL:OPEN/CLOSED Set Interlock Mode",
    "BDCLR": "Clear alarm signal",
}


def _get_mon_module_command(bd: int, command: str) -> bytes:
    """
    Generate a command string to monitor a specific module parameter.

    Args:
        bd (int): The board number. Must be in the range 0..31.
        command (str): The parameter to monitor.

    Returns:
        bytes: The command string encoded as bytes.

    Raises:
        ValueError: If the provided parameter is not valid.
    """
    if not 0 <= bd <= 31:
        raise ValueError(f"Invalid board number '{bd}'. Must be in the range 0..31.")

    command = command.upper()
    if command not in _mon_module_parameters:
        valid_parameters = ", ".join(_mon_module_parameters.keys())
        raise ValueError(
            f"Invalid parameter '{command}'. Valid parameters are: {valid_parameters}"
        )
    return f"$BD:{bd:02d},CMD:MON,PAR:{command}\r\n".encode("utf-8")


def _get_set_module_command(
    bd: int, command: str, value: str | int | float | None
) -> bytes:
    """
    Generate a command string to set a specific module parameter to a given value.

    Args:
        bd (int): The board number.
        command (str): The parameter to set.
        value (str | int | float): The value to set the parameter to.

    Returns:
        bytes: The command string encoded as bytes.

    Raises:
        ValueError: If the provided parameter or value is not valid.
    """
    if not 0 <= bd <= 31:
        raise ValueError(f"Invalid board number '{bd}'. Must be in the range 0..31.")

    command = command.upper()
    if command not in _set_module_parameters:
        valid_parameters = ", ".join(_set_module_parameters.keys())
        raise ValueError(
            f"Invalid parameter '{command}'. Valid parameters are: {valid_parameters}"
        )
    if value is None:
        if command not in ["BDCLR"]:
            raise ValueError(f"Value must be provided for parameter '{command}'.")

    return f"$BD:{bd:02d},CMD:SET,PAR:{command},VAL:{value}\r\n".encode("utf-8")
