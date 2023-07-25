from hvps.devices.iseg.channel import Channel
from hvps.utils import get_serial_ports
from hvps import Iseg

import pytest
import sys
import serial
import logging

serial_port = "COM4"  # change this to the serial port you are using
serial_baud = 9600
timeout = 5.0


def serial_port_available():
    ports = get_serial_ports()
    return ports != []


def is_macos():
    return sys.platform == "Darwin"


serial_skip_decorator = pytest.mark.skipif(
    serial_port_available() or not is_macos(), reason="No serial ports available"
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

    # Setter methods
    module.serial_baud_rate = 9600
    module.serial_echo_enable = 1
    with pytest.raises(ValueError):
        module.serial_echo_enable = 2

    module.filter_averaging_steps = 256
    with pytest.raises(ValueError):
        module.filter_averaging_steps = 257

    module.kill_enable = 1
    with pytest.raises(ValueError):
        module.kill_enable = 2

    module.adjustment = 0
    with pytest.raises(ValueError):
        module.adjustment = 2

    module.module_event_mask_register = 5

    module.module_can_address = 12
    with pytest.raises(ValueError):
        module.module_can_address = 250

    module.module_can_bitrate = 250000
    with pytest.raises(ValueError):
        module.module_can_bitrate = 250

    # Other methods
    module.enter_configuration_mode(12345)
    module.exit_configuration_mode()
    module.set_serial_echo_enabled()
    module.set_serial_echo_disabled()
    module.reset_module_event_status()
    module.clear_module_event_status_bits(8)


@serial_skip_decorator
def test_iseg_channel_monitor():
    ser = serial.Serial(serial_port, serial_baud, timeout=timeout)

    channel = Channel(ser, 0)

    # Set the action to be taken when a current trip occurs for the channel
    channel.trip_action = 1
    with pytest.raises(ValueError):
        channel.trip_action = 5

    # Set the trip timeout in milliseconds
    channel.trip_timeout = 2000
    with pytest.raises(ValueError):
        channel.trip_timeout = 0

    # Set the action to be taken when an External Inhibit event occurs for the channel
    channel.external_inhibit_action = 2
    with pytest.raises(ValueError):
        channel.external_inhibit_action = 5

    # Set the channel output mode
    channel.output_mode = 3
    with pytest.raises(ValueError):
        channel.output_mode = 5

    # Set the output polarity of the channel
    channel.output_polarity = "n"
    with pytest.raises(ValueError):
        channel.output_polarity = "x"

    # Set the channel voltage set
    channel.voltage_set = 12.5

    # Set the channel voltage bounds
    channel.voltage_bounds = 10.0

    # Clear the channel from state emergency off
    channel.clear_emergency_off()

    # Set the channel current set
    channel.current_set = 2.5

    # Set the channel current bounds
    channel.current_bounds = 2.0

    # Set the channel voltage ramp speed for up and down direction
    channel.set_channel_voltage_ramp_up_down_speed(250)

    # Set the channel voltage ramp up speed
    channel.channel_voltage_ramp_up_speed = 200

    # Set the channel voltage ramp down speed
    channel.channel_voltage_ramp_down_speed = 150.0

    # Switch on the high voltage with the configured ramp speed
    channel.switch_on_high_voltage()

    # Switch off the high voltage with the configured ramp speed
    channel.switch_off_high_voltage()

    # Shut down the channel high voltage (without ramp)
    channel.shutdown_channel_high_voltage()

    # Clear the channel from state emergency off
    channel.clear_channel_emergency_off()

    # Clear the Channel Event Status register
    channel.clear_event_status()

    # Clears single bits or bit combinations in the Channel Event Status register
    channel.clear_event_bits(3)

    # Set the Channel Event Mask register
    channel.set_event_mask(7)
