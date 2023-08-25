from __future__ import annotations


# TODO: change values for dictionary with possible values and description
_MON_MODULE_COMMANDS = {
    "number_of_channels": {
        "command": ":READ:MODULE:CHANNELNUMBER",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "The number of channels in the module.",
    },
    "firmware_release": {
        "command": ":READ:FIRMWARE:RELEASE",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Read out Firmware Release (XX.X)",
    },
    "filter_averaging_steps": {
        "command": ":CONF:AVER",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the digital filter averaging steps.",
    },
    "kill_enable": {
        "command": ":CONF:KILL",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Get the current value for the kill enable function.",
    },
    "adjustment": {
        "command": ":CONF:ADJUST",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Get the fine adjustment state.",
    },
    "module_can_address": {
        "command": ":CONF:CAN:ADDR",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the module's CAN bus address.",
    },
    "module_can_bitrate": {
        "command": ":CONF:CAN:BITRATE",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the module's CAN bus bit rate.",
    },
    "serial_baud_rate": {
        "command": ":CONF:SERIAL:BAUD",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the device's serial baud rate.",
    },
    "serial_echo_enable": {
        "command": ":CONF:SERIAL:ECHO",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Check if serial echo is enabled or disabled.",
    },
    "module_current_limit": {
        "command": ":READ:CURR:LIM",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module's current limit in percent.",
    },
    "module_voltage_limit": {
        "command": ":READ:VOLT:LIM",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module's voltage limit in percent.",
    },
    "module_voltage_ramp_speed": {
        "command": ":READ:RAMP:VOLT",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module's voltage ramp speed in percent/second.",
    },
    "module_current_ramp_speed": {
        "command": ":READ:RAMP:CURR",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module's current ramp speed in percent/second.",
    },
    "module_control_register": {
        "command": ":READ:MODULE:CONTROL",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Control register",
    },
    "module_status_register": {
        "command": ":READ:MODULE:STATUS",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Status register",
    },
    "module_event_status_register": {
        "command": ":READ:MODULE:EVENT:STATUS",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Event Status register",
    },
    "module_event_mask_register": {
        "command": ":READ:MODULE:EVENT:MASK",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Event Mask register",
    },
    "module_event_channel_status_register": {
        "command": ":READ:MODULE:EVENT:CHANSTAT",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Event Channel Status register",
    },
    "module_event_channel_mask_register": {
        "command": ":READ:MODULE:EVENT:CHANMASK",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the Module Event Channel Mask register",
    },
    "module_supply_voltage": {
        "command": ":READ:MODULE:SUPPLY? (@0-6)",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Query the module supply voltages",
    },
    "module_supply_voltage_p24v": {
        "command": ":READ:MODULE:SUPPLY:P24V",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module supply voltage +24 Volt",
    },
    "module_supply_voltage_n24v": {
        "command": ":READ:MODULE:SUPPLY:N24V",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module supply voltage -24 Volt",
    },
    "module_supply_voltage_p5v": {
        "command": ":READ:MODULE:SUPPLY:P5V",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module supply voltage +5 Volt",
    },
    "module_supply_voltage_p3v": {
        "command": ":READ:MODULE:SUPPLY:P3V",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module internal supply voltage +3.3 Volt",
    },
    "module_supply_voltage_p12v": {
        "command": ":READ:MODULE:SUPPLY:P12V",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module internal supply voltage +12 Volt",
    },
    "module_supply_voltage_n12v": {
        "command": ":READ:MODULE:SUPPLY:N12V",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module internal supply voltage -12 Volt",
    },
    "module_temperature": {
        "command": ":READ:MODULE:TEMPERATURE",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": float,
        "possible_output_values": [],
        "description": "Query the module temperature in degree Celsius",
    },
    "setvalue_changes_counter": {
        "command": ":READ:MODULE:SETVALUE",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": int,
        "possible_output_values": [],
        "description": "Query the setvalue changes counter",
    },
    "firmware_name": {
        "command": ":READ:FIRMWARE:NAME",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Query the module's firmware name",
    },
    "id_string": {
        "command": "*IDN",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Query the module's identification string",
    },
    "instruction_set": {
        "command": "*INSTR",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": str,
        "possible_output_values": [],
        "description": "Query the currently selected instruction set. All devices support the EDCP command set. Some devices (HPS, EHQ) support further command sets, refer to the devices manual for them.",
    },
}

