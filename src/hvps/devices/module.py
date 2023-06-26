from typing import List

import serial
from abc import ABC, abstractmethod

from .channel import Channel


class Module(ABC):
    def __init__(self, _serial: serial.Serial, module: int):
        """Initialize the Module object.

        Args:
            _serial (serial.Serial): The serial object used for communication.
            module (int): The module number.

        """
        self._serial = _serial
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
    def channels(self) -> List[Channel]:
        """The list of channels in the module.

        Returns:
            List[Channel]: The list of channels.

        """
        return self._channels

    def channel(self, channel: int) -> Channel:
        """Get the specified channel in the module.

        Args:
            channel (int): The channel number.

        Returns:
            Channel: The Channel object.

        Raises:
            KeyError: If the channel number is invalid.

        """
        if channel not in range(self.number_of_channels):
            raise KeyError(
                f"Invalid channel {channel}. Valid channels are 0..{self.number_of_channels - 1}"
            )
        return self.channels[channel]
