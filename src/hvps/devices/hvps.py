from __future__ import annotations

import serial
from serial.tools import list_ports
from typing import Dict
import logging
import uuid
import threading
from contextlib import contextmanager

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
        """Initialize the HVPS (High-Voltage Power Supply) object.

        Args:
            baudrate (int, optional): The baud rate for serial communication. Defaults to 115200.
            port (str | None, optional): The serial port to use. If None, it will try to detect one automatically. Defaults to None.
            timeout (float | None, optional): The timeout for serial communication. Defaults to None.
            connect (bool, optional): Whether to connect to the serial port during initialization. Defaults to True.
            logging_level (int, optional): The logger level. Defaults to logger.WARNING.

        """

        # Create a lock for the serial port
        self._lock = threading.Lock()

        self._logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}.{uuid.uuid4()}"
        )
        self._logger.setLevel(logging_level)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self._logger.addHandler(stream_handler)

        self._modules: Dict[int, Module] = {}

        if port is None and connect:
            self._logger.info("No port specified, trying to detect one")
            ports = [port.device for port in list_ports.comports()]
            if len(ports) == 0:
                raise Exception("No ports available")
            port = ports[0]

        self._serial: serial.Serial = serial.Serial()
        self._serial.port = port
        self._logger.info(f"Using port {port}")
        self._serial.baudrate = baudrate
        self._logger.info(f"Using baud rate {self._serial.baudrate}")
        self._serial.timeout = timeout
        self._logger.debug(f"Using timeout {self._serial.timeout}")

        if connect:
            self._logger.debug("Opening serial port")
            self._serial.open()
            self._logger.debug("Serial port opened")

    def __del__(self):
        """Cleanup method to close the serial port when the HVPS object is deleted."""
        self.close()

    def connect(self):
        """
        Open the serial port.
        """
        if not hasattr(self, "_serial"):
            return
        if not self._serial.is_open:
            self._serial.open()

    def disconnect(self):
        """
        Close the serial port.
        """
        if not hasattr(self, "_serial"):
            return
        if self._serial.is_open:
            self._serial.close()

    def close(self):
        """
        Close the serial port.
        """
        self.disconnect()

    @contextmanager
    def open(self):
        """
        A context manager to automatically open and close the serial port.
        """

        self.connect()
        yield
        self.disconnect()

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
    def logger(self) -> logging.Logger:
        """
        Get the logger.

        Returns:
            logging.Logger: The logger.
        """
        return self._logger

    def set_logging_level(self, level: int):
        """
        Set the logging level.

        Args:
            level (int): The logging level.
        """
        self._logger.setLevel(level)

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
        """Get the specified module.

        Args:
            module (int, optional): The module number. Defaults to 0.

        Returns:
            Module: The Module object.

        Raises:
            KeyError: If the module number is invalid.
        """
        if module not in self._modules:
            raise KeyError(f"Invalid module {module}")
        return self._modules[module]
