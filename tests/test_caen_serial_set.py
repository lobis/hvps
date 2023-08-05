import sys
import pytest

from hvps import Caen
from hvps.utils import get_serial_ports

import logging

# find a way to only run these tests if a serial port connection exists

serial_port = ""  # change this to the serial port you are using
serial_baud = 115200
timeout = 5.0


def serial_port_available():
    ports = get_serial_ports()
    return ports != []


def is_macos():
    return sys.platform == "Darwin"


serial_skip_decorator = pytest.mark.skipif(
    serial_port == "", reason="No serial ports set"
)


@serial_skip_decorator
def test_caen_module_monitor():
    # no ports available
    caen = Caen(
        port=serial_port,
        baudrate=serial_baud,
        connect=True,
        timeout=timeout,
        logging_level=logging.DEBUG,
    )
    print(
        f"Serial port status: connected: {caen.connected}, port: {caen.port}, baudrate: {caen.baudrate}, timeout: {caen.timeout}"
    )
    module = caen.module(0)

    prev_interlock_open = module.interlock_open
    module.open_interlock()
    module.close_interlock()
    module.open_interlock() if prev_interlock_open else module.close_interlock()
    module.clear_alarm_signal()


@serial_skip_decorator
def test_caen_channel_set():
    caen = Caen(
        port=serial_port,
        baudrate=serial_baud,
        connect=True,
        timeout=timeout,
        logging_level=logging.DEBUG,
    )
    print(
        f"Serial port status: connected: {caen.connected}, port: {caen.port}, baudrate: {caen.baudrate}, timeout: {caen.timeout}"
    )
    module = caen.module(0)

    for channel in module.channels:
        print("")
        print(f"Channel: {channel.channel}")

        prev_vset = channel.vset
        channel.vset = 20
        channel.vset = prev_vset

        prev_iset = channel.iset
        channel.iset = 5
        channel.iset = prev_iset

        prev_maxv = channel.maxv
        channel.maxv = 50
        channel.maxv = prev_maxv

        prev_rup = channel.rup
        channel.rup = 2
        channel.rup = prev_rup

        prev_rdw = channel.rdw
        channel.rdw = 3
        channel.rdw = prev_rdw

        prev_trip = channel.trip
        channel.trip = 5
        channel.trip = prev_trip

        prev_pdwn = channel.pdwn
        channel.pdwn = "RAMP"
        channel.pdwn = prev_pdwn

        prev_imrange = channel.imrange
        channel.imrange = "HIGH"
        channel.imrange = prev_imrange

        prev_on = channel.on
        channel.turn_on()
        channel.turn_off()
        channel.turn_on() if prev_on else channel.turn_off()
