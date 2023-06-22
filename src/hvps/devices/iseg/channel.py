import serial

from ...commands.iseg.channel import (
    _get_set_channel_command,
    _get_mon_channel_command,
)
from ...commands.iseg import _parse_response

from time import sleep


class Channel:
    """Represents a channel of a device.

    Args:
        _serial (serial.Serial): The serial connection to the device.
        bd (int): The bd value.
        channel (int): The channel number.
    """

    def __init__(self, _serial: serial.Serial, channel: int):
        self._serial = _serial
        self._channel = channel
