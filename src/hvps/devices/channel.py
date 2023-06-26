import serial
from abc import ABC, abstractmethod


class Channel(ABC):
    def __init__(self, _serial: serial.Serial, channel: int):
        """Initialize the Channel object.

        Args:
            _serial (serial.Serial): The serial object used for communication.
            channel (int): The channel number.

        """
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
        """The set voltage of the channel.

        This property should be implemented by subclasses to provide the set voltage of the channel.

        Returns:
            float: The set voltage.

        Raises:
            NotImplementedError: If the subclass does not implement this property.

        """
        pass
