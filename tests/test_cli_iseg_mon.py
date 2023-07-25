import os
import subprocess
import sys


def run_main_with_arguments(arguments: list) -> tuple:
    main_file_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "src/hvps",
        "__main__.py",
    )
    main_file_path = os.path.abspath(main_file_path)

    print(f"__main__.py file path: {main_file_path}")

    process = subprocess.Popen(
        [sys.executable, main_file_path] + arguments,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    exit_code = process.returncode

    return stdout.decode(), stderr.decode(), exit_code


def test_cli_iseg_channel_mon():
    for parameter in [
        "trip_action",
        "trip_timeout",
        # TODO: doesn't give response "external_inhibit_action",
        "output_mode",
        "available_output_modes",
        "output_polarity",
        "available_output_polarities",
        "voltage_set",
        "voltage_limit",
        "voltage_nominal",
        "voltage_mode",
        "voltage_mode_list",
        "voltage_bounds",
        "set_on",
        "emergency_off",
        "current_set",
        "current_limit",
        "current_nominal",
        "current_mode",
        "current_mode_list",
        "current_bounds",
        "current_ramp_speed",
        "voltage_ramp_speed",
        "voltage_ramp_speed_minimum",
        "voltage_ramp_speed_maximum",
        "current_ramp_speed_minimum",
        "current_ramp_speed_maximum",
        "channel_control",
        "channel_status",
        "channel_event_mask",
        "measured_voltage",
        "measured_current",
        "channel_voltage_ramp_up_speed",
        "channel_voltage_ramp_down_speed",
        "channel_current_ramp_up_speed",
        "channel_current_ramp_down_speed",
        "INVALID_PARAMETER",
    ]:
        arguments = [
            "--port",
            "COM5",
            "--baud",
            "9600",
            "--channel",
            "0",
            "iseg",
            f"{parameter}",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")

        exit_code_expected = 0 if parameter not in ["INVALID_PARAMETER"] else 1
        assert (
            exit_code == exit_code_expected
        ), f"exit_code: {exit_code} for arguments: {arguments}"


def test_cli_iseg_module_mon():
    for parameter in [
        "number_of_channels",
        "firmware_release",
        "module_status",
        "filter_averaging_steps",
        "kill_enable",
        "adjustment",
        "module_can_address",
        "module_can_bitrate",
        "serial_baud_rate",
        "serial_echo_enable",
        "serial_echo_enabled",
        "module_current_limit",
        "module_voltage_limit",
        "module_voltage_ramp_speed",
        "module_current_ramp_speed",
        "module_control_register",
        "module_status_register",
        "module_event_status_register",
        "module_event_mask_register",
        "module_event_channel_status_register",
        "module_event_channel_mask_register",
        "module_supply_voltage",
        "module_supply_voltage_p24v",
        "module_supply_voltage_n24v",
        "module_supply_voltage_p5v",
        "module_supply_voltage_p3v",
        "module_supply_voltage_p12v",
        "module_supply_voltage_n12v",
        "module_temperature",
        "setvalue_changes_counter",
        "firmware_name",
        "id_string",
        "instruction_set",
        "INVALID_PARAMETER",
    ]:
        arguments = [
            "--port",
            "COM5",
            "--baud",
            "9600",
            "iseg",
            f"{parameter}",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")

        exit_code_expected = 0 if parameter not in ["INVALID_PARAMETER"] else 1
        assert (
            exit_code == exit_code_expected
        ), f"exit_code: {exit_code} for arguments: {arguments}"
