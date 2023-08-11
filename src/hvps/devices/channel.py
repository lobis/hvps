from abc import ABC, abstractmethod
import logging
from typing import Callable


class Channel(ABC):
    def __init__(
        self,
        write_command_read_response: Callable,
        logger: logging.Logger,
        channel: int,
    ):
        """Initialize the Channel object.

        Args:
            write_command_read_response (Callable): The function used to write a command and read the response.
            logger (logging.Logger): The logger object used for logging.
            channel (int): The channel number.

        """
        self._write_command_read_response = write_command_read_response
        self._logger = logger
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
