import sys
import pytest

from hvps import Caen
from hvps.utils import get_serial_ports

import logging

# find a way to only run these tests if a serial port connection exists

serial_port = "COM4"  # change this to the serial port you are using
serial_baud = 115200
timeout = 5.0


def serial_port_available():
    ports = get_serial_ports()
    return ports != []


def is_macos():
    return sys.platform == "Darwin"


serial_skip_decorator = pytest.mark.skipif(
    serial_port_available() or not is_macos(), reason="No serial ports available"
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


@serial_skip_decorator
def test_caen_channel_serial():
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

        vmon = channel.vmon
        print(f"vmon: {vmon}")

        vset = channel.vset
        print(f"vset: {vset}")

        vmin = channel.vmin
        print(f"vmin: {vmin}")

        vmax = channel.vmax
        print(f"vmax: {vmax}")

        vdec = channel.vdec
        print(f"vdec: {vdec}")

        iset = channel.iset
        print(f"iset: {iset}")

        imin = channel.imin
        print(f"imin: {imin}")

        imax = channel.imax
        print(f"imax: {imax}")

        isdec = channel.isdec
        print(f"isdec: {isdec}")

        imon = channel.imon
        print(f"imon: {imon}")

        imrange = channel.imrange
        print(f"imrange: {imrange}")

        imdec = channel.imdec
        print(f"imdec: {imdec}")

        maxv = channel.maxv
        print(f"maxv: {maxv}")

        mvmin = channel.mvmin
        print(f"mvmin: {mvmin}")

        mvmax = channel.mvmax
        print(f"mvmax: {mvmax}")

        mvdec = channel.mvdec
        print(f"mvdec: {mvdec}")

        rup = channel.rup
        print(f"rup: {rup}")

        rupmin = channel.rupmin
        print(f"rupmin: {rupmin}")

        rupmax = channel.rupmax
        print(f"rupmax: {rupmax}")

        rupdec = channel.rupdec
        print(f"rupdec: {rupdec}")

        rdw = channel.rdw
        print(f"rdw: {rdw}")

        rdwmin = channel.rdwmin
        print(f"rdwmin: {rdwmin}")

        rdwmax = channel.rdwmax
        print(f"rdwmax: {rdwmax}")

        rdwdec = channel.rdwdec
        print(f"rdwdec: {rdwdec}")

        trip = channel.trip
        print(f"trip: {trip}")

        tripmin = channel.tripmin
        print(f"tripmin: {tripmin}")

        tripmax = channel.tripmax
        print(f"tripmax: {tripmax}")

        tripdec = channel.tripdec
        print(f"tripdec: {tripdec}")

        pdwn = channel.pdwn
        print(f"pdwn: {pdwn}")

        pol = channel.pol
        print(f"pol: {pol}")

        stat = channel.stat
        print(f"stat: {stat}")
