from hvps.utils import get_serial_ports
from hvps import Iseg

import pytest
import sys
import logging

serial_port = "COM5"  # change this to the serial port you are using
serial_baud = 9600
timeout = 5.0


def serial_port_available():
    ports = get_serial_ports()
    return ports != []


def is_macos():
    return sys.platform == "Darwin"


serial_skip_decorator = pytest.mark.skipif(
    not serial_port_available() or is_macos(), reason="No serial ports available"
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

    module = iseg.module(0)

    # Setter methods
    module.serial_baud_rate = 115200
    with pytest.raises(ValueError):
        module.serial_echo_enable = 2

    prev_filter_averaging_steps = module.filter_averaging_steps
    module.filter_averaging_steps = 256
    with pytest.raises(ValueError):
        module.filter_averaging_steps = 257
    module.filter_averaging_steps = prev_filter_averaging_steps

    prev_kill_enable = module.kill_enable
    module.kill_enable = 1
    with pytest.raises(ValueError):
        module.kill_enable = 2
    module.kill_enable = prev_kill_enable

    prev_adjustment = module.adjustment
    module.adjustment = 0
    with pytest.raises(ValueError):
        module.adjustment = 2
    module.adjustment = prev_adjustment

    module.module_event_mask_register = 5

    id_string = module.id_string

    # Other methods
    module.enter_configuration_mode(id_string[2])

    prev_module_can_address = module.module_can_address
    module.module_can_address = 12
    with pytest.raises(ValueError):
        module.module_can_address = 250
    module.module_can_address = prev_module_can_address

    prev_module_can_bitrate = module.module_can_bitrate
    module.module_can_bitrate = 250000
    with pytest.raises(ValueError):
        module.module_can_bitrate = 250
    module.module_can_bitrate = prev_module_can_bitrate

    module.exit_configuration_mode()
    module.set_serial_echo_enabled()

    """
    Be careful when switching off the echo as there is no other possibility to
    synchronize the HV device with the computer (no hardware/software
    handshake).
    This mode is only available for compatibility reasons and without support.

    module.set_serial_echo_disabled()
    """

    module.reset_module_event_status()
    module.clear_module_event_status_bits(8)
    module.clear_all_event_status_registers()
    module.reset_to_save_values()

    """
    Switch the device to the EDCP command set.
    Only for devices that support other command sets beside EDCP.
    For HPS and EHQ with other command sets, refer to the devices manual.
    This setting is permanent.

    module.set_command_set("EDCP")
    """

    module.local_lockout()
    module.goto_local()


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

        # Set the action to be taken when a current trip occurs for the channel
        prev_trip_action = channel.trip_action
        channel.trip_action = 1
        channel.trip_action = prev_trip_action
        with pytest.raises(ValueError):
            channel.trip_action = 5

        # Set the trip timeout in milliseconds
        prev_trip_timeout = channel.trip_timeout
        channel.trip_timeout = 20
        channel.trip_timeout = prev_trip_timeout
        with pytest.raises(ValueError):
            channel.trip_timeout = -1

        # Set the action to be taken when an External Inhibit event occurs for the channel
        # prev_external_inhibit_action = channel.external_inhibit_action
        # channel.external_inhibit_action = 2
        # channel.external_inhibit_action = prev_external_inhibit_action
        # with pytest.raises(ValueError):
        #    channel.external_inhibit_action = 5

        # Set the channel output mode
        available_output_modes = channel.available_output_modes
        if len(available_output_modes) != 0:
            prev_output_mode = channel.output_mode
            channel.output_mode = available_output_modes[0]
            channel.output_mode = prev_output_mode
            with pytest.raises(ValueError):
                channel.output_mode = 5

        # Set the output polarity of the channel
        prev_output_polarity = channel.output_polarity
        channel.output_polarity = "n"
        channel.output_polarity = prev_output_polarity
        with pytest.raises(ValueError):
            channel.output_polarity = "x"

        # Set the channel voltage set
        prev_voltage_set = channel.voltage_set
        channel.voltage_set = 15
        channel.voltage_set = prev_voltage_set

        # Set the channel voltage bounds
        prev_voltage_bounds = channel.voltage_bounds
        channel.voltage_bounds = 20.0
        channel.voltage_bounds = prev_voltage_bounds

        # Set the channel current set
        prev_current_set = channel.current_set
        channel.current_set = 0.0000005
        channel.current_set = prev_current_set

        # Set the channel current bounds
        prev_current_bounds = channel.current_bounds
        channel.current_bounds = 0.00000002
        channel.current_bounds = prev_current_bounds

        # Set the channel voltage ramp up speed
        prev_channel_voltage_ramp_up_speed = channel.channel_voltage_ramp_up_speed
        channel.channel_voltage_ramp_up_speed = 10
        channel.channel_voltage_ramp_up_speed = prev_channel_voltage_ramp_up_speed

        # Set the channel voltage ramp down speed
        prev_channel_voltage_ramp_down_speed = channel.channel_voltage_ramp_down_speed
        channel.channel_voltage_ramp_down_speed = 10
        channel.channel_voltage_ramp_down_speed = prev_channel_voltage_ramp_down_speed

        # TODO: the NHR says the command is processed but nothing changes
        # Set the channel voltage ramp speed for up and down direction
        # prev_set_channel_voltage_ramp_up_speed = channel.channel_voltage_ramp_up_speed
        # prev_set_channel_voltage_ramp_down_speed = channel.channel_voltage_ramp_down_speed
        # channel.set_channel_voltage_ramp_up_down_speed(5)
        # channel.channel_voltage_ramp_up_speed = prev_set_channel_voltage_ramp_up_speed
        # channel.channel_voltage_ramp_down_speed = prev_set_channel_voltage_ramp_down_speed

        # Set the channel current ramp up speed
        prev_channel_current_ramp_up_speed = channel.channel_current_ramp_up_speed
        channel.channel_current_ramp_up_speed = 0.000008
        channel.channel_current_ramp_up_speed = prev_channel_current_ramp_up_speed

        # Set the channel current ramp down speed
        prev_channel_current_ramp_down_speed = channel.channel_current_ramp_down_speed
        channel.channel_current_ramp_down_speed = 0.000008
        channel.channel_current_ramp_down_speed = prev_channel_current_ramp_down_speed

        # TODO: the NHR says the command is processed but nothing changes
        # Set the channel current ramp speed for up and down direction
        # prev_channel_current_ramp_up_speed = channel.channel_current_ramp_up_speed
        # prev_channel_current_ramp_down_speed = channel.channel_current_ramp_down_speed
        # channel.set_channel_current_ramp_up_down_speed(0.000006)
        # channel.channel_current_ramp_up_speed = prev_channel_current_ramp_up_speed
        # channel.channel_current_ramp_down_speed = prev_channel_current_ramp_down_speed

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
