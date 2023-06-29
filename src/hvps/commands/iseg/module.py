from __future__ import annotations

_mon_module_commands = {
    ":READ:MODULE:CHANNELNUMBER": "The number of channels in the module.",
    ":READ:FIRMWARE:RELEASE": "Read out Firmware Release (XX.X)",
    ":READ:MODULE:STATUS": "Read out module status register",
    ":CONF:AVER": "Query the digital filter averaging steps.",
    ":CONF:KILL": "Get the current value for the kill enable function.",
    ":CONF:ADJUST": "Get the fine adjustment state.",
    ":CONF:CAN:ADDR": "Query the module's CAN bus address.",
    ":CONF:CAN:BITRATE": "Query the module's CAN bus bit rate.",
    ":CONF:SERIAL:BAUD": "Query the device's serial baud rate.",
    ":CONF:SERIAL:ECHO": "Check if serial echo is enabled or disabled.",
    ":READ:VOLT:LIM": "Query the module's voltage limit in percent.",
    ":READ:CURR:LIM": "Query the module's current limit in percent.",
    ":READ:RAMP:VOLT": "Query the module's voltage ramp speed in percent/second.",
    ":READ:RAMP:CURR": "Query the module's current ramp speed in percent/second.",
    ":READ:MODULE:CONTROL": "Query the Module Control register",
    ":READ:MODULE:EVENT:STATUS": "Query the Module Event Status register",
    ":READ:MODULE:EVENT:MASK": "Query the Module Event Mask register",
    ":READ:MODULE:EVENT:CHANSTAT": "Query the Module Event Channel Status register",
    ":READ:MODULE:EVENT:CHANMASK": "Query the Module Event Channel Mask register",
    ":READ:MODULE:SUPPLY? (@0-6)": "Query the module supply voltages",
    ":READ:MODULE:SUPPLY:P24V": "Query the module supply voltage +24 Volt",
    ":READ:MODULE:SUPPLY:N24V": "Query the module supply voltage -24 Volt",
    ":READ:MODULE:SUPPLY:P5V": "Query the module supply voltage +5 Volt",
    ":READ:MODULE:SUPPLY:P3V": "Query the module internal supply voltage +3.3 Volt",
    ":READ:MODULE:SUPPLY:P12V": "Query the module internal supply voltage +12 Volt",
    ":READ:MODULE:SUPPLY:N12V": "Query the module internal supply voltage -12 Volt",
    ":READ:MODULE:TEMPERATURE": "Query the module temperature in degree Celsius",
    ":READ:MODULE:SETVALUE": "Query the setvalue changes counter",
    ":READ:FIRMWARE:NAME": "Query the module's firmware name",
    ":CONF:EVENT:MASK": "Query the Module Event Mask register",
    ":CONF:EVENT:CHANMASK": "Query the Module Event Channel Mask register",
}

_set_module_commands = {
    ":CONF:AVER": "Query the digital filter averaging steps.",
    ":CONF:KILL": "Get the current value for the kill enable function.",
    ":CONF:ADJUST": "Get the fine adjustment state.",
    ":CONF:CAN:ADDR": "Query the module's CAN bus address.",
    ":CONF:CAN:BITRATE": "Query the module's CAN bus bit rate.",
    ":CONF:SERIAL:BAUD": "Query the device's serial baud rate.",
    ":CONF:SERIAL:ECHO": "Check if serial echo is enabled or disabled.",
    ":CONF:EVENT:MASK": "Set the Module Event Mask register",
    ":CONF:EVENT:CHANMASK": "Set the Module Event Channel Mask register",
    ":SYSTEM:USER:CONFIG": "Set the device to configuration mode to change the CAN bitrate or address",
    ":CONF:EVENT CLEAR": "Reset the Module Event Status register",
    ":CONF:EVENT": "Clear single bits or bit combinations in the Module Event Status register",
}


def _get_mon_module_command(command: str) -> bytes:
    """
    Generates a query command string for monitoring a specific module.

    Args:
        command (str): The base command without the query symbol.

    Returns:
        bytes: The query command string as bytes.

    Raises:
        ValueError: If the provided command is not a valid command.

    Example:
        command = ":MEAS:CURR"
        query_command = _get_mon_module_command(command)
        print(query_command)
        b':MEAS:CURR?\r\n'
    """
    command = command.upper()
    if command not in _mon_module_commands:
        valid_commands = ", ".join(_mon_module_commands.keys())
        raise ValueError(
            f"Invalid command '{command}'. Valid commands are: {valid_commands}."
        )

    return f"{command.strip()}?\r\n".encode("ascii")


def _get_set_module_command(command: str, value: str | int | float | None) -> bytes:
    """
    Generates an order command as a bytes object to set a value for a specific module.

    Args:
        command (str): The base command without the value and channel suffix.
        value (str | int | float | None): The value to be set. Can be a string, integer, float, or None.

    Returns:
        bytes: The order command as a bytes object.

    Raises:
        ValueError: If the provided command is not a valid command.

    Example:
        command = ":VOLT"
        value = 200
        order_command = _get_set_module_command(command, value)
        print(order_command)
        b':VOLT 200;*OPC?\r\n'
    """
    command = command.upper()
    if command not in _set_module_commands:
        valid_commands = ", ".join(_set_module_commands.keys())
        raise ValueError(
            f"Invalid command '{command}'. Valid commands are: {valid_commands}."
        )
    if isinstance(value, float):
        value = f"{value:E}"

    return f"{command.strip()} {value};*OPC?\r\n".encode("ascii")