_SET_MODULE_COMMANDS = {
    "filter_averaging_steps": {
        "command": ":CONF:AVER",
        "input_type": int,
        "allowed_input_values": [1, 16, 64, 256, 512, 1024],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the number of digital filter averaging steps.",
    },
    "kill_enable": {
        "command": ":CONF:KILL",
        "input_type": int,
        "allowed_input_values": [0, 1],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set function kill enable (1) or kill disable (0).",
    },
    "adjustment": {
        "command": ":CONF:ADJUST",
        "input_type": int,
        "allowed_input_values": [0, 1],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the fine adjustment function on (1) or off (0).",
    },
    "module_can_address": {
        "command": ":CONF:CAN:ADDR",
        "input_type": int,
        "allowed_input_values": [*range(64)],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the module's CAN bus address.",
    },
    "module_can_bitrate": {
        "command": ":CONF:CAN:BITRATE",
        "input_type": int,
        "allowed_input_values": [125000, 250000],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the module's CAN bus bit rate.",
    },
    "serial_baud_rate": {
        "command": ":CONF:SERIAL:BAUD",
        "input_type": int,
        "allowed_input_values": [115200],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the device's serial baud rate.",
    },
    "serial_echo_enable": {
        "command": ":CONF:SERIAL:ECHO",
        "input_type": int,
        "allowed_input_values": [0, 1],
        "output_type": None,
        "possible_output_values": [],
        "description": "Enable or disable serial echo.",
    },
    "module_event_mask_register": {
        "command": ":CONF:EVENT:MASK",
        "input_type": int,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the Module Event Mask register.",
    },
    "module_event_channel_mask_register": {
        "command": ":CONF:EVENT:CHANMASK",
        "input_type": int,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the Module Event Channel Mask register.",
    },
    "enter_configuration_mode": {
        "command": ":SYSTEM:USER:CONFIG",
        "input_type": int,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Set the device to configuration mode to change settings.",
    },
    "reset_module_event_status": {
        "command": ":CONF:EVENT CLEAR",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Reset the Module Event Status register.",
    },
    "clear_module_event_status_bits": {
        "command": ":CONF:EVENT",
        "input_type": int,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Clear single bits or bit combinations in the Module Event Status register.",
    },
    "clear_all_event_status_registers": {
        "command": "*CLS",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Clear the Module Event Status and all Channel Event Status registers.",
    },
    "reset_to_save_values": {
        "command": "*RST",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Reset the device to save values: \n\
                        - turn high voltage off with ramp for all channel \n\
                        - set voltage set Vset to zero for all channels \n\
                        - set current set Iset to the current nominal for all channels",
    },
    "set_command_set": {
        "command": "*INSTR",
        "input_type": str,
        "allowed_input_values": ["EDCP"],
        "output_type": None,
        "possible_output_values": [],
        "description": "Switch the device to the EDCP command set. Only for devices that support other command sets beside EDCP. For HPS and EHQ with other command sets, refer to the devices manual. This setting is permanent.",
    },
    "local_lockout": {
        "command": "*LLO",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Local Lockout: Front panel buttons and rotary encoders are disabled. The device can only be controlled remotely.",
    },
    "goto_local": {
        "command": "*GTL",
        "input_type": None,
        "allowed_input_values": [],
        "output_type": None,
        "possible_output_values": [],
        "description": "Go to local: Front panel buttons and rotary encoders are enabled. The device can be controlled locally.",
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

    if isinstance(value, float):
        value = f"{value:.3E}"

    return f"{command.strip()} {value};*OPC?\r\n".encode("ascii")
