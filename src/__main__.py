from hvps import version, HVPS
from hvps.commands.caen.module import _set_module_parameters, _mon_module_parameters
from hvps.commands.caen.channel import _set_channel_parameters, _mon_channel_parameters

import argparse


def main():
    parser = argparse.ArgumentParser(description="HVPS control")
    parser.add_argument("--version", action="version", version=version.__version__)

    parser.add_argument(
        "--port",
        default=None,
        help="Serial port. If not specified it will attempt to automatically find",
    )
    parser.add_argument(
        "--baud",
        default=None,
        help="Baud rate for serial communication. "
        "If not specified it will attempt to automatically find",
    )
    parser.add_argument(
        "--module", type=int, default=0, help="Module number. CAEN only?"
    )  # TODO: update this once iseg is implemented
    parser.add_argument(
        "--channel", default=None, help="HV PS channel"
    )  # Required argument
    parser.add_argument(
        "--test", action="store_true", help="Testing mode. Do not run commands"
    )

    subparsers = parser.add_subparsers(dest="brand", help="Select brand (caen or iseg)")

    # CAEN
    caen_parser = subparsers.add_parser("caen", help="CAEN HVPS")
    caen_parser.add_argument("parameter", nargs=1, help="Parameter name")
    caen_parser.add_argument(
        "value",
        nargs="?",
        default=None,
        help="Value to set parameter to, if applicable",
    )

    # iseg
    iseg_parser = subparsers.add_parser("iseg", help="iseg HVPS")

    args = parser.parse_args()

    # validate parameters
    parameter = None
    value = None
    if args.brand == "caen":
        parameter = str(args.parameter[0]).upper()
        value = args.value
        channel = args.channel
        if channel is None:
            # parameter is at module level
            valid_parameters = (
                list(_mon_module_parameters.keys())
                if value is None
                else list(_set_module_parameters.keys())
            )
        else:
            # parameter is at channel level
            valid_parameters = (
                list(_mon_channel_parameters.keys())
                if value is None
                else list(_set_channel_parameters.keys())
            )

        if parameter not in valid_parameters:
            raise Exception(f"Parameter {parameter} not in {valid_parameters}")

    elif args.brand == "iseg":
        raise NotImplementedError("iseg not implemented yet")

    if args.test:
        print("Testing mode enabled, commands will not be run")
        return

    hvps = HVPS(port=args.port, baudrate=args.baud)
    if args.brand == "caen":
        module = hvps.module(args.module)
        channel = module.channel(args.channel) if args.channel is not None else None
        if value is None:
            if not channel:
                result = getattr(module, parameter)
            else:
                result = getattr(channel, parameter)

            print(f"{parameter}: {result}")

        else:
            if not channel:
                setattr(module, parameter, value)
            else:
                setattr(channel, parameter, value)

            print(f"{parameter} set to {value}")


if __name__ == "__main__":
    main()
