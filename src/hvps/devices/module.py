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
    def firmware_release(self) -> str:
        """
        Read out Firmware Release (XX.X)

        Returns:
            str: The firmware release.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDFREL"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        return response

    @property
    def serial_number(self) -> str:
        """
        Read out value serial number (XXXXX)

        Returns:
            str: The serial number.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDSNUM"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        # TODO: check if can be casted to int
        return response

    @property
    def interlock_status(self) -> bool:
        """
        Read out INTERLOCK status (YES/NO)

        Returns:
            bool: Yes: True, No: False
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDILK"))
        response = _parse_response(self._serial.readline(), bd=self.bd)

        if response == "YES":
            return True
        elif response == "NO":
            return False
        else:
            raise ValueError(f"Invalid response for 'interlock_status': {response}")

    @property
    def interlock_mode(self) -> str:
        """
        Read out INTERLOCK mode (OPEN/CLOSED)

        Returns:
            str: The interlock mode.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDILKM"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        if response not in ["OPEN", "CLOSED"]:
            raise ValueError(f"Invalid response for 'interlock_mode': {response}")
        return response

    @property
    def interlock_open(self) -> bool:
        """
        Returns:
            bool: True if interlock_mode == OPEN
        """
        return self.interlock_mode == "OPEN"

    @property
    def control_mode(self) -> str:
        """
        Read out Control Mode (LOCAL / REMOTE)

        Returns:
            str: The control mode.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDCTR"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        if response not in ["LOCAL", "REMOTE"]:
            raise ValueError(f"Invalid response for 'control_mode': {response}")
        return response

    @property
    def control_mode_local(self) -> bool:
        """
        Returns:
            bool: True if control_mode == LOCAL
        """
        return self.control_mode == "LOCAL"

    @property
    def control_mode_remote(self) -> bool:
        """
        Returns:
            bool: True if control_mode == REMOTE
        """
        return self.control_mode == "REMOTE"

    @control_mode.setter
    def control_mode(self, value: str):
        """
        Set Control Mode (LOCAL / REMOTE)

        Args:
            value (str): The control mode.
        """
        value = value.upper()
        if value not in ["LOCAL", "REMOTE"]:
            raise ValueError(f"Invalid value for 'control_mode': {value}")
        self._serial.write(_get_set_module_command(self._bd, "BDCTR", value))

    def set_control_mode_local(self):
        """
        Set Control Mode to LOCAL
        """
        self.control_mode = "LOCAL"

    def set_control_mode_remote(self):
        """
        Set Control Mode to REMOTE
        """
        self.control_mode = "REMOTE"

    @property
    def local_bus_termination_status(self) -> str:
        """
        Read out LOCAL BUS Termination status (ON/OFF)

        Returns:
            str: The local bus termination status.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDTERM"))
        response = _parse_response(self._serial.readline(), bd=self.bd)
        if response not in ["ON", "OFF"]:
            raise ValueError(
                f"Invalid response for 'local_bus_termination_status': {response}"
            )
        return response

    @property
    def local_bus_termination_status_on(self) -> bool:
        """
        Returns:
            bool: True if local_bus_termination_status == ON
        """
        return self.local_bus_termination_status == "ON"

    @property
    def local_bus_termination_status_off(self) -> bool:
        """
        Returns:
            bool: True if local_bus_termination_status == OFF
        """
        return self.local_bus_termination_status == "OFF"

    @property
    def board_alarm_status(self) -> dict:
        """
        Read out Board Alarm status value (XXXXX)

        Returns:
            str: The board alarm status value.
        """
        self._serial.write(_get_mon_module_command(self._bd, "BDALARM"))
        response = _parse_response(self._serial.readline(), bd=self.bd)

        bit_array = string_to_bit_array(response)

        return {
            "CH0": bool(bit_array[0]),  # True: Ch0 in Alarm status
            "CH1": bool(bit_array[1]),  # True: Ch1 in Alarm status
            "CH2": bool(bit_array[2]),  # True: Ch2 in Alarm status
            "CH3": bool(bit_array[3]),  # True: Ch3 in Alarm status
            "PWFAIL": bool(bit_array[4]),  # True: Board in POWER FAIL
            "OVP": bool(bit_array[5]),  # True: Board in OVER POWER
            "HVCKFAIL": bool(
                bit_array[6]
            ),  # True: Internal HV Clock FAIL (≠ 200±10kHz)
        }

    @interlock_mode.setter
    def interlock_mode(self, mode: str) -> None:
        """
        VAL:OPEN/CLOSED Set Interlock Mode

        Args:
            mode (str): The interlock mode to set.
        """
        mode = mode.upper()
        if mode not in ["OPEN", "CLOSED"]:
            raise ValueError(f"Invalid value for 'interlock_mode': {mode}")
        self._serial.write(_get_set_module_command(self._bd, "BDILKM", mode))
        _ = _parse_response(self._serial.readline(), bd=self.bd)

    def close_interlock(self) -> None:
        """
        Close Interlock
        """
        self.interlock_mode = "CLOSED"

    def open_interlock(self) -> None:
        """
        Open Interlock
        """
        self.interlock_mode = "OPEN"

    def clear_alarm_signal(self) -> None:
        """
        Clear alarm signal
        """
        self._serial.write(_get_set_module_command(self._bd, "BDCLR", None))
        _ = _parse_response(self._serial.readline(), bd=self.bd)

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
