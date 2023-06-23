import pytest

from hvps import CAEN

import logging
import sys
import time

# find a way to only run these tests if a serial port connection exists

serial_port = "COM3"
serial_baud = 115200
timeout = 5.0


def test_caen_module_monitor():
    # no ports available
    caen = CAEN(port=serial_port, baudrate=serial_baud, connect=True, timeout=timeout, verbosity=logging.DEBUG)
    print(
        f"Serial port status: connected: {caen.connected}, port: {caen.port}, baudrate: {caen.baudrate}, timeout: {caen.timeout}")
    module = caen.module(0)

    control_mode = module.control_mode
    print(f"Control mode: {control_mode}")

    interlock_mode = module.interlock_mode
    print(f"Interlock mode: {interlock_mode}")

    name = module.name
    print(f"Name: {name}")

    bd = module.bd
    print(f"BD value: {bd}")

    number_of_channels = module.number_of_channels
    print(f"Number of channels: {number_of_channels}")

    firmware_release = module.firmware_release
    print(f"Firmware release: {firmware_release}")

    serial_number = module.serial_number
    print(f"Serial number: {serial_number}")

    interlock_status = module.interlock_status
    print(f"Interlock status: {interlock_status}")

    interlock_open = module.interlock_open
    print(f"Interlock open: {interlock_open}")

    control_mode_local = module.control_mode_local
    print(f"Control mode local: {control_mode_local}")

    control_mode_remote = module.control_mode_remote
    print(f"Control mode remote: {control_mode_remote}")

    local_bus_termination_status = module.local_bus_termination_status
    print(f"Local bus termination status: {local_bus_termination_status}")

    local_bus_termination_status_on = module.local_bus_termination_status_on
    print(f"Local bus termination status on: {local_bus_termination_status_on}")

    local_bus_termination_status_off = module.local_bus_termination_status_off
    print(f"Local bus termination status off: {local_bus_termination_status_off}")

    board_alarm_status = module.board_alarm_status
    print(f"Board alarm status: {board_alarm_status}")

    channels = module.channels
    print(f"Channels: {channels}")
