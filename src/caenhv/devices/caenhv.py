from __future__ import annotations

import serial
from serial.tools import list_ports
from typing import Dict
import time
import logging

from .module import Module


def detect_baudrate(port: str) -> int:
    logger = logging.getLogger(__name__)
    logger.info(f"Detecting baudrate for port {port}")

    baudrate_detection_message = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    # Try different baud rates until one works
    for baudrate in [9600, 19200, 38400, 57600, 115200]:
        logger.debug(f"Trying baudrate {baudrate}")
        # Open the serial port with the current baud rate
        with serial.Serial(port, baudrate, timeout=1.0) as ser:

            # Send the baud rate detection message
            start_time = time.time()
            ser.write(baudrate_detection_message)
            ser.read(len(baudrate_detection_message))
            end_time = time.time()

            # Calculate the time it took for the device to respond
            elapsed_time = end_time - start_time

            # Calculate the baud rate based on the length of the message and the elapsed time
            expected_time = (len(baudrate_detection_message) + 2) / float(baudrate)
            expected_time *= 1.5  # Add a margin of error

            if abs(elapsed_time - expected_time) < 0.1:
                break

            logger.info(f"Baudrate detected: {baudrate}")
            return baudrate
    else:
        raise Exception("Unable to detect baudrate")


class CaenHV:
    def __init__(
            self, baudrate: int | None = None, port: str | None = None, timeout: float | None = None,
            connect: bool = True
    ):
        logger = logging.getLogger(__name__)
        self._modules: Dict[int, Module] = {}
        if port is None:
            logger.info("No port specified, trying to detect one")
            ports = [port.device for port in serial.tools.list_ports.comports()]
            if len(ports) == 0:
                raise Exception("No ports available")
            port = ports[0]

        self._serial: serial.Serial = serial.Serial()
        self._serial.port = port
        logger.debug(f"Using port {port}")
        self._serial.baudrate = baudrate or detect_baudrate(port)
        logger.debug(f"Using baudrate {self._serial.baudrate}")
        self._serial.timeout = timeout
        logger.debug(f"Using timeout {self._serial.timeout}")

        if connect:
            logger.debug("Opening serial port")
            self._serial.open()
            logger.debug("Serial port opened")

        # TODO: automatic module detection (connect to all in range 0..31) and baudrate detection (by getting module name)

    def write(self, data: bytes):
        logger = logging.getLogger(__name__)
        logger.debug(f"Serial write: {data}")
        self._serial.write(data)

    def __del__(self):
        if hasattr(self, "_serial"):
            self._serial.close()

    def disconnect(self):
        if not hasattr(self, "_serial"):
            return
        if self._serial.is_open:
            self._serial.close()

    def __getitem__(self, bd: int) -> Module:
        return self.module(bd)

    def __len__(self):
        return len(self._modules)

    def __iter__(self):
        for device in self._modules.values():
            yield device

    def __next__(self):
        return next(self._modules.values())

    @property
    def is_open(self) -> bool:
        return self._serial.is_open

    @property
    def connected(self) -> bool:
        return self.is_open

    @property
    def serial(self):
        return self._serial

    @property
    def modules(self):
        return self._modules

    def connect(self):
        self._serial.open()

    def module(self, bd: int = 0) -> Module:
        _module = Module(self._serial, bd)
        if bd not in self._modules:
            self._modules[bd] = _module
        return self._modules[bd]
