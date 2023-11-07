from hvps.utils import get_serial_ports
from hvps import Iseg

import pytest
import sys
import logging

serial_port = ""  # change this to the serial port you are using
serial_baud = 9600
timeout = 5.0


def serial_port_available():
    ports = get_serial_ports()
    return ports != []


def is_macos():
    return sys.platform == "Darwin"


serial_skip_decorator = pytest.mark.skipif(
    serial_port == "", reason="No serial ports set"
)


@serial_skip_decorator
def test_iseg_module_monitor():
    iseg = Iseg(
        port=serial_port,
        baudrate=serial_baud,
        connect=True,
        timeout=timeout,
        logging_level=logging.DEBUG,
    )

    print(
        f"Serial port status: connected: {iseg.connected}, port: {iseg.port}, baudrate: {iseg.baudrate}, timeout: {iseg.timeout}"
    )
    module = iseg.module(0)

    # TODO: check outputs are not None

    number_of_channels = module.number_of_channels
    print(f"number_of_channels: {number_of_channels}")

    firmware_release = module.firmware_release
    print(f"firmware_release: {firmware_release}")

    module_status = module.module_status
    print(f"module_status: {module_status}")

    filter_averaging_steps = module.filter_averaging_steps
    print(f"filter_averaging_steps: {filter_averaging_steps}")

    kill_enable = module.kill_enable
    print(f"kill_enable: {kill_enable}")

    adjustment = module.adjustment
    print(f"adjustment: {adjustment}")

    module_can_address = module.module_can_address
    print(f"module_can_address: {module_can_address}")

    module_can_bitrate = module.module_can_bitrate
    print(f"module_can_bitrate: {module_can_bitrate}")

    serial_baud_rate = module.serial_baud_rate
    print(f"serial_baud_rate: {serial_baud_rate}")

    serial_echo_enable = module.serial_echo_enable
    print(f"serial_echo_enable: {serial_echo_enable}")

    serial_echo_enabled = module.serial_echo_enabled
    print(f"serial_echo_disabled: {serial_echo_enabled}")

    module_voltage_limit = module.module_voltage_limit
    print(f"module_voltage_limit: {module_voltage_limit}")

    module_current_limit = module.module_current_limit
    print(f"module_current_limit: {module_current_limit}")

    module_voltage_ramp_speed = module.module_voltage_ramp_speed
    print(f"module_voltage_ramp_speed: {module_voltage_ramp_speed}")

    module_current_ramp_speed = module.module_current_ramp_speed
    print(f"module_current_ramp_speed: {module_current_ramp_speed}")

    module_control_register = module.module_control_register
    print(f"module_control_register: {module_control_register}")

    module_status_register = module.module_status_register
    print(f"module_status_register: {module_status_register}")

    module_event_status_register = module.module_event_status_register
    print(f"module_event_status_register: {module_event_status_register}")

    module_event_mask_register = module.module_event_mask_register
    print(f"module_event_mask_register: {module_event_mask_register}")

    module_event_channel_status_register = module.module_event_channel_status_register
    print(
        f"module_event_channel_status_register: {module_event_channel_status_register}"
    )

    module_event_channel_mask_register = module.module_event_channel_mask_register
    print(f"module_event_channel_mask_register: {module_event_channel_mask_register}")

    module_supply_voltage = module.module_supply_voltage
    print(f"module_supply_voltage: {module_supply_voltage}")

    module_supply_voltage_p24v = module.module_supply_voltage_p24v
    print(f"module_supply_voltage_p24v: {module_supply_voltage_p24v}")

    module_supply_voltage_n24v = module.module_supply_voltage_n24v
    print(f"module_supply_voltage_n24v: {module_supply_voltage_n24v}")

    module_supply_voltage_p5v = module.module_supply_voltage_p5v
    print(f"module_supply_voltage_p5v: {module_supply_voltage_p5v}")

    module_supply_voltage_p3v = module.module_supply_voltage_p3v
    print(f"module_supply_voltage_p3v: {module_supply_voltage_p3v}")

    module_supply_voltage_p12v = module.module_supply_voltage_p12v
    print(f"module_supply_voltage_p12v: {module_supply_voltage_p12v}")

    module_supply_voltage_n12v = module.module_supply_voltage_n12v
    print(f"module_supply_voltage_n12v: {module_supply_voltage_n12v}")

    module_temperature = module.module_temperature
    print(f"module_temperature: {module_temperature}")

    setvalue_changes_counter = module.setvalue_changes_counter
    print(f"setvalue_changes_counter: {setvalue_changes_counter}")

    firmware_name = module.firmware_name
    print(f"firmware_name: {firmware_name}")

    id_string = module.id_string
    print(f"id_string: {id_string}")

    instruction_set = module.instruction_set
    print(f"instruction_set: {instruction_set}")

    iseg.disconnect()


