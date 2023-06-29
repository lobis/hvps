from __future__ import annotations

_mon_channel_commands = {
    ":CONF:TRIP:ACTION": "Query the current action to be taken when a current trip occurs for the channel.",
    ":CONF:TRIP:TIME": "Query the current action to be taken when a current trip occurs for the channel.",
    ":CONF:INHP:ACTION": "Query the current action to be taken when a current trip occurs for the channel.",
    ":CONF:OUTPUT:MODE": "Query the configured channel output mode.",
    ":CONF:OUTPUT:MODE:LIST": "Query the available channel output modes as a list.",
    ":CONF:OUTPUT:POL": "Query the current output polarity of the channel.",
    ":CONF:OUTPUT:POL:LIST": "Query the available channel output polarities as a list.",
    ":READ:VOLT": "Query the voltage set Vset in Volt.",
    ":READ:VOLT:LIM": "Query the voltage limit Vlim in Volt.",
    ":READ:VOLT:NOM": "Query the channel voltage nominal Vnom in Volt.",
    ":READ:VOLT:ON": "Query the channel control bit 'Set On'.",
    ":READ:VOLT:EMCY": "Query the channel control bit 'Set Emergency Off'.",
    ":READ:CURR": "Query the current set (Iset) in Ampere.",
    ":READ:CURR:LIM": "Query the current limit (Ilim) in Ampere.",
    ":READ:CURR:NOM": "Query the current nominal (Inom) in Ampere.",
    ":READ:CURR:MODE": "Query the configured channel current mode in Ampere.",
    ":READ:CURR:MODE:LIST": "Query the available channel current modes as a list.",
    ":READ:CURR:BOUNDS": "Query the channel current bounds in Ampere.",
    ":READ:RAMP:CURR": "Query the channel current ramp speed in Ampere/second.",
    ":READ:RAMP:VOLT": "Query the channel voltage ramp speed in Volt/second.",
    ":READ:RAMP:VOLT:MIN": "Query the channel voltage ramp speed minimum in Volt/second.",
    ":READ:RAMP:VOLT:MAX": "Query the channel voltage ramp speed maximum in Volt/second.",
    ":READ:RAMP:CURR:MIN": "Query the channel current ramp speed minimum in Ampere/second.",
    ":READ:RAMP:CURR:MAX": "Query the channel current ramp speed maximum in Ampere/second.",
    ":READ:CHAN:CONTROL": "Query the Channel Control register.",
    ":READ:CHAN:STATUS": "Query the Channel Status register.",
    ":READ:CHAN:EVENT:MASK": "Query the Channel Event Mask register.",
    ":MEAS:VOLT": "Query the measured channel voltage in Volt.",
    ":MEAS:CURR": "Query the measured channel current in Ampere.",
    ":CONF:RAMP:VOLT:UP": "Query the channel voltage ramp up speed in Volt/second.",
    ":CONF:RAMP:VOLT:DOWN": "Query the channel voltage ramp down speed in Volt/second.",
    ":CONF:RAMP:CURR:UP": "Query the channel current ramp up speed in Ampere/second.",
    ":CONF:RAMP:CURR:DOWN": "Query the channel current ramp down speed in Ampere/second.",
}

_set_channel_commands = {
    ":CONF:TRIP:ACTION": "Set the action to be taken when a current trip occurs for the channel.",
    ":CONF:TRIP:TIME": "Set the trip timeout with one millisecond resolution.",
    ":CONF:INHP:ACTION": "Set the action to be taken when an External Inhibit event occurs for the channel.",
    ":CONF:OUTPUT:MODE": "Set the channel output mode.",
    ":CONF:OUTPUT:POL": "Set the output polarity of the channel.",
    ":VOLT": "Set the channel voltage set.",
    ":VOLT:BOUNDS": "Set the channel voltage bounds.",
    ":VOLT EMCY": "Clear the channel from state emergency off.",
    ":CURR": "Set the channel current set.",
    ":CURR:BOUNDS": "Set the channel current bounds in Ampere.",
    ":CONF:RAMP:VOLT": "Set the channel voltage ramp speed for up and down direction in Volt/second.",
    ":CONF:RAMP:VOLT:UP": "Set the channel voltage ramp up speed in Volt/second.",
    ":CONF:RAMP:VOLT:DOWN": "Set the channel voltage ramp down speed in Volt/second.",
    ":CONF:RAMP:CURR": "Set the channel current ramp speed for up and down direction in Ampere/second.",
    ":CONF:RAMP:CURR:UP": "Set the channel current ramp up speed in Ampere/second.",
    ":CONF:RAMP:CURR:DOWN": "Set the channel current ramp down speed in Ampere/second.",
    ":VOLT ON": "Switch on the high voltage with the configured ramp speed.",
    ":VOLT OFF": "Switch off the high voltage with the configured ramp speed.",
    ":VOLT EMCY OFF": "Shut down the channel high voltage (without ramp) or clear the channel from state emergency off.",
    ":VOLT EMCY CLR": "Clear the channel from state emergency off. The channel goes to state off.",
    ":EVENT CLEAR": "Clear the Channel Event Status register.",
    ":EVENT": "Clears single bits or bit combinations in the Channel Event Status register by writing a one to the corresponding bit position.",
    ":EVENT:MASK": "Clears single bits or bit combinations in the Channel Event Status register by writing a one to the corresponding bit position.",
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
