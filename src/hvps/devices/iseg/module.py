from __future__ import annotations

import inspect
from typing import List

from hvps.utils import check_command_input
from serial import SerialException

from ...commands.iseg.module import (
    _get_mon_module_command,
    _get_set_module_command,
    _MON_MODULE_COMMANDS,
    _SET_MODULE_COMMANDS,
)
from ...utils.utils import string_number_to_bit_array, check_command_output_and_convert

from ..module import Module as BaseModule
from .channel import Channel


class Module(BaseModule):
    def _write_command_read_response_module_mon(
        self, method_name: str, expected_response_type: type | None
    ) -> str | int | float | List | None:
        command = _MON_MODULE_COMMANDS[method_name]["command"]
        check_command_input(_MON_MODULE_COMMANDS, method_name)
        response = self._write_command_read_response(
            command=_get_mon_module_command(command=command),
            expected_response_type=expected_response_type,
        )
        return check_command_output_and_convert(
            command, None, response, _MON_MODULE_COMMANDS
        )

    def _write_command_read_response_module_set(
        self,
        method_name: str,
        value: str | int | float | None,
        expected_response_type: type | None,
    ) -> str | None:
        command = _SET_MODULE_COMMANDS[method_name]["command"]
        check_command_input(_SET_MODULE_COMMANDS, method_name, value)
        response = self._write_command_read_response(
            command=_get_set_module_command(command=command, value=value),
            expected_response_type=expected_response_type,
        )
        if response != "1":
            raise ValueError("Last command haven't been processed.")
        return response

    def channel(self, channel: int) -> Channel:
        return super().channel(channel)

    @property
    def number_of_channels(self) -> int:
        """The number of channels in the module.

        Returns:
            int: The number of channels.
        """
        self._logger.debug("Getting number of channels")

        try:
            return self._write_command_read_response_module_mon(
                method_name=inspect.currentframe().f_code.co_name,
                expected_response_type=int,
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
                        write_command_read_response=self._write_command_read_response,
                        logger=self._logger,
                    )
                )
        return self._channels

    @property
    def firmware_release(self) -> str:
        """
        Read out Firmware Release (XX.X)

        Returns:
            str: The firmware release.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=str,
        )

    @property
    def module_status(self) -> dict:
        """
        Read out module status register

        Returns:
            str: The board alarm status value.
        """
        command_name = inspect.currentframe().f_code.co_name
        response = self._write_command_read_response_module_mon(
            method_name=command_name, expected_response_type=str
        )
        register = check_command_output_and_convert(
            command_name, None, response, _MON_MODULE_COMMANDS
        )
        bit_array = string_number_to_bit_array(register)
        bit_array = list(reversed(bit_array))

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
            "Is Fine Adjustment": bit_array[0],
        }

    @property
    def filter_averaging_steps(self) -> int:
        """Query the digital filter averaging steps.

        Returns:
            int: The number of steps for filtering.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def kill_enable(self) -> int:
        """Get the current value for the kill enable function.

        Returns:
            int: The current kill enable value. 1 for enable, 0 for disable.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def adjustment(self) -> int:
        """Get the fine adjustment state.

        Returns:
            int: The current fine adjustment state. 1 for on, 0 for off.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def module_can_address(self) -> int:
        """Query the module's CAN bus address.

        Returns:
            int: The current CAN bus address of the module.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def module_can_bitrate(self) -> int:
        """Query the module's CAN bus bit rate.

        Returns:
            int: The current CAN bus bit rate of the module.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def serial_baud_rate(
        self,
    ) -> (
        int
    ):  # Instruction is currently implemented for EHS devices with serial interface only
        """Query the device's serial baud rate.

        Returns:
            int: The current serial baud rate of the device.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def serial_echo_enable(self) -> int:
        """Check if serial echo is enabled or disabled.

        Returns:
            int: 1 if serial echo is enabled, 0 if disabled.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def serial_echo_enabled(self) -> bool:
        return self.serial_echo_enable == 1

    @property
    def serial_echo_disabled(self) -> bool:
        return self.serial_echo_enable == 0

    @property
    def module_voltage_limit(self) -> float:
        """Query the module's voltage limit in percent.

        Returns:
            float: The current voltage limit of the module.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def module_current_limit(self) -> float:
        """Query the module's current limit in percent.

        Returns:
            float: The current electrical current limit of the module.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def module_voltage_ramp_speed(self) -> float:
        """Query the module's voltage ramp speed in percent/second.

        Returns:
            float: The current voltage ramp speed of the module.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def module_current_ramp_speed(self) -> float:
        """Query the module's current ramp speed in percent/second.

        Returns:
            float: The current electrical current ramp speed of the module.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def module_control_register(self) -> int:
        """Query the Module Control register.

        Returns:
            int: The value of the Module Control register.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def module_status_register(self) -> int:
        """Query the Module Status register.

        Returns:
            int: The value of the Module Status register.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def module_event_status_register(self) -> int:
        """Query the Module Event Status register.

        Returns:
            int: The value of the Module Event Status register.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def module_event_mask_register(self) -> int:
        """Query the Module Event Mask register.

        Returns:
            int: The value of the Module Event Mask register.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def module_event_channel_status_register(self) -> int:
        """Query the Module Event Channel Status register.

        Returns:
            int: The value of the Module Event Channel Status register.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def module_event_channel_mask_register(self) -> int:
        """Query the Module Event Channel Mask register.

        Returns:
            int: The value of the Module Event Channel Mask register.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def module_supply_voltage(self) -> List[float]:
        """Query the module supply voltages.

        Returns:
            List[float, float, float, float, float, float, float]: The module supply voltages.
        """
        response = self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=List[float],
        )
        if len(response) != 7:
            raise ValueError(
                "Wrong number of values were received, seven values expected"
            )

        return response

    @property
    def module_supply_voltage_p24v(self) -> float:
        """Query the module supply voltage +24 Volt.

        Returns:
            float: The module supply voltage +24 Volt.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def module_supply_voltage_n24v(self) -> float:
        """Query the module supply voltage -24 Volt.

        Returns:
            float: The module supply voltage -24 Volt.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def module_supply_voltage_p5v(self) -> float:
        """Query the module supply voltage +5 Volt.

        Returns:
            float: The module supply voltage +5 Volt.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def module_supply_voltage_p3v(self) -> float:
        """Query the module internal supply voltage +3.3 Volt.

        Returns:
            float: The module internal supply voltage +3.3 Volt.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def module_supply_voltage_p12v(self) -> float:
        """Query the module internal supply voltage +12 Volt.

        Returns:
            float: The module internal supply voltage +12 Volt.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def module_supply_voltage_n12v(self) -> float:
        """Query the module internal supply voltage -12 Volt.

        Returns:
            float: The module internal supply voltage -12 Volt.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def module_temperature(self) -> float:
        """Query the module temperature in degree Celsius.

        Returns:
            float: The module temperature in degree Celsius.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def setvalue_changes_counter(self) -> int:
        """Query the setvalue changes counter.

        Returns:
            int: The setvalue changes counter.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def firmware_name(self) -> str:
        """Query the module's firmware name.

        Returns:
            str: The firmware name.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=str,
        )

    @property
    def id_string(self) -> str:
        """Query the module's ID string.

        Returns:
            str: The ID string.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=str,
        )

    @property
    def instruction_set(self) -> str:
        """Query the module's instruction set.

        Returns:
            str: The instruction set.
        """
        return self._write_command_read_response_module_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=str,
        )

    # Setters

    @serial_baud_rate.setter
    def serial_baud_rate(self, baud_rate: int) -> None:
        """Set the device's serial baud rate.

        Args:
            baud_rate (int): The serial baud rate to set.
        """
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=baud_rate,
            expected_response_type=None,
        )
        if self.serial_baud_rate != baud_rate:
            raise ValueError("Last command haven't been processed.")

    # Be careful when switching off the echo as there is no other possibilit to synchronize the HV device
    # with the computer (no hardware/software handshake). This mode is only available
    # for compatibility reasons and without support.

    @serial_echo_enable.setter
    def serial_echo_enable(self, enabled: int) -> None:
        """Enable or disable serial echo.

        Args:
            enabled (int): 1 to enable serial echo, 0 to disable.
        """
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=enabled,
            expected_response_type=None,
        )
        if self.serial_echo_enable != enabled:
            raise ValueError("Last command haven't been processed.")

    @filter_averaging_steps.setter
    def filter_averaging_steps(self, steps: int) -> None:
        """Set the number of digital filter averaging steps.

        Args:
            steps (int): The number of steps for filtering. Accepts values 1, 16, 64, 256, 512, or 1024.

        Raises:
            ValueError: If an invalid number of steps is provided.
        """
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=steps,
            expected_response_type=None,
        )
        if self.filter_averaging_steps != steps:
            raise ValueError("Last command haven't been processed.")

    @kill_enable.setter
    def kill_enable(self, enable: int) -> None:
        """Set function kill enable (1) or kill disable (0).

        Args:
            enable (int): The kill enable value to set. Accepts 1 for enable or 0 for disable.
        """
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=enable,
            expected_response_type=None,
        )
        if self.kill_enable != enable:
            raise ValueError("Last command haven't been processed.")

    @adjustment.setter
    def adjustment(self, value: int) -> None:
        """Set the fine adjustment function on (1) or off (0).

        Args:
            value (int): The adjustment value to set. Accepts 1 for on or 0 for off.
        """
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=value,
            expected_response_type=None,
        )
        if self.adjustment != value:
            raise ValueError("Last command haven't been processed.")

    @module_event_mask_register.setter
    def module_event_mask_register(self, mask: int) -> None:
        """Set the Module Event Mask register.

        Args:
            mask (int): The value to set in the Module Event Mask register.
        """
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=mask,
            expected_response_type=None,
        )
        # TODO: check if read value = mask, careful with reserved bits

    @module_event_channel_mask_register.setter
    def module_event_channel_mask_register(self, mask: int) -> None:
        """Set the Module Event Channel Mask register.

        Args:
            mask (int): The value to set in the Module Event Channel Mask register.
        """
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=mask,
            expected_response_type=None,
        )
        # TODO: check if read value = mask, careful with reserved bits

    @module_can_address.setter
    def module_can_address(self, address: int) -> None:
        """Set the module's CAN bus address.

        Args:
            address (int): The CAN bus address to set (0-63).
        """

        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=address,
            expected_response_type=None,
        )
        if self.module_can_address != address:
            raise ValueError("Last command haven't been processed.")

    @module_can_bitrate.setter
    def module_can_bitrate(self, bitrate: int) -> None:
        """Set the module's CAN bus bit rate.

        Args:
            bitrate (int): The CAN bus bit rate to set. Accepts 125000 or 250000.
        """

        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=bitrate,
            expected_response_type=None,
        )
        if self.module_can_bitrate != bitrate:
            raise ValueError("Last command haven't been processed.")

    def enter_configuration_mode(self, serial_number: int):
        """Set the device to configuration mode to change the CAN bitrate or address.

        Parameters:
            serial_number (int): The device serial number.

        """
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=serial_number,
            expected_response_type=None,
        )

    def exit_configuration_mode(self):
        """Set the device back to normal mode."""
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=0,
            expected_response_type=None,
        )

    # Be careful when switching off the echo as there is no other possibilit to synchronize the HV device
    # with the computer (no hardware/software handshake). This mode is only available
    # for compatibility reasons and without support.
    def set_serial_echo_enabled(self) -> None:
        """Enable serial echo."""
        self.serial_echo_enable = 1

    # Be careful when switching off the echo as there is no other possibilit to synchronize the HV device
    # with the computer (no hardware/software handshake). This mode is only available
    # for compatibility reasons and without support.
    def set_serial_echo_disabled(self) -> None:
        """Disable serial echo."""
        self.serial_echo_enable = 0

    def reset_module_event_status(self) -> None:
        """Reset the Module Event Status register."""
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=None,
            expected_response_type=None,
        )

    def clear_module_event_status_bits(self, bits: int) -> None:
        """Clear single bits or bit combinations in the Module Event Status register.

        Args:
            bits (int): The bits to clear in the Module Event Status register.
        """
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=bits,
            expected_response_type=None,
        )

    def clear_all_event_status_registers(self) -> None:
        """Clear all event status registers (module and channels)."""

        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=None,
            expected_response_type=None,
        )

    def reset_to_save_values(self) -> None:
        """Reset the module to the saved values."""
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=None,
            expected_response_type=None,
        )

    def set_command_set(self, command_set: str) -> None:
        """Set the command set to use for the module.

        Args:
            command_set (str): The command set to use for the module.
        """
        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=command_set,
            expected_response_type=None,
        )

    def local_lockout(self) -> None:
        """Lockout the module from the local interface."""

        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=None,
            expected_response_type=None,
        )

    def goto_local(self) -> None:
        """Go to local mode."""

        self._write_command_read_response_module_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=None,
            expected_response_type=None,
        )
