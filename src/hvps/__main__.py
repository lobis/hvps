from typing import List

from hvps import __version__ as hvps_version, Caen
from hvps.commands.caen.module import _set_module_commands, _mon_module_commands
from hvps.commands.caen.channel import _set_channel_commands, _mon_channel_commands
from hvps.commands.iseg.module import _set_module_commands, _mon_module_commands
from hvps.commands.iseg.channel import _set_channel_commands, _mon_channel_commands
from hvps.devices.iseg.module import _mon_module_methods_to_commands
from hvps.devices.iseg.module import _set_module_methods_to_commands
from hvps.devices.iseg.channel import _mon_channel_methods_to_commands
from hvps.devices.iseg.channel import _set_channel_methods_to_commands

from serial.tools import list_ports

import argparse
import logging


def _is_monitor_mode(
    command: str, monitor_commands: List[str], set_commands: List[str]
) -> bool:
    monitor_mode = command in monitor_commands
    if not monitor_mode and command not in set_commands:
        raise Exception(
            f"Channel command '{command}' not a valid monitor command: {monitor_commands} or set "
            f"command: {set_commands}"
        )
    return monitor_mode


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
        "--module", type=int, default=0, help="Module number. CAEN"
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
    caen_parser.add_argument("command", nargs=1, help="command name")
    caen_parser.add_argument(
        "value",
        nargs="?",
        default=None,
        help="Value to set command to, if applicable",
    )

    # ISEG
    subparsers.add_parser("iseg", help="iseg HVPS")
    caen_parser.add_argument("command", nargs=1, help="command name")
    caen_parser.add_argument(
        "value",
        nargs="?",
        default=None,
        help="Value to set command to, if applicable",
    )

    args = parser.parse_args()
    logging.basicConfig(level=args.log.upper())
    if args.ports:
        ports = [port.device for port in list_ports.comports()]
        print(f"Number of ports available: {len(ports)}")
        for port in ports:
            print(f"  - {port}")
        exit(0)

    # validate commands
    command = None
    value = None
    monitor_mode = False

    if args.brand == "iseg" and args.module is not None:
        print(
            f"WARNING: ISEG power supplies just have one module, ignoring --module {args.module}"
        )

    if args.brand != "iseg" and args.brand != "caen":
        raise Exception(f"Brand '{args.brand}' not supported")

    command = str(args.command[0]).upper()
    value = args.value
    channel = args.channel
    monitor_mode = None
    if channel is None:
        # command is at module level
        if args.brand == "caen":
            monitor_mode = _is_monitor_mode(
                command, _mon_module_commands.keys(), _set_module_commands.keys()
            )
        elif args.brand == "iseg":
            monitor_mode = _is_monitor_mode(
                command,
                _mon_module_methods_to_commands.keys(),
                _set_module_methods_to_commands.keys(),
            )
        else:  # should never happen
            raise Exception(f"Brand '{args.brand}' not supported")
    else:
        # command is at channel level
        if args.brand == "caen":
            monitor_mode = _is_monitor_mode(
                command, _mon_channel_commands.keys(), _set_channel_commands.keys()
            )
        elif args.brand == "iseg":
            monitor_mode = _is_monitor_mode(
                command,
                _mon_channel_methods_to_commands.keys(),
                _set_channel_methods_to_commands.keys(),
            )
        else:  # should never happen
            raise Exception(f"Brand '{args.brand}' not supported")

        if monitor_mode and value is not None:
            raise Exception(f"Channel command {command} does not accept a value")

        if not monitor_mode:
            # set mode
            if command in ["ON", "OFF"]:
                if value is not None:
                    raise Exception(
                        f"Channel command {command} does not accept a value"
                    )
            else:
                if value is None:
                    raise Exception(f"Channel command {command} requires a value")

        if args.test:
            print("Testing mode enabled, commands will not be run")
            return

        if args.brand == "caen":
            caen = Caen(port=args.port, baudrate=args.baud)
            module = caen.module(args.module)
            channel = module.channel(args.channel) if args.channel is not None else None
            if monitor_mode:
                # monitor command
                if not channel:
                    # module level
                    result = getattr(module, command)
                else:
                    # channel level
                    result = getattr(channel, command)

                print(f"{command}: {result}")

            else:
                # set command
                if not channel:
                    # module level
                    setattr(module, command, value)
                else:
                    # channel level
                    if command in ["ON", "OFF"]:
                        if command == "ON":
                            channel.turn_on()
                            print(f"Channel {channel} turned on")
                        else:
                            channel.turn_off()
                            print(f"Channel {channel} turned off")
                    else:
                        setattr(channel, command, value)
                        print(f"{command} set to {value}")


if __name__ == "__main__":
    main()
