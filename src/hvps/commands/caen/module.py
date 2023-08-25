from __future__ import annotations


# Dictionary mapping monitor module commands to their descriptions
_MON_MODULE_COMMANDS = {
    "name": {
        "command": "BDNAME",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Read out module name (N1471)",
    },
    "number_of_channels": {
        "command": "BDNCH",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out number of Channels present",
    },
    "firmware_release": {
        "command": "BDFREL",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Read out Firmware Release (XX.X)",
    },
    "serial_number": {
        "command": "BDSNUM",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Read out value serial number (XXXXX)",
    },
    "interlock_status": {
        "command": "BDILK",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["YES", "NO"],
        "description": "Read out INTERLOCK status (YES/NO)",
    },
    "interlock_mode": {
        "command": "BDILKM",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["OPEN", "CLOSED"],
        "description": "Read out INTERLOCK mode (OPEN/CLOSED)",
    },
    "control_mode": {
        "command": "BDCTR",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["LOCAL", "REMOTE"],
        "description": "Read out Control Mode (LOCAL/REMOTE)",
    },
    "local_bus_termination_status": {
        "command": "BDTERM",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["ON", "OFF"],
        "description": "Read out LOCAL BUS Termination status (ON/OFF)",
    },
    "board_alarm_status": {
        "command": "BDALARM",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out Board Alarm status value (XXXXX)",
    },
}

# Dictionary mapping set module commands to their descriptions
_SET_MODULE_COMMANDS = {
    "interlock_mode": {
        "command": "BDILKM",
        "input_type": str,
        "allowed_input_values": ["OPEN", "CLOSED"],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set Interlock Mode",
    },
    "clear_alarm_signal": {
        "command": "BDCLR",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
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

    command = command.upper()
    valid_commands = [
        entry_value["command"]
        for entry_key, entry_value in _MON_MODULE_COMMANDS.items()
        if "command" in entry_value
    ]
    if command not in valid_commands:
        valid_commands_string = ", ".join(valid_commands)
        raise ValueError(
            f"Invalid command '{command}'. Valid commands are: {valid_commands_string}"
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

    return f"$BD:{bd:02d},CMD:SET,PAR:{command},VAL:{value}\r\n".encode("utf-8")
