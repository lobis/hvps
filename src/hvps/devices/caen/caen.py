from __future__ import annotations

import serial
from serial.tools import list_ports
from typing import Dict
import time
import logging

from .module import Module


class CAEN:
    def __init__(
        self,
        baudrate: int = 115200,
        port: str | None = None,
        timeout: float | None = None,
        connect: bool = True,
        verbosity: int = logging.WARNING,
    ):
        """
        Initialize the CaenHV object.

        Args:
            baudrate (int): The baud rate for the serial communication. Default: 115200.
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
        logger.info(f"Using port {port}")
        self._serial.baudrate = baudrate
        logger.info(f"Using baud rate {self._serial.baudrate}")
        self._serial.timeout = timeout
        logger.debug(f"Using timeout {self._serial.timeout}")

        if connect:
            logger.debug("Opening serial port")
            self._serial.open()
            logger.debug("Serial port opened")

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
    def connected(self) -> bool:
        """
        Check if connected to the serial port.

        Returns:
            bool: True if connected, False otherwise.
        """
        return self._serial.is_open

    @property
    def port(self) -> str:
        """
        Get the serial port.

        Returns:
            str: The serial port.
        """
        return self._serial.port

    @property
    def baudrate(self) -> int:
        """
        Get the baud rate.

        Returns:
            int: The baud rate.
        """
        return self._serial.baudrate

    @property
    def timeout(self) -> float:
        """
        Get the timeout.

        Returns:
            float: The timeout.
        """
        return self._serial.timeout

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
