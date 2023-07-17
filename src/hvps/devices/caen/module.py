import inspect
from functools import cached_property
from typing import List

from ...commands.caen.module import (
    _get_mon_module_command,
    _get_set_module_command,
    _MON_MODULE_COMMANDS,
)
from ...commands.caen import _write_command
from ...utils.utils import string_number_to_bit_array, check_command_output_and_convert
from .channel import Channel
from ..module import Module as BaseModule


class Module(BaseModule):
    @property
    def bd(self) -> int:
        """The bd value of the module.

        Returns:
            int: The bd value.
        """
        return self.module

    def channel(self, channel: int) -> Channel:
        return super().channel(channel)

    @cached_property
    def number_of_channels(self) -> int:
        """The number of channels in the module.

        Returns:
            int: The number of channels.
        """
        self._logger.debug("Getting number of channels")
        if not self._serial.is_open:
            # TODO: we should not cache the property if the serial port is not open
            self._logger.warning(
                "Serial port is not open. Returning 1 as number of channels."
            )
            return 1

        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_module_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self.bd,
            command=_get_mon_module_command(self.bd, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_MODULE_COMMANDS
        )

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
                        ser=self._serial,
                        logger=self._logger,
                        channel=channel,
                        bd=self.bd,
                    )
                )
        return self._channels

    @cached_property
    def name(self) -> str:
        """The name of the module.

        Returns:
            str: The name of the module.
        """
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_module_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self.bd,
            command=_get_mon_module_command(self.bd, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_MODULE_COMMANDS
        )

    @property
    def firmware_release(self) -> str:
        """
        Read out Firmware Release (XX.X)

        Returns:
            str: The firmware release.
        """
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_module_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self.bd,
            command=_get_mon_module_command(self.bd, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_MODULE_COMMANDS
        )

    @property
    def serial_number(self) -> str:
        """
        Read out value serial number (XXXXX)

        Returns:
            str: The serial number.
        """
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_module_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self.bd,
            command=_get_mon_module_command(self.bd, command_name),
        )
        # TODO: check if can be casted to int
        return check_command_output_and_convert(
            command_name, None, response, _MON_MODULE_COMMANDS
        )

    @property
    def interlock_status(self) -> bool:
        """
        Read out INTERLOCK status (YES/NO)

        Returns:
            bool: Yes: True, No: False
        """
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_module_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self.bd,
            command=_get_mon_module_command(self.bd, command_name),
        )
        response = check_command_output_and_convert(
            command_name, None, response, _MON_MODULE_COMMANDS
        )
        return response == "YES"

    @property
    def interlock_mode(self) -> str:
        """
        Read out INTERLOCK mode (OPEN/CLOSED)

        Returns:
            str: The interlock mode.
        """
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_module_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self.bd,
            command=_get_mon_module_command(self.bd, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_MODULE_COMMANDS
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
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_module_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self.bd,
            command=_get_mon_module_command(self.bd, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_MODULE_COMMANDS
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
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_module_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self.bd,
            command=_get_mon_module_command(self.bd, command_name),
        )
        if response not in ["ON", "OFF"]:
            raise ValueError(
                f"Invalid response for 'local_bus_termination_status': {response}"
            )
        return check_command_output_and_convert(
            command_name, None, response, _MON_MODULE_COMMANDS
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
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_module_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self.bd,
            command=_get_mon_module_command(self.bd, command_name),
        )
        check_command_output_and_convert(
            command_name, None, response, _MON_MODULE_COMMANDS
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

        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_module_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self.bd,
            command=_get_set_module_command(self.bd, command_name, mode),
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
        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_module_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self.bd,
            command=_get_set_module_command(self.bd, command_name, None),
        )


_mon_module_methods_to_commands = {
    "number_of_channels": "BDNCH",
    "name": "BDNAME",
    "firmware_release": "BDFREL",
    "serial_number": "BDSNUM",
    "interlock_status": "BDILK",
    "interlock_mode": "BDILKM",
    "local_bus_termination_status": "BDTERM",
    "control_mode": "BDCTR",
    "board_alarm_status": "BDALARM",
}
_set_module_methods_to_commands = {
    "interlock_mode": "BDILKM",
    "clear_alarm_signal": "BDCLR",
}
