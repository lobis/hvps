from __future__ import annotations

# Dictionary mapping monitor module commands to their descriptions
_mon_module_commands = {
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

# Dictionary mapping set module commands to their descriptions
_set_module_commands = {
    "BDILKM": "VAL:OPEN/CLOSED Set Interlock Mode",
    "BDCLR": "Clear alarm signal",
}


def _get_mon_module_command(bd: int, command: str) -> bytes:
    """
    Generate a command string to monitor a specific module command.

    Args:
        bd (int): The board number. Must be in the range 0..31.
        command (str): The command to monitor.

    Returns:
        bytes: The command string encoded as bytes.

    Raises:
        ValueError: If the provided command is not valid.
    """
    if not 0 <= bd <= 31:
        raise ValueError(f"Invalid board number '{bd}'. Must be in the range 0..31.")

    command = command.upper()
    if command not in _mon_module_commands:
        valid_commands = ", ".join(_mon_module_commands.keys())
        raise ValueError(
            f"Invalid command '{command}'. Valid commands are: {valid_commands}"
        )
    return f"$BD:{bd:02d},CMD:MON,PAR:{command}\r\n".encode("utf-8")


def _get_set_module_command(
    bd: int, command: str, value: str | int | float | None
) -> bytes:
    """
    Generate a command string to set a specific module command to a given value.

    Args:
        bd (int): The board number.
        command (str): The command to set.
        value (str | int | float): The value to set the command to.

    Returns:
        bytes: The command string encoded as bytes.

    Raises:
        ValueError: If the provided command or value is not valid.
    """
    if not 0 <= bd <= 31:
        raise ValueError(f"Invalid board number '{bd}'. Must be in the range 0..31.")

    command = command.upper()
    if command not in _set_module_commands:
        valid_commands = ", ".join(_set_module_commands.keys())
        raise ValueError(
            f"Invalid command '{command}'. Valid commands are: {valid_commands}"
        )
    return f"$BD:{bd:02d},CMD:SET,PAR:{command},VAL:{value}\r\n".encode("utf-8")
