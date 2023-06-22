from __future__ import annotations


def _get_mon_channel_command(channel: int, command: str) -> bytes:
    """
    Generates a query command string for monitoring a specific channel.

    Args:
        command (str): The base command without the query symbol.
        channel (int): The channel number.

    Returns:
        str: The query command string.

    Example:
        command = ":MEAS:CURR"
        channel = 3
        query_command = _get_mon_channel_command(command, channel)
        print(query_command)
        :MEAS:CURR? (@3)
    """
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

    Example:
        channel = 4
        command = ":VOLT"
        value = 200
        order_command = _get_set_channel_command(channel, command, value)
        print(order_command)
        :VOLT 200,(@4)\r\n'
    """
    return f"{command.strip()} {value},(@{channel});*OPC?\r\n".encode("ascii")
