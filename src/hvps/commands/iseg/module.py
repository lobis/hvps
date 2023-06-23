def _get_mon_module_command(command: str) -> bytes:
    """
    Generates a query command string for monitoring a specific channel.

    Args:
        command (str): The base command without the query symbol.

    Returns:
        str: The query command string.

    Example:
        command = ":MEAS:CURR"
        query_command = _get_mon_channel_command(command, channel)
        print(query_command)
        :MEAS:CURR? (@3)
    """
    return f"{command.strip()}?\r\n".encode("ascii")


def _get_set_module_command(command: str, value: str | int | float | None) -> bytes:
    """
    Generates an order command as a bytes object to set a value for a specific channel.

    Args:
        command (str): The base command without the value and channel suffix.
        value (str | int | float | None): The value to be set. Can be a string, integer, float, or None.

    Returns:
        bytes: The order command as a bytes object.

    Example:
        command = ":VOLT"
        value = 200
        order_command = _get_set_channel_command(channel, command, value)
        print(order_command)
        :VOLT 200,(@4)\r\n'
    """
    if isinstance(value, float):
        value_string = "{:E}".format(value)
        return f"{command.strip()} {value_string};*OPC?\r\n".encode("ascii")
    else:
        return f"{command.strip()} {value};*OPC?\r\n".encode("ascii")
