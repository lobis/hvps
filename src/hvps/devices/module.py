from typing import List

import serial

from .channel import Channel


class Module:
    def __init__(self, _serial: serial.Serial, module: int):
        self._serial = _serial
        self._module = module
        self._channels: List[Channel] = []

    @property
    def module(self) -> int:
        return self._module

    @property
    def number_of_channels(self) -> int:
        raise NotImplementedError("This method must be implemented by the subclass.")

    @property
    def channels(self) -> List[Channel]:
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
