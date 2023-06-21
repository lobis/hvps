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
    monitor_mode = False
    if args.brand == "caen":
        parameter = str(args.parameter[0]).upper()
        value = args.value
        channel = args.channel
        if channel is None:
            # parameter is at module level
            monitor_parameters = list(_mon_module_parameters.keys())
            set_parameters = list(_set_module_parameters.keys())
            monitor_mode = parameter in monitor_parameters
            if not monitor_mode and parameter not in set_parameters:
                raise Exception(
                    f"Parameter '{parameter}' not a valid monitor parameter: {monitor_parameters} or set parameter: {set_parameters}"
                )

        else:
            # parameter is at channel level
            monitor_parameters = list(_mon_channel_parameters.keys())
            set_parameters = list(_set_channel_parameters.keys())

            if parameter in monitor_parameters and set_parameters:
                raise Exception(
                    f"Parameter '{parameter}' is both a monitor and set parameter"
                )

            monitor_mode = parameter in monitor_parameters
            if not monitor_mode and parameter not in set_parameters:
                raise Exception(
                    f"Channel parameter '{parameter}' not a valid monitor parameter: {monitor_parameters} or set parameter: {set_parameters}"
                )

            if monitor_mode and value is not None:
                raise Exception(
                    f"Channel parameter {parameter} does not accept a value"
                )

            if not monitor_mode:
                # set mode
                if parameter in ["ON", "OFF"]:
                    if value is not None:
                        raise Exception(
                            f"Channel parameter {parameter} does not accept a value"
                        )
                else:
                    if value is None:
                        raise Exception(
                            f"Channel parameter {parameter} requires a value"
                        )

    elif args.brand == "iseg":
        raise NotImplementedError("iseg not implemented yet")

    if args.test:
        print("Testing mode enabled, commands will not be run")
        return

    hvps = HVPS(port=args.port, baudrate=args.baud)
    if args.brand == "caen":
        module = hvps.module(args.module)
        channel = module.channel(args.channel) if args.channel is not None else None
        if monitor_mode:
            # monitor parameter
            if not channel:
                # module level
                result = getattr(module, parameter)
            else:
                # channel level
                result = getattr(channel, parameter)

            print(f"{parameter}: {result}")

        else:
            # set parameter
            if not channel:
                # module level
                setattr(module, parameter, value)
            else:
                # channel level
                if parameter in ["ON", "OFF"]:
                    if parameter == "ON":
                        channel.on()
                        print(f"Channel {channel} turned on")
                    else:
                        channel.off()
                        print(f"Channel {channel} turned off")
                else:
                    setattr(channel, parameter, value)
                    print(f"{parameter} set to {value}")


if __name__ == "__main__":
    main()
