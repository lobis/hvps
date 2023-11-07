from __future__ import annotations

from typing import List


_MON_CHANNEL_COMMANDS = {
    "trip_action": {
        "command": ":CONF:TRIP:ACTION",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [*range(5)],
        "description": "Query the current action to be taken when a current trip occurs for the channel.",
    },
    "trip_timeout": {
        "command": ":CONF:TRIP:TIME",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the current action to be taken when a current trip occurs for the channel.",
    },
    "external_inhibit_action": {
        "command": ":CONF:INHP:ACTION",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [*range(5)],
        "description": "Query the action that should happen when an External Inhibit for the channel occurs.",
    },
    "output_mode": {
        "command": ":CONF:OUTPUT:MODE",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [1, 2, 3],
        "description": "Query the configured channel output mode.",
    },
    "available_output_modes": {
        "command": ":CONF:OUTPUT:MODE:LIST",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": List[int],
        "possible_output_values": [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]],
        "description": "Query the available channel output modes as a list.",
    },
    "output_polarity": {
        "command": ":CONF:OUTPUT:POL",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": ["p", "n"],
        "description": "Query the current output polarity of the channel.",
    },
    "available_output_polarities": {
        "command": ":CONF:OUTPUT:POL:LIST",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": List[str],
        "possible_output_values": [["p", "n"]],
        "description": "Query the available channel output polarities as a list.",
    },
    "voltage_set": {
        "command": ":READ:VOLT",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the voltage set Vset in Volt.",
    },
    "voltage_limit": {
        "command": ":READ:VOLT:LIM",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the voltage limit Vlim in Volt.",
    },
    "voltage_nominal": {
        "command": ":READ:VOLT:NOM",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the voltage nominal Vnom in Volt.",
    },
    "voltage_mode": {
        "command": ":READ:VOLT:MODE",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel voltage mode.",
    },
    "voltage_mode_list": {
        "command": ":READ:VOLT:MODE:LIST",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": List[float],
        "possible_output_values": [],
        "description": "Query the available channel voltage modes as a list.",
    },
    "voltage_bounds": {
        "command": ":READ:VOLT:BOUNDS",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the voltage bounds in Volt.",
    },
    "set_on": {
        "command": ":READ:VOLT:ON",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [0, 1],
        "description": "Query the channel control bit Set On",
    },
    "emergency_off": {
        "command": ":READ:VOLT:EMCY",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [0, 1],
        "description": "Query the channel control bit Set Emergency Off",
    },
    "current_set": {
        "command": ":READ:CURR",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the current set Iset in Ampere.",
    },
    "current_limit": {
        "command": ":READ:CURR:LIM",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the current limit Ilim in Ampere.",
    },
    "current_nominal": {
        "command": ":READ:CURR:NOM",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the current nominal Inom in Ampere.",
    },
    "current_mode": {
        "command": ":READ:CURR:MODE",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel current mode.",
    },
    "current_mode_list": {
        "command": ":READ:CURR:MODE:LIST",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": List[float],
        "possible_output_values": [],
        "description": "Query the available channel current modes as a list.",
    },
    "current_bounds": {
        "command": ":READ:CURR:BOUNDS",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the current bounds in Ampere.",
    },
    "current_ramp_speed": {
        "command": ":READ:RAMP:CURR",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel current ramp speed for up and down direction in Ampere/second.",
    },
    "voltage_ramp_speed": {
        "command": ":READ:RAMP:VOLT",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the configured channel voltage ramp speed for up and down direction in Volt/second.",
    },
    "voltage_ramp_speed_minimum": {
        "command": ":READ:RAMP:VOLT:MIN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the channel voltage ramp speed minimum in Volt/second.",
    },
    "voltage_ramp_speed_maximum": {
        "command": ":READ:RAMP:VOLT:MAX",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the channel voltage ramp speed maximum in Volt/second.",
    },
    "current_ramp_speed_minimum": {
        "command": ":READ:RAMP:CURR:MIN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the channel current ramp speed minimum in Ampere/second.",
    },
    "current_ramp_speed_maximum": {
        "command": ":READ:RAMP:CURR:MAX",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the channel current ramp speed maximum in Ampere/second.",
    },
    "channel_control": {
        "command": ":READ:CHAN:CONTROL",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Channel Control register.",
    },
    "channel_status": {
        "command": ":READ:CHAN:STATUS",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Channel Status register.",
    },
    "channel_event_mask": {
        "command": "READ:CHAN:EVENT:MASK",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Channel Event Mask register.",
    },
    "measured_voltage": {
        "command": ":MEAS:VOLT",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the measured channel voltage in Volt.",
    },
    "measured_current": {
        "command": ":MEAS:CURR",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the measured channel current in Ampere.",
    },
    "channel_voltage_ramp_up_speed": {
        "command": ":CONF:RAMP:VOLT:UP",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Set the channel voltage ramp up speed in Volt/second.",
    },
    "channel_voltage_ramp_down_speed": {
        "command": ":CONF:RAMP:VOLT:DOWN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Set the channel voltage ramp down speed in Volt/second.",
    },
    "channel_current_ramp_up_speed": {
        "command": ":CONF:RAMP:CURR:UP",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Set the channel current ramp up speed in Ampere/second.",
    },
    "channel_current_ramp_down_speed": {
        "command": ":CONF:RAMP:CURR:DOWN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Set the channel current ramp down speed in Ampere/second.",
    },
}

