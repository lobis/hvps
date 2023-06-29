from hvps import __version__ as hvps_version, Caen
from hvps.commands.caen.module import _set_module_commands, _mon_module_commands
from hvps.commands.caen.channel import _set_channel_commands, _mon_channel_commands

from serial.tools import list_ports

import argparse
import logging


def main():
    parser = argparse.ArgumentParser(description="HVPS control")
    parser.add_argument("--version", action="version", version=hvps_version)

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
    subparsers.add_parser("iseg", help="iseg HVPS")

    args = parser.parse_args()
    logging.basicConfig(level=args.log.upper())
    if args.ports:
        ports = [port.device for port in list_ports.comports()]
        print(f"Number of ports available: {len(ports)}")
        for port in ports:
            print(f"  - {port}")
        exit(0)
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
            monitor_commands = list(_mon_module_commands.keys())
            set_commands = list(_set_module_commands.keys())
            monitor_mode = parameter in monitor_commands
            if not monitor_mode and parameter not in set_commands:
                raise Exception(
                    f"Parameter '{parameter}' not a valid monitor parameter: {monitor_commands} or set parameter: {set_commands}"
                )

        else:
            # parameter is at channel level
            monitor_commands = list(_mon_channel_commands.keys())
            set_commands = list(_set_channel_commands.keys())

            monitor_mode = parameter in monitor_commands
            if parameter in monitor_commands and set_commands:
                if value is not None:
                    monitor_mode = False  # some parameters such as 'VSET' can be both monitor and set

            if not monitor_mode and parameter not in set_commands:
                raise Exception(
                    f"Channel parameter '{parameter}' not a valid monitor parameter: {monitor_commands} or set "
                    f"parameter: {set_commands}"
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

    if args.brand == "caen":
        caen = Caen(port=args.port, baudrate=args.baud)
        module = caen.module(args.module)
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
                        channel.turn_on()
                        print(f"Channel {channel} turned on")
                    else:
                        channel.turn_off()
                        print(f"Channel {channel} turned off")
                else:
                    setattr(channel, parameter, value)
                    print(f"{parameter} set to {value}")


if __name__ == "__main__":
    main()
