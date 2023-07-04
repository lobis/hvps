from __future__ import annotations

from typing import List

_MON_CHANNEL_COMMANDS = {
    ":CONF:TRIP:ACTION": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [*range(5)],
        "description": "Query the current action to be taken when a current trip occurs for the channel.",
    },
    ":CONF:TRIP:TIME": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the current action to be taken when a current trip occurs for the channel.",
    },
    ":CONF:INHP:ACTION": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [*range(5)],
        "description": "Query the action that should happen when an External Inhibit for the channel occurs.",
    },
    ":CONF:OUTPUT:MODE": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [1, 2, 3],
        "description": "Query the configured channel output mode.",
    },
    ":CONF:OUTPUT:MODE:LIST": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": List[int],
        "possible_output_values": [[1, 2, 3]],
        "description": "Query the available channel output modes as a list.",
    },
    ":CONF:OUTPUT:POL": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["p", "n"],
        "description": "Query the current output polarity of the channel.",
    },
    ":CONF:OUTPUT:POL:LIST": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": List[str],
        "possible_output_values": [["p", "n"]],
        "description": "Query the available channel output polarities as a list.",
    },
    ":READ:VOLT": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the voltage set Vset in Volt.",
    },
    ":READ:VOLT:LIM": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the voltage limit Vlim in Volt.",
    },
    ":READ:VOLT:NOM": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the voltage nominal Vnom in Volt.",
    },
    ":READ:VOLT:MODE": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel voltage mode.",
    },
    ":READ:VOLT:MODE:LIST": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": List[float],
        "possible_output_values": [],
        "description": "Query the available channel voltage modes as a list.",
    },
    ":READ:VOLT:BOUNDS": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the voltage bounds in Volt.",
    },
    ":READ:VOLT:ON": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [0, 1],
        "description": "Query the voltage output state.",
    },
    ":READ:VOLT:EMCY": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [0, 1],
        "description": "Query the voltage emergency state.",
    },
    ":READ:CURR": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the current set Iset in Ampere.",
    },
    ":READ:CURR:LIM": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the current limit Ilim in Ampere.",
    },
    ":READ:CURR:NOM": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the current nominal Inom in Ampere.",
    },
    ":READ:CURR:MODE": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel current mode.",
    },
    ":READ:CURR:MODE:LIST": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": List[float],
        "possible_output_values": [],
        "description": "Query the available channel current modes as a list.",
    },
    ":READ:CURR:BOUNDS": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the current bounds in Ampere.",
    },
    ":READ:RAMP:VOLT": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel voltage ramp speed for up and down direction in Volt/second.",
    },
    ":READ:RAMP:VOLT:MIN": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the channel voltage ramp speed minimum in Volt/second.",
    },
    ":READ:RAMP:VOLT:MAX": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the channel voltage ramp speed maximum in Volt/second.",
    },
    ":READ:RAMP:VOLT:UP": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel voltage ramp up speed in Volt/second.",
    },
    ":READ:RAMP:VOLT:DOWN": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel voltage ramp down speed in Volt/second.",
    },
    ":READ:RAMP:CURR": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel current ramp speed for up and down direction in Ampere/second.",
    },
    ":READ:RAMP:CURR:MIN": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the channel current ramp speed minimum in Ampere/second.",
    },
    ":READ:RAMP:CURR:MAX": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the channel current ramp speed maximum in Ampere/second.",
    },
    ":READ:RAMP:CURR:UP": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel current ramp up speed in Ampere/second.",
    },
    ":READ:RAMP:CURR:DOWN": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel current ramp down speed in Ampere/second.",
    },
    ":READ:CHAN:CONTROL": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Channel Control register.",
    },
    ":READ:CHAN:STATUS": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Channel Status register.",
    },
    ":MEAS:VOLT": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the measured channel voltage in Volt.",
    },
    ":MEAS:CURR": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the measured channel current in Ampere.",
    },
}

