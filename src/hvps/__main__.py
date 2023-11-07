from __future__ import annotations
from typing import List, Dict

import serial
from serial.tools import list_ports
import argparse
import logging

from hvps import __version__ as hvps_version
from hvps import Caen, Iseg
from hvps.commands.caen.module import (
    _MON_MODULE_COMMANDS as CAEN_MON_MODULE_COMMANDS,
    _SET_MODULE_COMMANDS as CAEN_SET_MODULE_COMMANDS,
)
from hvps.commands.caen.channel import (
    _MON_CHANNEL_COMMANDS as CAEN_MON_CHANNEL_COMMANDS,
    _SET_CHANNEL_COMMANDS as CAEN_SET_CHANNEL_COMMANDS,
)
from hvps.commands.iseg.module import (
    _MON_MODULE_COMMANDS as ISEG_MON_MODULE_COMMANDS,
    _SET_MODULE_COMMANDS as ISEG_SET_MODULE_COMMANDS,
)
from hvps.commands.iseg.channel import (
    _MON_CHANNEL_COMMANDS as ISEG_MON_CHANNEL_COMMANDS,
    _SET_CHANNEL_COMMANDS as ISEG_SET_CHANNEL_COMMANDS,
)


# TODO: command help in cli
# TODO: name of parameter in function calls
# TODO: update docstrings
# TODO: abstract methods


def _is_setter_mode(
    command: str,
    value: str | None,
    monitor_commands: List[str],
    set_commands: List[str],
) -> bool:
    """
    Check if command is a setter command or a monitor command

    Args:
        command: command to check
        value: value to set command to, if applicable
        monitor_commands: list of monitor commands
        set_commands: list of set commands

    Returns: True if setter mode, False if monitor mode

    Throws:
        Exception if command is not a valid monitor or set command
    """
    setter_mode = value is not None  # if it gets a value must be a setter
    # but if not it can be a setter if is not between the monitor commands
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
    method: str,
    value: str | None,
    o: object,
    commands: Dict[str, Dict],
    dry_run: bool = False,
    logger: logging.Logger = None,
) -> None:
    """
    Call setter method of name command with value value on object o

    Args:
        method: command to call (must be a setter)
        value: value to set command to, if applicable
        o: object to call command on
        commands: dictionary of commands
        dry_run: if True, commands will not be run

    Throws:
        Exception if command is not a valid setter command

    Returns:
        None
    """

    command_input_type = commands[method]["input_type"]
    # True if sets a property, False if setter just sets non-readable state in the hvps
    sets_property = isinstance(getattr(type(o), method), property)

    try:
        if value is None and command_input_type is None:
            # setter with no input value
            getattr(o, method)()
        elif value is None and command_input_type is not None:
            # setter with no input value called with a value as input
            raise Exception(f"Command '{method}' doesn't accept a value")
        elif value is not None:
            # setter with input value
            value = command_input_type(value)
            if sets_property:
                setattr(o, method, value)
            else:
                getattr(o, method)(value)
    except (serial.SerialException, serial.serialutil.PortNotOpenError) as e:
        if dry_run:
            logger.info(f"setter {method} called")
        else:
            raise e

    result = f"{method} {value}: ok"
    logger.info(result)


