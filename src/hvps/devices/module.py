from functools import cached_property
from typing import List

import serial

from ..commands.caen.module import _get_mon_module_command, _get_set_module_command
from ..commands.caen import _parse_response
from ..utils.utils import string_to_bit_array
from .channel import Channel


class Module:
    """Represents a module of a device.

    Args:
        _serial (serial.Serial): The serial connection to the device.
        bd (int): The bd value.
    """

    def __init__(self, _serial: serial.Serial, bd: int):
        self._serial = _serial
        self._bd = bd
        self._channels: List[Channel] = []

    @property
    def bd(self) -> int:
        """The bd value of the module.

        Returns:
            int: The bd value.
        """
        return self._bd

    @cached_property
    def name(self) -> str:
        """The name of the module.

        Returns:
            str: The name of the module.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDNAME"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        return str(response)

    @cached_property
    def number_of_channels(self) -> int:
        """The number of channels in the module.

        Returns:
            int: The number of channels.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDNCH"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        return int(response)

    @property
    def get_firmware_release(self) -> str:
        """
           Read out Firmware Release (XX.X)

           Returns:
               str: The firmware release.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDFREL"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        return response

    @property
    def get_serial_number(self) -> str:
        """
            Read out value serial number (XXXXX)

            Returns:
                str: The serial number.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDSNUM"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        return int(response)

    @property
    def get_interlock_status(self) -> str:
        """
            Read out INTERLOCK status (YES/NO)

            Returns:
                str: The interlock status.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDILK"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        return response

    @property
    def get_interlock_mode(self) -> str:
        """
            Read out INTERLOCK mode (OPEN/CLOSED)

            Returns:
                str: The interlock mode.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDILKM"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        return response

    @property
    def get_control_mode(self) -> str:
        """
            Read out Control Mode (LOCAL / REMOTE)

            Returns:
                str: The control mode.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDCTR"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        return response

    @property
    def get_local_bus_termination_status(self) -> str:
        """
            Read out LOCAL BUS Termination status (ON/OFF)

            Returns:
                str: The local bus termination status.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDTERM"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        return response

    @property
    def get_board_alarm_status(self) -> str:
        """
            Read out Board Alarm status value (XXXXX)

            Returns:
                str: The board alarm status value.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDALARM"))
        response = _parse_response(self._serial.readline(), bd=self.bd)

        bit_array = string_to_bit_array(response)

        mapping = {
            "CH0": bool(bit_array[0]),  # True: Ch0 in Alarm status
            "CH1": bool(bit_array[1]),  # True: Ch1 in Alarm status
            "CH2": bool(bit_array[2]),  # True: Ch2 in Alarm status
            "CH3": bool(bit_array[3]),  # True: Ch3 in Alarm status
            "PWFAIL": bool(bit_array[4]),  # True: Board in POWER FAIL
            "OVP": bool(bit_array[5]),  # True: Board in OVER POWER
            "HVCKFAIL": bool(bit_array[6])  # True: Internal HV Clock FAIL (≠ 200±10kHz)
        }

        return mapping

    @property
    def set_interlock_mode(self, mode: str) -> None:
        """
            VAL:OPEN/CLOSED Set Interlock Mode

            Args:
                mode (str): The interlock mode to set.
        """
        self._serial.write(_get_set_module_command(self._bd, "BDILKM", mode))

    @property
    def clear_alarm_signal(self) -> None:
        """
            Clear alarm signal
        """
        self._serial.write(_get_set_module_command(self._bd, "BDCLR", None))

    @property
    def channels(self):
        """The channels in the module.

        Returns:
            List[Channel]: A list of Channel objects.
        """
        if len(self._channels) == 0:
            for channel in range(self.number_of_channels):
                self._channels.append(Channel(self._serial, self.bd, channel))
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
