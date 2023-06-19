from __future__ import annotations

import serial
from serial.tools import list_ports
from typing import Dict
import time
import logging

from .module import Module


def detect_baudrate(port: str) -> int:
    """
    Detect the baud rate for a given serial port.

    Args:
        port (str): The serial port to detect the baud rate for.

    Returns:
        int: The detected baud rate.

    Raises:
        Exception: If the baud rate cannot be detected.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Detecting baud rate for port {port}")

    baudrate_detection_message = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    # Try different baud rates until one works
    for baudrate in [9600, 19200, 38400, 57600, 115200]:
        logger.debug(f"Trying baud rate {baudrate}")
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

            logger.info(f"Baud rate detected: {baudrate}")
            return baudrate

    raise Exception("Could not detect baud rate")


class HVPS:
    def __init__(
        self,
        baudrate: int | None = None,
        port: str | None = None,
        timeout: float | None = None,
        connect: bool = True,
        verbosity: int = logging.WARNING,
    ):
        """
        Initialize the CaenHV object.

        Args:
            baudrate (int | None): The baud rate for the serial communication. If None, it will be detected automatically.
            port (str | None): The serial port to use. If None, it will try to detect an available port.
            timeout (float | None): The serial communication timeout in seconds. If None, the default timeout will be used.
            connect (bool): Whether to automatically open the serial port on initialization.
            verbosity (int): The logging verbosity level.

        Raises:
            Exception: If no available ports are found.
        """
        # Set global logging level
        logging.basicConfig(level=verbosity)
        logger = logging.getLogger(__name__)

        self._modules: Dict[int, Module] = {}

        if port is None:
            logger.info("No port specified, trying to detect one")
            ports = [port.device for port in list_ports.comports()]
            if len(ports) == 0:
                raise Exception("No ports available")
            port = ports[0]

        self._serial: serial.Serial = serial.Serial()
        self._serial.port = port
        logger.debug(f"Using port {port}")
        self._serial.baudrate = baudrate or detect_baudrate(port)
        logger.debug(f"Using baud rate {self._serial.baudrate}")
        self._serial.timeout = timeout
        logger.debug(f"Using timeout {self._serial.timeout}")

        if connect:
            logger.debug("Opening serial port")
            self._serial.open()
            logger.debug("Serial port opened")

        # TODO: automatic module detection (connect to all in range 0..31) and baud rate detection (by getting module name)

    def write(self, data: bytes):
        """
        Write data to the serial port.

        Args:
            data (bytes): The data to write.
        """
        logger = logging.getLogger(__name__)
        logger.debug(f"Serial write: {data}")
        self._serial.write(data)

    def __del__(self):
        if hasattr(self, "_serial"):
            self._serial.close()

    def disconnect(self):
        """
        Disconnect from the serial port.
        """
        if not hasattr(self, "_serial"):
            return
        if self._serial.is_open:
            self._serial.close()

    def __getitem__(self, bd: int) -> Module:
        """
        Get a Module object corresponding to the specified board number.

        Args:
            bd (int): The board number.

        Returns:
            Module: The Module object.
        """
        return self.module(bd)

    def __len__(self):
        """
        Get the number of modules.

        Returns:
            int: The number of modules.
        """
        return len(self._modules)

    def __iter__(self):
        """
        Iterate over the modules.

        Yields:
            Module: The next Module object.
        """
        for device in self._modules.values():
            yield device

    def __next__(self):
        """
        Get the next module.

        Returns:
            Module: The next Module object.
        """
        return next(self._modules.values())

    @property
    def is_open(self) -> bool:
        """
        Check if the serial port is open.

        Returns:
            bool: True if the serial port is open, False otherwise.
        """
        return self._serial.is_open

    @property
    def connected(self) -> bool:
        """
        Check if connected to the serial port.

        Returns:
            bool: True if connected, False otherwise.
        """
        return self.is_open

    @property
    def serial(self):
        """
        Get the underlying serial.Serial object.

        Returns:
            serial.Serial: The serial.Serial object.
        """
        return self._serial

    @property
    def modules(self):
        """
        Get the dictionary of modules.

        Returns:
            Dict[int, Module]: The dictionary of modules.
        """
        return self._modules

    def connect(self):
        """
        Connect to the serial port.
        """
        self._serial.open()

    def module(self, bd: int = 0) -> Module:
        """
        Get a Module object corresponding to the specified board number.

        Args:
            bd (int): The board number.

        Returns:
            Module: The Module object.
        """
        _module = Module(self._serial, bd)
        if bd not in self._modules:
            self._modules[bd] = _module
        return self._modules[bd]
