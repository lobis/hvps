from __future__ import annotations
import inspect
from typing import List

from hvps.utils import check_command_input
from serial import SerialException

from ...commands.caen.module import (
    _get_mon_module_command,
    _get_set_module_command,
    _MON_MODULE_COMMANDS,
    _SET_MODULE_COMMANDS,
)
from ...utils.utils import string_number_to_bit_array, check_command_output_and_convert
from .channel import Channel
from ..module import Module as BaseModule


class Module(BaseModule):
    def _write_command_read_response_module_mon(
        self, method_name: str
    ) -> str | int | float | None:
        command = _MON_MODULE_COMMANDS[method_name]["command"]
        check_command_input(_MON_MODULE_COMMANDS, method_name)
        response = self._write_command_read_response(
            bd=self.bd,
            command=_get_mon_module_command(bd=self.bd, command=command),
        )
        return check_command_output_and_convert(
            method_name, None, response, _MON_MODULE_COMMANDS
        )

    def _write_command_read_response_module_set(
        self, method_name: str, value: str | int | float | None
    ) -> str | None:
        command = _SET_MODULE_COMMANDS[method_name]["command"]
        check_command_input(_SET_MODULE_COMMANDS, method_name, value)
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
            return self._write_command_read_response_module_mon(
                method_name=inspect.currentframe().f_code.co_name
            )
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
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name
        )

    @property
    def firmware_release(self) -> str:
        """
        Read out Firmware Release (XX.X)

        Returns:
            str: The firmware release.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name
        )

    @property
    def serial_number(self) -> str:
        """
        Read out value serial number (XXXXX)

        Returns:
            str: The serial number.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name
        )

    @property
    def interlock_status(self) -> bool:
        """
        Read out INTERLOCK status (YES/NO)

        Returns:
            bool: Yes: True, No: False
        """
        response = self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name
        )
        return response == "YES"

    @property
    def interlock_mode(self) -> str:
        """
        Read out INTERLOCK mode (OPEN/CLOSED)

        Returns:
            str: The interlock mode.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name
        )

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
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name
        )

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

    @property
    def local_bus_termination_status(self) -> str:
        """
        Read out LOCAL BUS Termination status (ON/OFF)

        Returns:
            str: The local bus termination status.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name
        )

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
        command = _MON_MODULE_COMMANDS[inspect.currentframe().f_code.co_name]["command"]
        response = self._write_command_read_response(
            bd=self.bd,
            command=_get_mon_module_command(bd=self.bd, command=command),
        )
        check_command_output_and_convert(
            "board_alarm_status", None, response, _MON_MODULE_COMMANDS
        )
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
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name, value=mode
        )

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
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name, value=None
        )