_SET_CHANNEL_COMMANDS = {
    ":CONF:TRIP:ACTION": {
        "input_type": int,
        "allowed_input_values": [*range(5)],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the action to be taken when a current trip occurs for the channel.",
    },
    ":CONF:TRIP:TIME": {
        "input_type": int,
        "allowed_input_values": [*range(1, 4096)],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the trip timeout with one millisecond resolution.",
    },
    ":CONF:INHP:ACTION": {
        "input_type": int,
        "allowed_input_values": [*range(5)],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the action to be taken when an External Inhibit event occurs for the channel.",
    },
    ":CONF:OUTPUT:MODE": {
        "input_type": int,
        "allowed_input_values": [*range(1, 4)],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel output mode.",
    },
    ":CONF:OUTPUT:POL": {
        "input_type": str,
        "allowed_input_values": ["p", "n"],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the output polarity of the channel.",
    },
    ":VOLT": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel voltage set.",
    },
    ":VOLT:BOUNDS": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel voltage bounds.",
    },
    ":CURR": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel current set.",
    },
    ":CURR:BOUNDS": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel current bounds.",
    },
    ":CONF:RAMP:VOLT": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel voltage ramp speed for up and down direction in Volt/second.",
    },
    ":CONF:RAMP:VOLT:UP": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel voltage ramp up speed in Volt/second.",
    },
    ":CONF:RAMP:VOLT:DOWN": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel voltage ramp down speed in Volt/second.",
    },
    ":CONF:RAMP:CURR": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel current ramp speed for up and down direction in Ampere/second.",
    },
    ":CONF:RAMP:CURR:UP": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel current ramp up speed in Ampere/second.",
    },
    ":CONF:RAMP:CURR:DOWN": {
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel current ramp down speed in Ampere/second.",
    },
    ":VOLT ON": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Switch on the high voltage with the configured ramp speed.",
    },
    ":VOLT OFF": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Switch off the high voltage with the configured ramp speed.",
    },
    ":VOLT EMCY OFF": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Switch off the high voltage immediately.",
    },
    ":CURR ON": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Switch on the high current with the configured ramp speed.",
    },
    ":CURR OFF": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Switch off the high current with the configured ramp speed.",
    },
    ":CURR EMCY OFF": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Switch off the high current immediately.",
    },
    ":VOLT EMCY CLR": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Clear the voltage emergency state.",
    },
    ":CURR EMCY CLR": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Clear the current emergency state.",
    },
    ":EVENT CLEAR": {
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Clear the Channel Event Status register.",
    },
    ":EVENT": {
        "input_type": int,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Clears single bits or bit combinations in the Channel Event Status register by writing a one to the corresponding bit position.",
    },
    ":EVENT:MASK": {
        "input_type": int,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the Channel Event Mask register",
    },
}


def _get_mon_channel_command(channel: int, command: str) -> bytes:
    """
    Generates a query command string for monitoring a specific channel.

    Args:
        channel (int): The channel number.
        command (str): The base command without the query symbol.

    Returns:
        bytes: The query command string as bytes.

    Raises:
        ValueError: If the provided channel is not a valid positive integer.
        ValueError: If the provided command is not a valid command.

    Example:
        command = ":MEAS:CURR"
        channel = 3
        query_command = _get_mon_channel_command(channel, command)
        print(query_command)
        b':MEAS:CURR? (@3)\r\n'
    """
    if channel < 0:
        raise ValueError(
            f"Invalid channel '{channel}'. Valid channels are positive integers."
        )
    command = command.upper()
    if command not in _mon_channel_commands:
        valid_commands = ", ".join(_mon_channel_commands.keys())
        raise ValueError(
            f"Invalid command '{command}'. Valid commands are: {valid_commands}."
        )

    return f"{command.strip()}? (@{channel})\r\n".encode("ascii")


def _get_set_channel_command(
    channel: int, command: str, value: str | int | float | None
) -> bytes:
    """
    Generates an order command as a bytes object to set a value for a specific channel.

    Args:
        channel (int): The channel number.
        command (str): The base command without the value and channel suffix.
        value (str | int | float | None): The value to be set. Can be a string, integer, float, or None.

    Returns:
        bytes: The order command as a bytes object.

    Raises:
        ValueError: If the provided channel is not a valid positive integer.
        ValueError: If the provided command is not a valid command.

    Example:
        channel = 4
        command = ":VOLT"
        value = 200
        order_command = _get_set_channel_command(channel, command, value)
        print(order_command)
        b':VOLT 200,(@4);*OPC?\r\n'
    """
    if channel < 0:
        raise ValueError(
            f"Invalid channel '{channel}'. Valid channels are positive integers."
        )
    command = command.upper()
    if command not in _set_channel_commands:
        valid_commands = ", ".join(_mon_channel_commands.keys())
        raise ValueError(
            f"Invalid command '{command}'. Valid commands are: {valid_commands}."
        )

    if isinstance(value, float):
        value = f"{value:E}"

    return f"{command.strip()} {value},(@{channel});*OPC?\r\n".encode("ascii")
