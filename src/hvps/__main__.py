from __future__ import annotations
from typing import List, Dict

from hvps import __version__ as hvps_version, Caen, Iseg
from hvps.commands.caen.module import (
    _SET_MODULE_COMMANDS as CAEN_SET_MODULE_COMMANDS,
)
from hvps.commands.caen.channel import (
    _SET_CHANNEL_COMMANDS as CAEN_SET_CHANNEL_COMMANDS,
)
from hvps.commands.iseg.module import (
    _SET_MODULE_COMMANDS as ISEG_SET_MODULE_COMMANDS,
)
from hvps.commands.iseg.channel import (
    _SET_CHANNEL_COMMANDS as ISEG_SET_CHANNEL_COMMANDS,
)
from hvps.devices.iseg.module import (
    _mon_module_methods_to_commands as iseg_mon_module_methods,
)
from hvps.devices.iseg.module import (
    _set_module_methods_to_commands as iseg_set_module_methods,
)
from hvps.devices.iseg.channel import (
    _mon_channel_methods_to_commands as iseg_mon_channel_methods,
)
from hvps.devices.iseg.channel import (
    _set_channel_methods_to_commands as iseg_set_channel_methods,
)
from hvps.devices.caen.module import (
    _mon_module_methods_to_commands as caen_mon_module_methods,
)
from hvps.devices.caen.module import (
    _set_module_methods_to_commands as caen_set_module_methods,
)
from hvps.devices.caen.channel import (
    _mon_channel_methods_to_commands as caen_mon_channel_methods,
)
from hvps.devices.caen.channel import (
    _set_channel_methods_to_commands as caen_set_channel_methods,
)

from serial.tools import list_ports

import argparse
import logging


def _is_setter_mode(
    command: str,
    value: str | None,
    monitor_commands: List[str],
    set_commands: List[str],
) -> bool:
    setter_mode = value is not None
    if value is None and command not in monitor_commands:
        if command in set_commands:
            return True
        else:
            raise Exception(
                f"Channel command '{command}' not a valid monitor command: {monitor_commands} or set "
                f"command: {set_commands}"
            )
    return setter_mode


def _call_setter_method(
    command: str,
    value: str | None,
    o: object,
    methods_to_commands: Dict[str, str],
    commands: Dict[str, Dict],
    testing: bool = False,
):
    if command not in methods_to_commands:
        raise Exception(
            f"Channel command '{command}' not a valid setter command: {caen_set_channel_methods}"
        )
    if testing:
        print("Testing mode enabled, commands will not be run")
        return

    command_input_type = commands[methods_to_commands[command]]["input_type"]
    # True if sets a property, False if setter just sets non-readable state in the hvps
    sets_property = isinstance(getattr(o, command), property)

    if value is None and command_input_type is None:
        # setter with no input value
        getattr(o, command)()
    elif value is None and command_input_type is not None:
        # setter with no input value called with a value as input
        raise Exception(f"Command '{command}' doesn't accept a value")
    elif value is not None:
        # setter with input value
        if sets_property:
            setattr(o, command, value)
        else:
            getattr(o, command)(value)
    print(f"setter {command} called with value: {value}")


def _call_monitor_method(
    command: str, o: object, methods_to_commands: Dict[str, str], testing: bool = False
):
    if command not in methods_to_commands:
        raise Exception(
            f"Channel command '{command}' not a valid monitor command: {caen_mon_channel_methods}"
        )
    if testing:
        print("Testing mode enabled, commands will not be run")
        return

    print(f"{command}: {getattr(o, command)}")


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
    parser.add_argument("--module", type=int, default=0, help="Module number. CAEN")
    parser.add_argument(
        "--channel", default=None, help="HV PS channel"
    )  # Required argument
    parser.add_argument(
        "--test", action="store_true", help="Testing mode. Do not run commands"
    )

    # Subparsers
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
    iseg_parser = subparsers.add_parser("iseg", help="iseg HVPS")
    iseg_parser.add_argument("command", nargs=1, help="command name")
    iseg_parser.add_argument(
        "value",
        nargs="?",
        default=None,
        help="Value to set command to, if applicable",
    )

    # validate args
    args = parser.parse_args()
    logging.basicConfig(level=args.log.upper())
    if args.ports:
        ports = [port.device for port in list_ports.comports()]
        print(f"Number of ports available: {len(ports)}")
        for port in ports:
            print(f"  - {port}")
        exit(0)

    if args.brand == "iseg" and args.module is not None:
        print(
            f"WARNING: ISEG power supplies just have one module, ignoring --module {args.module}"
        )

    if args.brand != "iseg" and args.brand != "caen":
        raise Exception(f"Brand '{args.brand}' not supported")

    testing = False
    if args.test:
        testing = True
    command = str(args.command[0]).lower()
    value = args.value
    channel = args.channel
    setter_mode = None  # True if command is a setter command, False if monitor command
    is_caen = args.brand == "caen"  # True if caen, False if iseg
    is_channel_mode = channel is not None  # True if channel is specified, False if not

    if is_caen:
        if testing:
            caen = None
        else:
            caen = Caen(port=args.port, baudrate=args.baud)
        if testing:
            module = None
        else:
            module = caen.module(args.module)
        if not is_channel_mode:
            # command is caen at module level
            setter_mode = _is_setter_mode(
                command,
                value,
                caen_mon_module_methods.keys(),
                caen_set_module_methods.keys(),
            )

            if setter_mode:
                _call_setter_method(
                    command,
                    value,
                    caen,
                    caen_set_module_methods,
                    CAEN_SET_MODULE_COMMANDS,
                    testing,
                )
            else:
                _call_monitor_method(command, caen, caen_mon_module_methods, testing)
        else:
            # command is caen at channel level
            if testing:
                channel = None
            else:
                channel = module.channel(args.channel)
            setter_mode = _is_setter_mode(
                command,
                value,
                caen_mon_channel_methods.keys(),
                caen_set_channel_methods.keys(),
            )

            if setter_mode:
                _call_setter_method(
                    command,
                    value,
                    channel,
                    caen_set_channel_methods,
                    CAEN_SET_CHANNEL_COMMANDS,
                    testing,
                )
            else:
                _call_monitor_method(
                    command, channel, caen_mon_channel_methods, testing
                )

    elif not is_caen:
        if testing:
            iseg = None
        else:
            iseg = Iseg(port=args.port, baudrate=args.baud)
        if testing:
            module = None
        else:
            module = iseg.module(0)
        if not is_channel_mode:
            # command is iseg at module level
            setter_mode = _is_setter_mode(
                command,
                value,
                iseg_mon_module_methods.keys(),
                iseg_set_module_methods.keys(),
            )
            if setter_mode:
                _call_setter_method(
                    command,
                    value,
                    module,
                    iseg_set_module_methods,
                    ISEG_SET_MODULE_COMMANDS,
                    testing,
                )
            else:
                _call_monitor_method(command, module, iseg_mon_module_methods, testing)
        else:
            # command is iseg at channel level
            if testing:
                channel = None
            else:
                channel = module.channel(args.channel)
            setter_mode = _is_setter_mode(
                command,
                value,
                iseg_mon_channel_methods.keys(),
                iseg_set_channel_methods.keys(),
            )
            if setter_mode:
                _call_setter_method(
                    command,
                    value,
                    channel,
                    iseg_set_channel_methods,
                    ISEG_SET_CHANNEL_COMMANDS,
                    testing,
                )
            else:
                _call_monitor_method(
                    command, channel, iseg_mon_channel_methods, testing
                )


if __name__ == "__main__":
    main()
