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
            "COM6",
            "--baud",
            "9600",
            "--channel",
            "0",
            "caen",
            "--module",
            "0",
            f"{parameter}",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")

        # dump previous messages to a txt file named as the test source file + _results.txt
        with open(__file__[:-3] + "_results.txt", "w") as f:
            f.write(f"arguments: {arguments}\n")
            f.write(f"stdout: {stdout}\n")
            f.write(f"stderr: {stderr}\n")
            f.write(f"exit_code: {exit_code}\n")
        f.close()

        exit_code_expected = 0 if parameter not in ["INVALID_PARAMETER"] else 1
        assert (
            exit_code == exit_code_expected
        ), f"exit_code: {exit_code} for arguments: {arguments}"


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
        "board_alarm_status",
        "INVALID_PARAMETER",
    ]:
        arguments = [
            "--port",
            "COM6",
            "--baud",
            "9600",
            "caen",
            "--module",
            "0",
            f"{parameter}",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")

        # dump previous messages to a txt file named as the test source file + _results.txt
        with open(__file__[:-3] + "_results.txt", "w") as f:
            f.write(f"arguments: {arguments}\n")
            f.write(f"stdout: {stdout}\n")
            f.write(f"stderr: {stderr}\n")
            f.write(f"exit_code: {exit_code}\n")
        f.close()

        exit_code_expected = 0 if parameter not in ["INVALID_PARAMETER"] else 1
        assert (
            exit_code == exit_code_expected
        ), f"exit_code: {exit_code} for arguments: {arguments}"
