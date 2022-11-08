from functools import cached_property
from typing import List

import serial

from ..commands.module import _get_mon_module_command, _get_set_module_command
from ..commands import _parse_response
from .channel import Channel


class Module:
    def __init__(self, _serial: serial.Serial, bd: int):
        self._serial = _serial
        self._bd = bd
        self._channels: List[Channel] = []

    @property
    def bd(self) -> int:
        return self._bd

    @cached_property
    def name(self) -> str:
        self._serial.write(_get_mon_module_command(self._bd, "BDNAME"))
        code, response = _parse_response(self._serial.readline(), bd=self.bd)
        # TODO: handle error code
        return str(response)

    @cached_property
    def number_of_channels(self) -> int:
        self._serial.write(_get_mon_module_command(self._bd, "BDNCH"))
        code, response = _parse_response(self._serial.readline(), bd=self.bd)
        # TODO: handle error code
        return int(response)

    @property
    def channels(self):
        if len(self._channels) == 0:
            for channel in range(self.number_of_channels):
                self._channels.append(Channel(self._serial, self.bd, channel))
        return self._channels

    def channel(self, channel: int) -> Channel:
        if channel not in range(self.number_of_channels):
            raise KeyError(
                f"Invalid channel {channel}. Valid channels are 0..{self.number_of_channels - 1}"
            )
        return self.channels[channel]
