from __future__ import annotations


# Dictionary mapping monitor channel commands to their descriptions
_MON_CHANNEL_COMMANDS = {
    "vset": {
        "command": "VSET",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out VSET value (XXXX.X V)",
    },
    "vmin": {
        "command": "VMIN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out VSET minimum value (0 V)",
    },
    "vmax": {
        "command": "VMAX",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out VSET maximum value (8000.0 V)",
    },
    "vdec": {
        "command": "VDEC",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out VSET number of decimal digits",
    },
    "vmon": {
        "command": "VMON",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out VMON value (XXXX.X V)",
    },
    "iset": {
        "command": "ISET",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out ISET value (XXXX.XX µA)",
    },
    "imin": {
        "command": "IMIN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out ISET minimum value (0 µA)",
    },
    "imax": {
        "command": "IMAX",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out ISET maximum value (3000.00 µA)",
    },
    "isdec": {
        "command": "ISDEC",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out ISET number of decimal digits",
    },
    "imon": {
        "command": "IMON",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out IMON value (XXXX.XX µA)",
    },
    "imrange": {
        "command": "IMRANGE",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["HIGH", "LOW"],
        "description": "Read out IMON RANGE value (HIGH / LOW)",
    },
    "imrange_high": {
        "command": "",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": bool,
        "possible_output_values": [],
        "description": "Check out if IMON RANGE value is HIGH)",
    },
    "imrange_low": {
        "command": "",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": bool,
        "possible_output_values": [],
        "description": "Check out if IMON RANGE value is HIGH)",
    },
    "imdec": {
        "command": "IMDEC",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out IMON number of decimal digits (2 HR, 3 LR)",
    },
    "maxv": {
        "command": "MAXV",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out MAXVSET value (XXXX V)",
    },
    "mvmin": {
        "command": "MVMIN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out MAXVSET minimum value (0 V)",
    },
    "mvmax": {
        "command": "MVMAX",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out MAXVSET maximum value (8100 V)",
    },
    "mvdec": {
        "command": "MVDEC",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out MAXVSET number of decimal digits",
    },
    "rup": {
        "command": "RUP",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP UP value (XXX V/S)",
    },
    "rupmin": {
        "command": "RUPMIN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP UP minimum value (0 V/S)",
    },
    "rupmax": {
        "command": "RUPMAX",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP UP maximum value (1000 V/S)",
    },
    "rupdec": {
        "command": "RUPDEC",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out RAMP UP number of decimal digits",
    },
    "rdw": {
        "command": "RDW",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP DOWN value (XXX V/S)",
    },
    "rdwmin": {
        "command": "RDWMIN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP DOWN minimum value ( V/S )",
    },
    "rdwmax": {
        "command": "RDWMAX",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP DOWN maximum value",
    },
    "rdwdec": {
        "command": "RDWDEC",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out RAMP DOWN number of decimal digits",
    },
    "trip": {
        "command": "TRIP",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out TRIP value (XXXXX)",
    },
    "tripmin": {
        "command": "TRIPMIN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "TRIP minimum value (S)",
    },
    "tripmax": {
        "command": "TRIPMAX",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Read out TRIP time minimum value ( S )",
    },
    "tripdec": {
        "command": "TRIPDEC",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out TRIP time number of decimal digits",
    },
    "pdwn": {
        "command": "PDWN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["RAMP", "KILL"],
        "description": "Read out POWER DOWN value (RAMP / KILL)",
    },
    "pol": {
        "command": "POL",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["+", "-"],
        "description": "Read out POLARITY value (+ / -)",
    },
    "polarity_positive": {
        "command": "",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": bool,
        "possible_output_values": [],
        "description": "Check out POLARITY value is +",
    },
    "polarity_negative": {
        "command": "",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": bool,
        "possible_output_values": [],
        "description": "Check out POLARITY value is -",
    },
    "stat": {
        "command": "STAT",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out Channel status value (XXXXX)",
    },
}

# Dictionary mapping set channel commands to their descriptions
_SET_CHANNEL_COMMANDS = {
    "vset": {
        "command": "VSET",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set VSET value (XXXX.X V)",
    },
    "iset": {
        "command": "ISET",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set ISET value (XXXX.XX µA)",
    },
    "maxv": {
        "command": "MAXV",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set MAXVSET value (XXXX V)",
    },
    "rup": {
        "command": "RUP",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set RAMP UP value (XXX V/S)",
    },
    "rdw": {
        "command": "RDW",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set RAMP DOWN value (XXX V/S)",
    },
    "trip": {
        "command": "TRIP",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set TRIP time value (XXXX.X s)",
    },
    "pdwn": {
        "command": "PDWN",
        "input_type": str,
        "allowed_input_values": ["RAMP", "KILL"],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set POWER DOWN mode value (RAMP / KILL)",
    },
    "imrange": {
        "command": "IMRANGE",
        "input_type": str,
        "allowed_input_values": ["HIGH", "LOW"],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set IMON RANGE value (HIGH / LOW)",
    },
    "turn_on": {
        "command": "ON",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set Ch ON",
    },
    "turn_off": {
        "command": "OFF",
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

    if value is None:
        return f"$BD:{bd:02d},CMD:SET,CH:{channel:01d},PAR:{command}\r\n".encode(
            "utf-8"
        )

    return (
        f"$BD:{bd:02d},CMD:SET,CH:{channel:01d},PAR:{command},VAL:{value}\r\n".encode(
            "utf-8"
        )
    )
