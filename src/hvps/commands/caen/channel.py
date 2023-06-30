from __future__ import annotations

# Dictionary mapping monitor channel commands to their descriptions
_mon_channel_commands = {
    "VSET": "Read out VSET value (XXXX.X V)",
    "VMIN": "Read out VSET minimum value (0 V)",
    "VMAX": "Read out VSET maximum value (8000.0 V)",
    "VDEC": "Read out VSET number of decimal digits",
    "VMON": "Read out VMON value (XXXX.X V)",
    "ISET": "Read out ISET value (XXXX.XX µA)",
    "IMIN": "Read out ISET minimum value (0 µA)",
    "IMAX": "Read out ISET maximum value (3000.00 µA)",
    "ISDEC": "Read out ISET number of decimal digits",
    "IMON": "Read out IMON value (XXXX.XX µA)",
    "IMRANGE": "Read out IMON RANGE value (HIGH / LOW)",
    "IMDEC": "Read out IMON number of decimal digits (2 HR, 3 LR)",
    "MAXV": "Read out MAXVSET value (XXXX V)",
    "MVMIN": "Read out MAXVSET minimum value (0 V)",
    "MVMAX": "Read out MAXVSET maximum value (8100 V)",
    "MVDEC": "Read out MAXVSET number of decimal digits",
    "RUP": "Read out RAMP UP value (XXX V/S)",
    "RUPMIN": "Read out RAMP UP minimum value (1 V/S)",
    "RUPMAX": "Read out RAMP UP maximum value (500 V/S)",
    "RUPDEC": "Read out RAMP UP number of decimal digits",
    "RDW": "Read out RAMP DOWN value (XXX V/S)",
    "RDWMIN": "Read out RAMP DOWN minimum value (1 V/S)",
    "RDWMAX": "Read out RAMP DOWN maximum value (500 V/S)",
    "RDWDEC": "Read out RAMP DOWN number of decimal digits",
    "TRIP": "Read out TRIP time value (XXXX.X S)",
    "TRIPMIN": "Read out TRIP time minimum value (0 S)",
    "TRIPMAX": "Read out TRIP time maximum value (1000.0 S)",
    "TRIPDEC": "Read out TRIP time number of decimal digits",
    "PDWN": "Read out POWER DOWN value (RAMP / KILL)",
    "POL": "Read out POLARITY value ('+' / '-')",
    "STAT": "Read out Channel status value (XXXXX)",
}

# Dictionary mapping set channel commands to their descriptions
_set_channel_commands = {
    "VSET": "VAL:XXXX.X Set VSET value",
    "ISET": "VAL:XXXX.XX Set ISET value",
    "MAXV": "VAL:XXXX Set MAXVSET value",
    "RUP": "VAL:XXX Set RAMP UP value",
    "RDW": "VAL:XXX Set RAMP DOWN value",
    "TRIP": "VAL:XXXX.X Set TRIP time value",
    "PDWN": "VAL:RAMP/KILL Set POWER DOWN mode value",
    "IMRANGE": "VAL:HIGH/LOW Set IMON RANGE value",
    "ON": "Set Ch ON",
    "OFF": "Set Ch OFF",
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

    validate_channel_command(command, _mon_channel_commands)

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

    validate_channel_command(command, _set_channel_commands)

    if command in ["ON", "OFF"]:
        if value is not None:
            raise ValueError(f"command '{command}' does not accept a value")
        return f"$BD:{bd:02d},CMD:SET,CH:{channel:01d},PAR:{command}\r\n".encode(
            "utf-8"
        )
    elif command == "IMRANGE":
        if value not in ["HIGH", "LOW"]:
            raise ValueError(f"command '{command}' only accepts 'HIGH' or 'LOW'")
    elif command == "PDWN":
        if value not in ["RAMP", "KILL"]:
            raise ValueError(f"command '{command}' only accepts 'RAMP' or 'KILL'")

    return (
        f"$BD:{bd:02d},CMD:SET,CH:{channel:01d},PAR:{command},VAL:{value}\r\n".encode(
            "utf-8"
        )
    )
