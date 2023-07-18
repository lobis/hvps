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


def test_cli_caen_channel_mon():
    for parameter in [
        "VSET",
        "VMIN",
        "VMAX",
        "VDEC",
        "VMON",
        "ISET",
        "IMIN",
        "IMAX",
        "ISDEC",
        "IMON",
        "IMRANGE",
        "IMDEC",
        "MAXV",
        "MVMIN",
        "MVMAX",
        "MVDEC",
        "RUP",
        "RUPMIN",
        "RUPMAX",
        "RUPDEC",
        "RDW",
        "RDWMIN",
        "RDWMAX",
        "RDWDEC",
        "TRIP",
        "TRIPMIN",
        "TRIPMAX",
        "TRIPDEC",
        "PDWN",
        "POL",
        "STAT",
        "INVALID_PARAMETER",
    ]:
        arguments = [
            "--port",
            "/dev/ttyUSB0",
            "--baud",
            "9600",
            "--channel",
            "0",
            "--test",
            "caen",
            "--module",
            "1",
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


def test_cli_caen_channel_set():
    for parameter in [
        "VSET",
        "ISET",
        "MAXV",
        "RUP",
        "RDW",
        "TRIP",
        "PDWN",
        "IMRANGE",
        "ON",
        "OFF",
    ]:
        arguments = [
            "--port",
            "/dev/ttyUSB0",
            "--baud",
            "9600",
            "--channel",
            "0",
            "--test",
            "caen",
            "--module",
            "1",
            f"{parameter}",
            "100",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")


def test_cli_caen_module_mon():
    for parameter in [
        "number_of_channels",
        "name",
        "firmware_release",
        "serial_number",
        "interlock_status",
        "interlock_mode",
        "local_bus_termination_status",
        "control_mode",
        "INVALID_PARAMETER",
    ]:
        arguments = [
            "--port",
            "/dev/ttyUSB0",
            "--baud",
            "9600",
            "--test",
            "caen",
            "--module",
            "1",
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


def test_cli_caen_module_set():
    for parameter in [
        "interlock_mode",
        "clear_alarm_signal",
    ]:
        arguments = [
            "--port",
            "/dev/ttyUSB0",
            "--baud",
            "9600",
            "--test",
            "caen",
            "--module",
            "2",
            f"{parameter}",
            "200",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")


def test_cli_iseg_channel_mon():
    for parameter in [
        "trip_action",
        "trip_timeout",
        "external_inhibit_action",
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
            "/dev/ttyUSB0",
            "--baud",
            "9600",
            "--channel",
            "0",
            "--test",
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


def test_cli_iseg_channel_set():
    for parameter in [
        "trip_action",
        "trip_timeout",
        "external_inhibit_action",
        "output_mode",
        "output_polarity",
        "voltage_set",
        "voltage_bounds",
        "clear_emergency_off",
        "current_set",
        "current_bounds",
        "set_channel_voltage_ramp_up_down_speed",
        "channel_voltage_ramp_up_speed",
        "channel_voltage_ramp_down_speed",
        "set_channel_current_ramp_up_down_speed",
        "channel_current_ramp_up_speed",
        "channel_current_ramp_down_speed",
        "switch_on_high_voltage",
        "switch_off_high_voltage",
        "shutdown_channel_high_voltage",
        "clear_channel_emergency_off",
        "clear_event_status",
        "clear_event_bits",
        "set_event_mask",
    ]:
        arguments = [
            "--port",
            "/dev/ttyUSB0",
            "--baud",
            "9600",
            "--channel",
            "0",
            "--test",
            "iseg",
            f"{parameter}",
            "100",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")


def test_cli_iseg_module_mon():
    for parameter in [
        "channel",
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
            "/dev/ttyUSB0",
            "--baud",
            "9600",
            "--test",
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


def test_cli_iseg_module_set():
    for parameter in [
        "serial_baud_rate",
        "serial_echo_enable",
        "filter_averaging_steps",
        "kill_enable",
        "adjustment",
        "module_event_mask_register",
        "module_event_channel_mask_register",
        "module_can_address",
        "module_can_bitrate",
        "enter_configuration_mode",
        "exit_configuration_mode",
        "set_serial_echo_enabled",
        "clear_module_event_status_bits",
        "clear_all_event_status_registers",
        "reset_to_save_values",
        "set_command_set",
        "local_lockout",
        "goto_local",
    ]:
        arguments = [
            "--port",
            "/dev/ttyUSB0",
            "--baud",
            "9600",
            "--test",
            "iseg",
            f"{parameter}",
            "200",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")
