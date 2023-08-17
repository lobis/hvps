from __future__ import annotations

import serial
from serial.tools import list_ports
from typing import Dict
import logging
import uuid
import threading

from .module import Module


class Hvps:
    def __init__(
        self,
        baudrate: int = 115200,
        port: str | None = None,
        timeout: float | None = None,
        logging_level=logging.WARNING,
    ):
        """Initialize the HVPS (High-Voltage Power Supply) object.

        Args:
            baudrate (int, optional): The baud rate for serial communication. Defaults to 115200.
            port (str | None, optional): The serial port to use. If None, it will try to detect one automatically. Defaults to None.
            timeout (float | None, optional): The timeout for serial communication. Defaults to None.
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

        if port is None:
            self._logger.info("No port specified, trying to detect one")
            ports = [port.device for port in list_ports.comports()]
            if len(ports) >= 1:
                port = ports[0]
                if len(ports) > 1:
                    self._logger.warning(
                        f"Multiple ports detected: {ports}, using the first one: {port}"
                    )

        self._serial: serial.Serial = serial.Serial()

        self._serial.port = port
        self._serial.baudrate = baudrate
        if timeout is not None:
            self._serial.timeout = timeout

    def __del__(self):
        """Cleanup method to close the serial port when the HVPS object is deleted."""
        self.close()

    def connect(self):
        """
        Open the serial port.
        """

        self._logger.debug("Connecting to serial port")
        self._logger.info(f"Using port {self._serial.port}")
        self._logger.info(f"Using baud rate {self._serial.baudrate}")
        self._logger.debug(f"Using timeout {self._serial.timeout}")

        if not hasattr(self, "_serial"):
            return
        if self.port is None:
            raise ValueError("No port specified")
        if not self._serial.is_open:
            self._serial.open()
        else:
            self._logger.warning("Serial port is already open")

    def open(self):
        """
        Open the serial port. (Alias for connect).
        """

        self.connect()

    def disconnect(self):
        """
        Close the serial port.
        """

        self._logger.debug("Disconnecting from serial port")

        if not hasattr(self, "_serial"):
            return
        if self._serial.is_open:
            self._serial.close()
        else:
            self._logger.warning("Serial port is already closed")

    def close(self):
        """
        Close the serial port. (Alias for disconnect).
        """
        self.disconnect()

    def __enter__(self) -> Hvps:
        """
        Context manager enter method.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Context manager exit method.
        """
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

    @port.setter
    def port(self, port: str):
        """
        Set the serial port.

        Args:
            port (str): The serial port.
        """
        self._serial.port = port

    @property
    def baudrate(self) -> int:
        """
        Get the baud rate.

        Returns:
            int: The baud rate.
        """
        return self._serial.baudrate

    @baudrate.setter
    def baudrate(self, baudrate: int):
        """
        Set the baud rate.

        Args:
            baudrate (int): The baud rate.
        """
        self._serial.baudrate = baudrate

    @property
    def timeout(self) -> float:
        """
        Get the timeout.

        Returns:
            float: The timeout.
        """
        return self._serial.timeout

    @timeout.setter
    def timeout(self, timeout: float):
        """
        Set the timeout.

        Args:
            timeout (float): The timeout.
        """
        if timeout < 0:
            raise ValueError("Timeout must be positive")
        self._serial.timeout = timeout

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
