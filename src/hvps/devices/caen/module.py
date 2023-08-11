from __future__ import annotations

from typing import List
from serial import SerialException

from ...commands.caen.module import _get_mon_module_command, _get_set_module_command
from ...utils.utils import string_number_to_bit_array
from .channel import Channel
from ..module import Module as BaseModule


class Module(BaseModule):
    def _write_command_read_response_module_mon(self, command: str) -> str | None:
        return self._write_command_read_response(
            bd=self.bd,
            command=_get_mon_module_command(bd=self.bd, command=command),
        )

    def _write_command_read_response_module_set(
        self, command: str, value: str | int | float | None
    ) -> str | None:
        return self._write_command_read_response(
            bd=self.bd,
            command=_get_set_module_command(bd=self.bd, command=command, value=value),
        )

    @property
    def bd(self) -> int:
        """The bd value of the module.

        Returns:
            int: The bd value.
        """
        return self.module

    def channel(self, channel: int) -> Channel:
        return super().channel(channel)

    @property
    def number_of_channels(self) -> int:
        """The number of channels in the module.

        Returns:
            int: The number of channels.
        """
        try:
            response = self._write_command_read_response_module_mon(command="BDNCH")
            return int(response)
        except SerialException:
            return 1

    @property
    def channels(self) -> List[Channel]:
        """The channels in the module.

        Returns:
            List[Channel]: A list of Channel objects.
        """
        if len(self._channels) == 0:
            self._logger.debug("Initializing channels")
            for channel in range(self.number_of_channels):
                self._logger.debug(f"Creating channel {channel}")
                self._channels.append(
                    Channel(
                        channel=channel,
                        bd=self.bd,
                        write_command_read_response=self._write_command_read_response,
                        logger=self._logger,
                    )
                )
        return self._channels

    @property
    def name(self) -> str:
        """The name of the module.

        Returns:
            str: The name of the module.
        """
        response = self._write_command_read_response_module_mon(command="BDNAME")
        return str(response)

    @property
    def firmware_release(self) -> str:
        """
        Read out Firmware Release (XX.X)

        Returns:
            str: The firmware release.
        """
        response = self._write_command_read_response_module_mon(command="BDFREL")
        return response

    @property
    def serial_number(self) -> str:
        """
        Read out value serial number (XXXXX)

        Returns:
            str: The serial number.
        """
        response = self._write_command_read_response_module_mon(command="BDSNUM")
        # TODO: check if can be casted to int
        return response

    @property
    def interlock_status(self) -> bool:
        """
        Read out INTERLOCK status (YES/NO)

        Returns:
            bool: Yes: True, No: False
        """
        response = self._write_command_read_response_module_mon(command="BDILK")
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
        response = self._write_command_read_response_module_mon(command="BDILKM")
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
        response = self._write_command_read_response_module_mon(command="BDCTR")
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

        self._write_command_read_response_module_set(command="BDCTR", value=value)

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
        response = self._write_command_read_response_module_mon(command="BDTERM")
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
        response = self._write_command_read_response_module_mon(command="BDALARM")

        bit_array = string_number_to_bit_array(response)

        return {
            "CH0": bit_array[0],  # True: Ch0 in Alarm status
            "CH1": bit_array[1],  # True: Ch1 in Alarm status
            "CH2": bit_array[2],  # True: Ch2 in Alarm status
            "CH3": bit_array[3],  # True: Ch3 in Alarm status
            "PWFAIL": bit_array[4],  # True: Board in POWER FAIL
            "OVP": bit_array[5],  # True: Board in OVER POWER
            "HVCKFAIL": bit_array[6],  # True: Internal HV Clock FAIL (≠ 200±10kHz)
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

        self._write_command_read_response_module_set(command="BDILKM", value=mode)

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
        self._write_command_read_response_module_set(command="BDCLR", value=None)
