import os
import subprocess
import sys


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


def test_cli_channel_mon():
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
            "--module",
            "1",
            "--channel",
            "2",
            "--test",
            "caen",
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
        "OFF",
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

        # ON / OFF are special cases, they cannot be set to a value, so they should return exit code 1
        exit_code_expected = 0 if parameter not in ["ON", "OFF"] else 1
        assert (
            exit_code == exit_code_expected
        ), f"exit_code: {exit_code} for arguments: {arguments}"


def test_cli_module_mon():
    for parameter in [
        "BDNAME",
        "BDNCH",
        "BDFREL",
        "BDSNUM",
        "BDILK",
        "BDILKM",
        "BDCTR",
        "BDTERM",
        "BDALARM",
        "INVALID_PARAMETER",
    ]:
        arguments = [
            "--port",
            "/dev/ttyUSB0",
            "--baud",
            "9600",
            "--module",
            "1",
            "--test",
            "caen",
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


def test_cli_module_set():
    for parameter in [
        "BDILKM",
        "BDCLR",
    ]:
        arguments = [
            "--port",
            "/dev/ttyUSB0",
            "--baud",
            "9600",
            "--module",
            "2",
            "--test",
            "caen",
            f"{parameter}",
            "200",
        ]

        stdout, stderr, exit_code = run_main_with_arguments(arguments)

        print(f"arguments: {arguments}")
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")
        print(f"exit_code: {exit_code}")

        # ON / OFF are special cases, they cannot be set to a value, so they should return exit code 1
        exit_code_expected = 0 if parameter not in ["ON", "OFF"] else 1
        assert (
            exit_code == exit_code_expected
        ), f"exit_code: {exit_code} for arguments: {arguments}"
