from __future__ import annotations

from ...utils import check_command_input

# Dictionary mapping monitor channel commands to their descriptions
_MON_CHANNEL_COMMANDS = {
    "VSET": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out VSET value (XXXX.X V)",
    },
    "VMIN": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out VSET minimum value (0 V)",
    },
    "VMAX": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out VSET maximum value (8000.0 V)",
    },
    "VDEC": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out VSET number of decimal digits",
    },
    "VMON": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out VMON value (XXXX.X V)",
    },
    "ISET": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out ISET value (XXXX.XX µA)",
    },
    "IMIN": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out ISET minimum value (0 µA)",
    },
    "IMAX": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out ISET maximum value (3000.00 µA)",
    },
    "ISDEC": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out ISET number of decimal digits",
    },
    "IMON": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out IMON value (XXXX.XX µA)",
    },
    "IMRANGE": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["HIGH", "LOW"],
        "description": "Read out IMON RANGE value (HIGH / LOW)",
    },
    "IMDEC": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out IMON number of decimal digits (2 HR, 3 LR)",
    },
    "MAXV": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out MAXVSET value (XXXX V)",
    },
    "MVMIN": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out MAXVSET minimum value (0 V)",
    },
    "MVMAX": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out MAXVSET maximum value (8100 V)",
    },
    "MVDEC": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out MAXVSET number of decimal digits",
    },
    "RUP": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP UP value (XXX V/S)",
    },
    "RUPMIN": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP UP minimum value (0 V/S)",
    },
    "RUPMAX": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP UP maximum value (1000 V/S)",
    },
    "RUPDEC": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out RAMP UP number of decimal digits",
    },
    "RDW": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP DOWN value (XXX V/S)",
    },
    "RDWMIN": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP DOWN minimum value ( V/S )",
    },
    "RDWMAX": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP DOWN maximum value",
    },
    "RDWDEC": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP DOWN number of decimal digits",
    },
    "TRIP": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out TRIP value (XXXXX)",
    },
    "TRIPMIN": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "TRIP minimum value (S)",
    },
    "TRIPMAX": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out TRIP time minimum value ( S )",
    },
    "TRIPDEC": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out TRIP time number of decimal digits",
    },
    "PDWN": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["RAMP", "KILL"],
        "description": "Read out POWER DOWN value (RAMP / KILL)",
    },
    "POL": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["+", "-"],
        "description": "Read out POLARITY value (+ / -)",
    },
    "STAT": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out Channel status value (XXXXX)",
    },
}

# Dictionary mapping set channel commands to their descriptions
_SET_CHANNEL_COMMANDS = {
    "VSET": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set VSET value (XXXX.X V)",
    },
    "ISET": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set ISET value (XXXX.XX µA)",
    },
    "MAXV": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set MAXVSET value (XXXX V)",
    },
    "RUP": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set RAMP UP value (XXX V/S)",
    },
    "RDW": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set RAMP DOWN value (XXX V/S)",
    },
    "TRIP": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set TRIP time value (XXXX.X s)",
    },
    "PDWN": {
        "input_type": str,
        "allowed_input_values": ["RAMP", "KILL"],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set POWER DOWN mode value (RAMP / KILL)",
    },
    "IMRANGE": {
        "input_type": str,
        "allowed_input_values": ["HIGH", "LOW"],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set IMON RANGE value (HIGH / LOW)",
    },
    "ON": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set Ch ON",
    },
    "OFF": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set Ch OFF",
    },
}


def validate_channel_number(channel: int) -> None:
    if not 0 <= channel <= 7:
        raise ValueError(
            f"Invalid channel number '{channel}'. Must be in the range 0..7."
        )


def validate_board_number(board: int) -> None:
    if not 0 <= board <= 31:
        raise ValueError(f"Invalid board number '{board}'. Must be in the range 0..31.")


def validate_channel_command(command: str, valid_commands: dict) -> None:
    if command.upper() not in valid_commands:
        valid_commands = ", ".join(valid_commands.keys())
        raise ValueError(
            f"Invalid command '{command}'. Valid command are: {valid_commands}"
        )


def _get_mon_channel_command(bd: int, channel: int, command: str) -> bytes:
    """
    Generate a command string to monitor a specific channel command.

    Args:
        bd (int): The board number.
        channel (int): The channel number.
        command (str): The command to monitor.


    Returns:
        bytes: The command string encoded as bytes.

    Raises:
        ValueError: If the provided command is not valid.
    """

    validate_board_number(bd)
    validate_channel_number(channel)

    command = command.upper()

    check_command_input(_MON_CHANNEL_COMMANDS, command)

    return f"$BD:{bd:02d},CMD:MON,CH:{channel:01d},PAR:{command}\r\n".encode("utf-8")


def _get_set_channel_command(
    bd: int, channel: int, command: str, value: str | int | float | None
) -> bytes:
    """
    Generate a command string to set a specific channel command to a given value.

    Args:
        bd (int): The board number.
        channel (int): The channel number.
        command (str): The command to set.
        value (str | int | float | None): The value to set the command to.

    Returns:
        bytes: The command string encoded as bytes.

    Raises:
        ValueError: If the provided command or value is not valid.
    """

    validate_board_number(bd)
    validate_channel_number(channel)

    command = command.upper()

    check_command_input(_SET_CHANNEL_COMMANDS, command, value)

    if value is None:
        return f"$BD:{bd:02d},CMD:SET,CH:{channel:01d},PAR:{command}\r\n".encode(
            "utf-8"
        )

    return (
        f"$BD:{bd:02d},CMD:SET,CH:{channel:01d},PAR:{command},VAL:{value}\r\n".encode(
            "utf-8"
        )
    )
