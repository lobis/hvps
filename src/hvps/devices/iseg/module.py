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
        return {
            "Bit31": bool(bit_array[31]),  # Reserved
            "Bit30": bool(bit_array[30]),  # Reserved
            "Bit29": bool(bit_array[29]),  # Reserved
            "Bit28": bool(bit_array[28]),  # Reserved
            "Bit27": bool(bit_array[27]),  # Reserved
            "Bit26": bool(bit_array[26]),  # Reserved
            "Bit25": bool(bit_array[25]),  # Reserved
            "Bit24": bool(bit_array[24]),  # Reserved
            "Bit23": bool(bit_array[23]),  # Reserved
            "Bit22": bool(bit_array[22]),  # Reserved
            "Bit21": bool(bit_array[21]),  # Is Voltage Ramp Speed Limited
            "Bit20": bool(bit_array[20]),  # Reserved
            "Bit19": bool(bit_array[19]),  # Reserved
            "Bit18": bool(bit_array[18]),  # Reserved
            "Bit17": bool(bit_array[17]),  # Reserved
            "Bit16": bool(bit_array[16]),  # Is Fast Ramp Down
            "Bit15": bool(bit_array[15]),  # Is Kill Enable
            "Bit14": bool(bit_array[14]),  # Is Temperature Good
            "Bit13": bool(bit_array[13]),  # Is Supply Good
            "Bit12": bool(bit_array[12]),  # Is Module Good
            "Bit11": bool(bit_array[11]),  # Is Event Active
            "Bit10": bool(bit_array[10]),  # Is Safety Loop Good
            "Bit09": bool(bit_array[9]),  # Is No Ramp
            "Bit08": bool(bit_array[8]),  # Is No Sum
            "Bit07": bool(bit_array[7]),  # Reserved
            "Bit06": bool(bit_array[6]),  # Is Input Error
            "Bit05": bool(bit_array[5]),  # Reserved
            "Bit04": bool(bit_array[4]),  # Is Service Is High
            "Bit03": bool(bit_array[3]),  # Voltage On
            "Bit02": bool(bit_array[2]),  # Reserved
            "Bit01": bool(bit_array[1]),  # Reserved
            "Bit00": bool(bit_array[0]),  # Is Fine Adjustment
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
