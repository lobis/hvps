import serial
from abc import ABC, abstractmethod


class Channel(ABC):
    def __init__(self, _serial: serial.Serial, channel: int):
        self._serial = _serial
        self._channel = channel

    @property
    def channel(self) -> int:
        """The channel number.

        Returns:
            int: The channel number.
        """
        return self._channel

    @property
    @abstractmethod
    def voltage_set(self) -> float:
        ...