@serial_skip_decorator
def test_iseg_channel_monitor():
    iseg = Iseg(
        port=serial_port,
        baudrate=serial_baud,
        connect=True,
        timeout=timeout,
        logging_level=logging.DEBUG,
    )

    module = iseg.module(0)

    for channel in module.channels:
        print("")
        print(f"Channel: {channel.channel}")

        trip_action = channel.trip_action
        print(f"trip_action: {trip_action}")

        trip_timeout = channel.trip_timeout
        print(f"trip_timeouts: {trip_timeout}")

        output_mode = channel.output_mode
        print(f"output_mode: {output_mode}")

        available_output_modes = channel.available_output_modes
        print(f"available_output_modes: {available_output_modes}")

        output_polarity = channel.output_polarity
        print(f"output_polarity: {output_polarity}")

        # TODO: channel.external_inhibit_action returns an empty list
        # external_inhibit_action = channel.external_inhibit_action
        # print(f"external_inhibit_action: {external_inhibit_action}")

        available_output_polarities = channel.available_output_polarities
        print(f"available_output_polarities: {available_output_polarities}")

        voltage_set = channel.voltage_set
        print(f"voltage_set: {voltage_set}")

        voltage_limit = channel.voltage_limit
        print(f"voltage_limit: {voltage_limit}")

        voltage_nominal = channel.voltage_nominal
        print(f"voltage_nominal: {voltage_nominal}")

        voltage_mode = channel.voltage_mode
        print(f"voltage_mode: {voltage_mode}")

        voltage_mode_list = channel.voltage_mode_list
        print(f"voltage_mode_list: {voltage_mode_list}")

        voltage_bounds = channel.voltage_bounds
        print(f"voltage_bounds: {voltage_bounds}")

        set_on = channel.set_on
        print(f"set_on: {set_on}")

        emergency_off = channel.emergency_off
        print(f"emergency_off: {emergency_off}")

        current_set = channel.current_set
        print(f"current_set: {current_set}")

        current_limit = channel.current_limit
        print(f"current_limit: {current_limit}")

        current_nominal = channel.current_nominal
        print(f"current_nominal: {current_nominal}")

        current_mode = channel.current_mode
        print(f"current_mode: {current_mode}")

        modes = channel.current_mode_list
        print(f"modes: {modes}")

        bounds = channel.current_bounds
        print(f"bounds: {bounds}")

        speed = channel.current_ramp_speed
        print(f"speed: {speed}")

        speed = channel.voltage_ramp_speed
        print(f"speed: {speed}")

        speed_min = channel.voltage_ramp_speed_minimum
        print(f"speed_min: {speed_min}")

        speed_max = channel.voltage_ramp_speed_maximum
        print(f"speed_max: {speed_max}")

        speed_min = channel.current_ramp_speed_minimum
        print(f"speed_min: {speed_min}")

        speed_max = channel.current_ramp_speed_maximum
        print(f"speed_max: {speed_max}")

        control = channel.channel_control
        print(f"control: {control}")

        status = channel.channel_status
        print(f"status: {status}")

        mask = channel.channel_event_mask
        print(f"mask: {mask}")

        voltage = channel.measured_voltage
        print(f"voltage: {voltage}")

        current = channel.measured_current
        print(f"current: {current}")

        speed = channel.channel_voltage_ramp_up_speed
        print(f"speed: {speed}")

        speed = channel.channel_voltage_ramp_down_speed
        print(f"speed: {speed}")

        speed = channel.channel_current_ramp_up_speed
        print(f"speed: {speed}")

        speed = channel.channel_current_ramp_down_speed
        print(f"speed: {speed}")

    iseg.disconnect()
