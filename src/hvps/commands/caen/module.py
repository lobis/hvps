from __future__ import annotations

from types import NoneType

from utils import check_command_input

# Dictionary mapping monitor module commands to their descriptions
_MON_MODULE_COMMANDS = {
    "BDNAME": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Read out module name (N1471)",
    },
    "BDNCH": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out number of Channels present",
    },
    "BDFREL": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Read out Firmware Release (XX.X)",
    },
    "BDSNUM": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Read out value serial number (XXXXX)",
    },
    "BDILK": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["YES", "NO"],
        "description": "Read out INTERLOCK status (YES/NO)",
    },
    "BDILKM": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["OPEN, CLOSED"],
        "description": "Read out INTERLOCK mode (OPEN/CLOSED)",
    },
    "BDCTR": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["LOCAL", "REMOTE"],
        "description": "Read out Control Mode (LOCAL/REMOTE)",
    },
    "BDTERM": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["ON", "OFF"],
        "description": "Read out LOCAL BUS Termination status (ON/OFF)",
    },
    "BDALARM": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out Board Alarm status value (XXXXX)",
    },
}

# Dictionary mapping set module commands to their descriptions
_SET_MODULE_COMMANDS = {
    "BDILKM": {
        "input_type": str,
        "allowed_input_values": ["OPEN", "CLOSED"],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Set Interlock Mode",
    },
    "BDCLR": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Clear alarm signal",
    },
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

    check_command_input(_MON_MODULE_COMMANDS, command)

    command = command.upper()
    if command not in _MON_MODULE_COMMANDS:
        valid_commands = ", ".join(_MON_MODULE_COMMANDS.keys())
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

    check_command_input(_SET_MODULE_COMMANDS, command, value)

    command = command.upper()

    return f"$BD:{bd:02d},CMD:SET,PAR:{command},VAL:{value}\r\n".encode("utf-8")
