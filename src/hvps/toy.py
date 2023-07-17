import argparse


def main():
    parser = argparse.ArgumentParser(description="HVPS control")
    parser.add_argument("--version", action="version")

    parser.add_argument(
        "--port",
        default=None,
        help="Serial port. If not specified it will attempt to automatically find",
    )
    parser.add_argument(
        "--ports", action="store_true", help="list serial ports available"
    )
    parser.add_argument(
        "--baud",
        default=None,
        help="Baud rate for serial communication. "
        "If not specified it will attempt to automatically find",
    )
    parser.add_argument(
        "--log",
        default="INFO",
        help="Logging level. Default: INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )

    parser.add_argument(
        "--channel", default=None, help="HV PS channel"
    )  # Required argument
    parser.add_argument(
        "--test", action="store_true", help="Testing mode. Do not run commands"
    )

    subparsers = parser.add_subparsers(dest="brand", help="Select brand (caen or iseg)")

    # CAEN
    caen_parser = subparsers.add_parser("caen", help="CAEN HVPS")
    parser.add_argument("--module", type=int, default=0, help="Module number")
    caen_parser.add_argument("parameter", nargs=1, help="Parameter name")
    caen_parser.add_argument(
        "value",
        nargs="?",
        default=None,
        help="Value to set parameter to, if applicable",
    )

    iseg_parser = subparsers.add_parser("iseg", help="iseg HVPS")
    iseg_parser.add_argument("method", nargs=1, help="Command name")
    iseg_parser.add_argument(
        "value",
        nargs="?",
        default=None,
        help="Value to set method to, if applicable",
    )

    parser.parse_args()


if __name__ == "__main__":
    main()