def _call_monitor_method(
    method: str,
    o: object,
    dry_run: bool = False,
    logger: logging.Logger = None,
) -> None:
    """
    Call monitor method of name command on object o

    Args:
        method: method to call (must be a monitor method)
        o: object to call command on
        dry_run: if True, commands will not be run

    Throws:
        Exception if command is not a valid monitor command

    Returns:
        None
    """
    try:
        result = f"{method}: {getattr(o, method)}"
        logger.info(result)
    except (serial.SerialException, serial.serialutil.PortNotOpenError) as e:
        if dry_run:
            logger.info(f"monitor {method} called")
        else:
            raise e


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
        "--channel", default=None, type=int, help="HV PS channel"
    )  # Required argument
    parser.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Dry run mode. Do not run commands",
    )

    # Subparsers
    subparsers = parser.add_subparsers(dest="brand", help="Select brand (caen or iseg)")

    # CAEN
    caen_parser = subparsers.add_parser("caen", help="CAEN HVPS")
    caen_parser.add_argument("--module", default=0, type=int, help="Module number")
    caen_parser.add_argument("method", nargs=1, help="Command name")
    caen_parser.add_argument(
        "value",
        nargs="?",
        default=None,
        help="Value to set method to, if applicable",
    )

    # ISEG
    iseg_parser = subparsers.add_parser("iseg", help="iseg HVPS")
    iseg_parser.add_argument("method", nargs=1, help="Command name")
    iseg_parser.add_argument(
        "value",
        nargs="?",
        default=None,
        help="Value to set method to, if applicable",
    )

    # validate args
    args = parser.parse_args()
    logging.basicConfig(level=args.log.upper())
    dry_run = True if args.dry_run else False

    if args.ports:
        ports = [port.device for port in list_ports.comports()]
        print(f"Number of ports available: {len(ports)}")
        for port in ports:
            print(f"  - {port}")
        exit(0)

    # TODO: add validation for main call with --ports
    method = str(args.method[0]).lower() if args.method else None
    value = args.value
    channel = args.channel
    is_channel_mode = channel is not None  # True if channel is specified, False if not

    if args.brand == "caen":
        module = args.module
        caen = Caen(port=args.port, baudrate=args.baud)
        if not dry_run:
            caen.open()

        module = caen.module(module)

        if not is_channel_mode:
            # method is caen at module level
            setter_mode = _is_setter_mode(
                method,
                value,
                CAEN_MON_MODULE_COMMANDS.keys(),
                CAEN_SET_MODULE_COMMANDS.keys(),
            )

            if setter_mode:
                _call_setter_method(
                    method,
                    value,
                    module,
                    CAEN_SET_MODULE_COMMANDS,
                    dry_run,
                    caen._logger,
                )
            else:
                _call_monitor_method(method, module, dry_run, caen._logger)
        else:
            # method is caen at channel level
            channel = module.channel(args.channel)
            setter_mode = _is_setter_mode(
                method,
                value,
                CAEN_MON_CHANNEL_COMMANDS.keys(),
                CAEN_SET_CHANNEL_COMMANDS.keys(),
            )

            if setter_mode:
                _call_setter_method(
                    method,
                    value,
                    channel,
                    CAEN_SET_CHANNEL_COMMANDS,
                    dry_run,
                    caen._logger,
                )
            else:
                _call_monitor_method(method, channel, dry_run, caen._logger)

        caen.close()

    elif args.brand == "iseg":
        iseg = Iseg(port=args.port, baudrate=args.baud)
        if not dry_run:
            iseg.open()
        module = iseg.module()

        if not is_channel_mode:
            # method is iseg at module level
            setter_mode = _is_setter_mode(
                method,
                value,
                ISEG_MON_MODULE_COMMANDS.keys(),
                ISEG_SET_MODULE_COMMANDS.keys(),
            )
            if setter_mode:
                _call_setter_method(
                    method,
                    value,
                    module,
                    ISEG_SET_MODULE_COMMANDS,
                    dry_run,
                    iseg._logger,
                )
            else:
                _call_monitor_method(method, module, dry_run, iseg._logger)
        else:
            # method is iseg at channel level
            channel = module.channel(args.channel)
            setter_mode = _is_setter_mode(
                method,
                value,
                ISEG_MON_CHANNEL_COMMANDS.keys(),
                ISEG_SET_CHANNEL_COMMANDS.keys(),
            )
            if setter_mode:
                _call_setter_method(
                    method,
                    value,
                    channel,
                    ISEG_SET_CHANNEL_COMMANDS,
                    dry_run,
                    iseg._logger,
                )
            else:
                _call_monitor_method(method, channel, dry_run, iseg._logger)
        iseg.close()
    else:
        raise ValueError(f"Brand {args.brand} not supported")


if __name__ == "__main__":
    main()
