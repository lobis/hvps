from functools import cached_property
from typing import List

import serial

from ...commands.iseg.module import _get_mon_module_command, _get_set_module_command
from ...commands.iseg import _write_command
from ...utils.utils import string_number_to_bit_array
from .channel import Channel


class Module:
    """Represents a module of a device.

    Args:
        _serial (serial.Serial): The serial connection to the device.
    """

    def __init__(self, _serial: serial.Serial):
        self._serial = _serial
        self._channels: List[Channel] = []

    @cached_property
    def number_of_channels(self) -> int:
        """The number of channels in the module.

        Returns:
            int: The number of channels.
        """
        command = _get_mon_module_command(":READ:MODULE:CHANNELNUMBER")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def firmware_release(self) -> str:
        """
        Read out Firmware Release (XX.X)

        Returns:
            str: The firmware release.
        """
        command = _get_mon_module_command(":READ:FIRMWARE:RELEASE")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return response[0]

    @property
    def module_status(self) -> dict:
        """
        Read out module status register

        Returns:
            str: The board alarm status value.
        """
        command = _get_mon_module_command(":READ:MODULE:STATUS")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")

        bit_array = string_number_to_bit_array(response[0])
        bit_array = list(reversed(bit_array))

        # TODO: review this
        return {
            "Is Voltage Ramp Speed Limited": bit_array[21],
            "Is Fast Ramp Down": bit_array[16],
            "Is Kill Enable": bit_array[15],
            "Is Temperature Good": bit_array[14],
            "Is Supply Good": bit_array[13],
            "Is Module Good": bit_array[12],
            "Is Event Active": bit_array[11],
            "Is Safety Loop Good": bit_array[10],
            "Is No Ramp": bit_array[9],
            "Is No Sum": bit_array[8],
            "Is Input Error": bit_array[6],
            "Is Service Is High": bit_array[4],
            "Voltage On": bit_array[3],
            "Is Fine Adjustment": bit_array[0]
        }

    @property
    def channels(self):
        """The channels in the module.

        Returns:
            List[Channel]: A list of Channel objects.
        """
        if len(self._channels) == 0:
            for channel in range(self.number_of_channels):
                self._channels.append(Channel(self._serial, channel))
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