_SET_CHANNEL_COMMANDS = {
    "trip_action": {
        "command": ":CONF:TRIP:ACTION",
        "input_type": int,
        "allowed_input_values": [*range(5)],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the action to be taken when a current trip occurs for the channel.",
    },
    "trip_timeout": {
        "command": ":CONF:TRIP:TIME",
        "input_type": int,
        "allowed_input_values": [*range(0, 4096)],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the trip timeout with one millisecond resolution.",
    },
    "external_inhibit_action": {
        "command": ":CONF:INHP:ACTION",
        "input_type": int,
        "allowed_input_values": [*range(5)],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the action to be taken when an External Inhibit event occurs for the channel.",
    },
    "output_mode": {
        "command": ":CONF:OUTPUT:MODE",
        "input_type": int,
        "allowed_input_values": [*range(1, 4)],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel output mode.",
    },
    "output_polarity": {
        "command": ":CONF:OUTPUT:POL",
        "input_type": str,
        "allowed_input_values": ["p", "n"],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the output polarity of the channel.",
    },
    "voltage_set": {
        "command": ":VOLT",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel voltage set.",
    },
    "voltage_bounds": {
        "command": ":VOLT:BOUNDS",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel voltage bounds.",
    },
    "current_set": {
        "command": ":CURR",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel current set.",
    },
    "current_bounds": {
        "command": ":CURR:BOUNDS",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel current bounds.",
    },
    "set_channel_voltage_ramp_up_down_speed": {
        "command": ":CONF:RAMP:VOLT",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel voltage ramp speed for up and down direction in Volt/second.",
    },
    "channel_voltage_ramp_up_speed": {
        "command": ":CONF:RAMP:VOLT:UP",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel voltage ramp up speed in Volt/second.",
    },
    "channel_voltage_ramp_down_speed": {
        "command": ":CONF:RAMP:VOLT:DOWN",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel voltage ramp down speed in Volt/second.",
    },
    "set_channel_current_ramp_up_down_speed": {
        "command": ":CONF:RAMP:CURR",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel current ramp speed for up and down direction in Ampere/second.",
    },
    "channel_current_ramp_up_speed": {
        "command": ":CONF:RAMP:CURR:UP",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel current ramp up speed in Ampere/second.",
    },
    "channel_current_ramp_down_speed": {
        "command": ":CONF:RAMP:CURR:DOWN",
        "input_type": float,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the channel current ramp down speed in Ampere/second.",
    },
    "switch_on_high_voltage": {
        "command": ":VOLT ON",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Switch on the high voltage with the configured ramp speed.",
    },
    "switch_off_high_voltage": {
        "command": ":VOLT OFF",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Switch off the high voltage with the configured ramp speed.",
    },
    "shutdown_channel_high_voltage": {
        "command": ":VOLT EMCY OFF",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Switch off the high voltage immediately.",
    },
    "clear_channel_emergency_off": {
        "command": ":VOLT EMCY CLR",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Clear the voltage emergency state.",
    },
    "clear_event_status": {
        "command": ":EVENT CLEAR",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Clear the Channel Event Status register.",
    },
    "clear_event_bits": {
        "command": ":EVENT",
        "input_type": int,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Clears single bits or bit combinations in the Channel Event Status register by writing a one to the corresponding bit position.",
    },
    "set_event_mask": {
        "command": ":EVENT:MASK",
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

    if isinstance(value, float):
        value = f"{value:.3E}"

    return f"{command.strip()} {value},(@{channel});*OPC?\r\n".encode("ascii")
