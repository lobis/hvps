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


def test_cli_caen_channel_set():
    for parameter in [
        ("VSET", "20"),
        ("ISET", "5"),
        ("MAXV", "50"),
        ("RUP", "2"),
        ("RDW", "3"),
        ("TRIP", "5"),
        ("PDWN", "RAMP"),
        ("IMRANGE", "HIGH"),
        ("turn_on", ""),
        ("turn_off", ""),
    ]:
        arguments = [
            "--port",
            "COM6",
            "--baud",
            "115200",
            "--channel",
            "0",
            "caen",
            "--module",
            "0",
            f"{parameter[0]}",
            f"{parameter[1]}",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")


def test_cli_caen_module_set():
    for parameter in [
        ("interlock_mode", "OPEN"),
        ("clear_alarm_signal", ""),
    ]:
        arguments = [
            "--port",
            "COM6",
            "--baud",
            "115200",
            "caen",
            "--module",
            "0",
            f"{parameter[0]}",
            f"{parameter[1]}",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")
