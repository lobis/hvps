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


def test_cli_serial():
    """Tests the cli-api interface when serial port is connected"""
    for arguments in [
        [
            "--port",
            "COM6",
            "--baud",
            "115200",
            "--channel",
            "0",
            "caen",
            "--module",
            "0",
            "VSET",
            "20",
        ],
        [
            "--port",
            "COM6",
            "--baud",
            "115200",
            "--channel",
            "0",
            "caen",
            "--module",
            "0",
            "VSET",
        ],
        [
            "--port",
            "COM6",
            "--baud",
            "115200",
            "caen",
            "--module",
            "0",
            "number_of_channels",
        ],
        [
            "--port",
            "COM6",
            "--baud",
            "115200",
            "caen",
            "--module",
            "0",
            "interlock_mode",
            "OPEN",
        ],
        [
            "--port",
            "COM5",
            "--baud",
            "115200",
            "--channel",
            "0",
            "iseg",
            "--module",
            "0",
            "trip_action",
            "1",
        ],
        [
            "--port",
            "COM5",
            "--baud",
            "115200",
            "--channel",
            "0",
            "iseg",
            "--module",
            "0",
            "trip_action",
        ],
        [
            "--port",
            "COM5",
            "--baud",
            "115200",
            "iseg",
            "--module",
            "0",
            "number_of_channels",
        ],
        [
            "--port",
            "COM5",
            "--baud",
            "115200",
            "caen",
            "--module",
            "0",
            "clear_all_event_status_registers",
        ],
    ]:
        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")

        exit_code_expected = 0 if parameter not in ["INVALID_PARAMETER"] else 1
        assert (
            exit_code == exit_code_expected
        ), f"exit_code: {exit_code} for arguments: {arguments}"
