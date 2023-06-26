from hvps import ISEG
import pytest
from hvps.commands.iseg import _get_set_channel_command, _get_mon_channel_command
from hvps.devices.iseg.channel import Channel
import serial

from .test_caen_serial import serial_skip_decorator

serial_port = "COM4"  # change this to the serial port you are using
serial_baud = 9600
timeout = 5.0


@serial_skip_decorator
def test_iseg_module_monitor():
    ...


@serial_skip_decorator
def test_iseg_channel_monitor():
    ser = serial.Serial(serial_port, serial_baud, timeout=timeout)

    channel = Channel(ser, 0)

    trip_action = channel.trip_action
    print(f"trip_action: {trip_action}")

    output_mode = channel.output_mode
    print(f"output_mode: {output_mode}")

    output_polarity = channel.output_polarity
    print(f"output_polarity: {output_polarity}")

    available_output_polarities = channel.available_output_polarities
    print(f"available_output_polarities: {available_output_polarities}")

    voltage_set = channel.voltage_set
    print(f"voltage_set: {voltage_set}")

    voltage_limit = channel.voltage_limit
    print(f"voltage_limit: {voltage_limit}")

    voltage_nominal = channel.voltage_nominal
    print(f"voltage_nominal: {voltage_nominal}")

    available_output_modes = channel.available_output_modes
    print(f"available_output_modes: {available_output_modes}")
