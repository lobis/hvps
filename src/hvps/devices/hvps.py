from __future__ import annotations

import serial
from serial.tools import list_ports
from typing import Dict
import logging

from .module import Module


class Hvps:
    def __init__(
        self,
        baudrate: int = 115200,
        port: str | None = None,
        timeout: float | None = None,
        connect: bool = True,
        logging_level=logging.WARNING,
    ):
        # Set global logging level
        # TODO: rethink logging
        logging.basicConfig(level=logging_level)
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

    def connect(self):
        """
        Connect to the serial port.
        """
        self._serial.open()

    # modules

    @property
    def modules(self):
        """
        Get the dictionary of modules.

        Returns:
            Dict[int, Module]: The dictionary of modules.
        """
        return self._modules

    def module(self, module: int = 0) -> Module:
        if module not in self._modules:
            raise KeyError(f"Invalid module {module}")
        return self._modules[module]
