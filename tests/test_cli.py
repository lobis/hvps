import os
import subprocess
import sys
import pytest


def run_main_with_arguments(arguments: list) -> tuple:
    main_file_path = os.path.join(
        os.path.dirname(__file__), "..", "src/hvps", "__main__.py"
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


def test_cli_channel_set():
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
    ]:
        arguments = [
            "--port",
            "/dev/ttyUSB0",
            "--baud",
            "9600",
            "--module",
            "1",
            "--channel",
            "2",
            "--test",
            "caen",
            f"{parameter}",
            "100",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")

        assert exit_code == 0, f"exit_code: {exit_code} for arguments: {arguments}"
