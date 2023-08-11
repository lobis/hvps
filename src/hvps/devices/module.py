from typing import List

import serial
import logging
import threading
from abc import ABC, abstractmethod

from .channel import Channel


class Module(ABC):
    def __init__(
        self,
        ser: serial.Serial,
        lock: threading.Lock,
        logger: logging.Logger,
        module: int,
    ):
        """Initialize the Module object.

        Args:
            ser (serial.Serial): The serial.Serial object.
            logger (logging.Logger): The logger.
            lock (threading.Lock): The lock.
            module (int): The module number.

        """
        self._serial = ser
        self._lock = lock
        self._logger = logger
        self._module = module
        self._channels: List[Channel] = []

    @property
    def module(self) -> int:
        """The module number.

        Returns:
            int: The module number.

        """
        return self._module

    @property
    @abstractmethod
    def number_of_channels(self) -> int:
        """The number of channels in the module.

        This property should be implemented by subclasses to provide the number of channels in the module.

        Returns:
            int: The number of channels.

        Raises:
            NotImplementedError: If the subclass does not implement this property.

        """
        pass

    @property
    @abstractmethod
    def channels(self) -> List[Channel]:
        """The channels in the module.

        This property should be implemented by subclasses to provide the channels in the module.

        Returns:
            List[Channel]: A list of Channel objects.

        Raises:
            NotImplementedError: If the subclass does not implement this property.

        """
        pass

    def channel(self, channel: int) -> Channel:
        """Get the specified channel in the module.

        Args:
            channel (int): The channel number.

        Returns:
            Channel: The Channel object.

        Raises:
            KeyError: If the channel number is invalid.

        """
        if channel not in range(len(self.channels)):
            raise KeyError(
                f"Invalid channel {channel}. Valid channels are 0..{self.number_of_channels - 1}"
            )
        return self.channels[channel]
