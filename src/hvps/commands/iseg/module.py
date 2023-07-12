from __future__ import annotations

from types import NoneType

from ...utils import check_command_input


# TODO: change values for dictionary with possible values and description
_MON_MODULE_COMMANDS = {
    ":READ:MODULE:CHANNELNUMBER": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "The number of channels in the module.",
    },
    ":READ:FIRMWARE:RELEASE": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Read out Firmware Release (XX.X)",
    },
    ":READ:MODULE:STATUS": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Read out module status register",
    },
    ":CONF:AVER": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Query the digital filter averaging steps.",
    },
    ":CONF:KILL": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Get the current value for the kill enable function.",
    },
    ":CONF:ADJUST": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Get the fine adjustment state.",
    },
    ":CONF:CAN:ADDR": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Query the module's CAN bus address.",
    },
    ":CONF:CAN:BITRATE": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Query the module's CAN bus bit rate.",
    },
    ":CONF:SERIAL:BAUD": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Query the device's serial baud rate.",
    },
    ":CONF:SERIAL:ECHO": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Check if serial echo is enabled or disabled.",
    },
    ":READ:VOLT:LIM": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module's voltage limit in percent.",
    },
    ":READ:CURR:LIM": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module's current limit in percent.",
    },
    ":READ:RAMP:VOLT": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module's voltage ramp speed in percent/second.",
    },
    ":READ:RAMP:CURR": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module's current ramp speed in percent/second.",
    },
    ":READ:MODULE:CONTROL": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Control register",
    },
    ":READ:MODULE:EVENT:STATUS": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Event Status register",
    },
    ":READ:MODULE:EVENT:MASK": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Event Mask register",
    },
    ":READ:MODULE:EVENT:CHANSTAT": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Event Channel Status register",
    },
    ":READ:MODULE:EVENT:CHANMASK": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Event Channel Mask register",
    },
    ":READ:MODULE:SUPPLY? (@0-6)": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Query the module supply voltages",
    },
    ":READ:MODULE:SUPPLY:P24V": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module supply voltage +24 Volt",
    },
    ":READ:MODULE:SUPPLY:N24V": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module supply voltage -24 Volt",
    },
    ":READ:MODULE:SUPPLY:P5V": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module supply voltage +5 Volt",
    },
    ":READ:MODULE:SUPPLY:P3V": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module internal supply voltage +3.3 Volt",
    },
    ":READ:MODULE:SUPPLY:P12V": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module internal supply voltage +12 Volt",
    },
    ":READ:MODULE:SUPPLY:N12V": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module internal supply voltage -12 Volt",
    },
    ":READ:MODULE:TEMPERATURE": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module temperature in degree Celsius",
    },
    ":READ:MODULE:SETVALUE": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the setvalue changes counter",
    },
    ":READ:FIRMWARE:NAME": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Query the module's firmware name",
    },
    ":CONF:EVENT:MASK": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Event Mask register",
    },
    ":CONF:EVENT:CHANMASK": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Event Channel Mask register",
    },
}

_SET_MODULE_COMMANDS = {
    ":CONF:AVER": {
        "input_type": int,
        "allowed_input_values": [1, 16, 64, 256, 512, 1024],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Set the number of digital filter averaging steps.",
    },
    ":CONF:KILL": {
        "input_type": int,
        "allowed_input_values": [0, 1],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Set function kill enable (1) or kill disable (0).",
    },
    ":CONF:ADJUST": {
        "input_type": int,
        "allowed_input_values": [0, 1],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Set the fine adjustment function on (1) or off (0).",
    },
    ":CONF:CAN:ADDR": {
        "input_type": int,
        "allowed_input_values": [*range(64)],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Set the module's CAN bus address.",
    },
    ":CONF:CAN:BITRATE": {
        "input_type": int,
        "allowed_input_values": [125000, 250000],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Set the module's CAN bus bit rate.",
    },
    ":CONF:SERIAL:BAUD": {
        "input_type": int,
        "allowed_input_values": [],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Set the device's serial baud rate.",
    },
    ":CONF:SERIAL:ECHO": {
        "input_type": int,
        "allowed_input_values": [0, 1],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Enable or disable serial echo.",
    },
    ":CONF:EVENT:MASK": {
        "input_type": int,
        "allowed_input_values": [],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Set the Module Event Mask register.",
    },
    ":CONF:EVENT:CHANMASK": {
        "input_type": int,
        "allowed_input_values": [],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Set the Module Event Channel Mask register.",
    },
    ":SYSTEM:USER:CONFIG": {
        "input_type": int,
        "allowed_input_values": [],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Set the device to configuration mode to change the CAN bitrate or address.",
    },
    ":CONF:EVENT CLEAR": {
        "input_type": NoneType,
        "allowed_input_values": [],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Reset the Module Event Status register.",
    },
    ":CONF:EVENT": {
        "input_type": int,
        "allowed_input_values": [],
        "output_type": NoneType,
        "possible_output_values": [],
        "description": "Clear single bits or bit combinations in the Module Event Status register.",
    },
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
    check_command_input(_MON_MODULE_COMMANDS, command)
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
    check_command_input(_SET_MODULE_COMMANDS, command, value)

    if isinstance(value, float):
        value = f"{value:.3E}"

    return f"{command.strip()} {value};*OPC?\r\n".encode("ascii")
