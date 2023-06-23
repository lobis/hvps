from hvps import ISEG
import pytest
from hvps.commands.iseg import _get_set_channel_command, _get_mon_channel_command
from hvps.devices.iseg.channel import Channel
from hvps.devices.iseg.module import Module
import serial

serial_port = "COM4"  # change this to the serial port you are using
serial_baud = 9600
timeout = 5.0


def test_iseg_module_monitor():
    ser = serial.Serial(serial_port, serial_baud, timeout=timeout)
    module = Module(ser)

    number_of_channels = module.number_of_channels
    print(f"number_of_channels: {number_of_channels}")

    firmware_release = module.firmware_release
    print(f"firmware_release: {firmware_release}")

    module_status = module.module_status
    print(f"module_status: {module_status}")


def test_iseg_channel_monitor():
    ser = serial.Serial(serial_port, serial_baud, timeout=timeout)

    module = Module(ser)
    module.channel(0)

    trip_action = module.channel(0).trip_action
    print(f"trip_action: {trip_action}")

    output_mode = module.channel(0).output_mode
    print(f"output_mode: {output_mode}")

    output_polarity = module.channel(0).output_polarity
    print(f"output_polarity: {output_polarity}")

    available_output_polarities = module.channel(0).available_output_polarities
    print(f"available_output_polarities: {available_output_polarities}")

    voltage_set = module.channel(0).voltage_set
    print(f"voltage_set: {voltage_set}")

    voltage_limit = module.channel(0).voltage_limit
    print(f"voltage_limit: {voltage_limit}")

    voltage_nominal = module.channel(0).voltage_nominal
    print(f"voltage_nominal: {voltage_nominal}")

    available_output_modes = module.channel(0).available_output_modes
    print(f"available_output_modes: {available_output_modes}")
