from __future__ import annotations
from functools import cached_property
from typing import List

import serial

from ...commands.iseg.module import _get_mon_module_command, _get_set_module_command
from ...commands.iseg import _write_command
from ...utils.utils import string_number_to_bit_array
from ..module import Module as BaseModule
from .channel import Channel


class Module(BaseModule):
    def channel(self, channel: int) -> Channel:
        return super().channel(channel)

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
        response = _write_command(self._serial, None, command, int)
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
        response = _write_command(self._serial, None, command, str)
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
        response = _write_command(self._serial, None, command, dict)
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
            "Is Fine Adjustment": bit_array[0],
        }

    @property
    def filter_averaging_steps(self) -> int:
        """Query the digital filter averaging steps.

        Returns:
            int: The number of steps for filtering.
        """
        command = _get_mon_module_command(":CONF:AVER")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def kill_enable(self) -> int:
        """Get the current value for the kill enable function.

        Returns:
            int: The current kill enable value. 1 for enable, 0 for disable.
        """
        command = _get_mon_module_command(":CONF:KILL")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def adjustment(self) -> int:
        """Get the fine adjustment state.

        Returns:
            int: The current fine adjustment state. 1 for on, 0 for off.
        """
        command = _get_mon_module_command(":CONF:ADJUST")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def module_can_address(self) -> int:
        """Query the module's CAN bus address.

        Returns:
            int: The current CAN bus address of the module.
        """
        command = _get_mon_module_command(":CONF:CAN:ADDR")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def module_can_bitrate(self) -> int:
        """Query the module's CAN bus bit rate.

        Returns:
            int: The current CAN bus bit rate of the module.
        """
        command = _get_mon_module_command(":CONF:CAN:BITRATE")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

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
        command = _get_mon_module_command(":CONF:SERIAL:BAUD")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def serial_echo_enable(self) -> int:
        """Check if serial echo is enabled or disabled.

        Returns:
            int: 1 if serial echo is enabled, 0 if disabled.
        """
        command = _get_mon_module_command(":CONF:SERIAL:ECHO")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

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
        command = _get_mon_module_command(":READ:VOLT:LIM")
        response = _write_command(self._serial, None, command, float)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(response[0].rstrip("%"))

    @property
    def module_current_limit(self) -> float:
        """Query the module's current limit in percent.

        Returns:
            float: The current current limit of the module.
        """
        command = _get_mon_module_command(":READ:CURR:LIM")
        response = _write_command(self._serial, None, command, float)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(response[0].rstrip("%"))

    @property
    def module_voltage_ramp_speed(self) -> float:
        """Query the module's voltage ramp speed in percent/second.

        Returns:
            float: The current voltage ramp speed of the module.
        """
        command = _get_mon_module_command(":READ:RAMP:VOLT")
        response = _write_command(self._serial, None, command, float)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(response[0][:3])

    @property
    def module_current_ramp_speed(self) -> float:
        """Query the module's current ramp speed in percent/second.

        Returns:
            float: The current current ramp speed of the module.
        """
        command = _get_mon_module_command(":READ:RAMP:CURR")
        response = _write_command(self._serial, None, command, float)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(response[0][:3])

    @property
    def module_control_register(self) -> int:
        """Query the Module Control register.

        Returns:
            int: The value of the Module Control register.
        """
        command = _get_mon_module_command(":READ:MODULE:CONTROL")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def module_status_register(self) -> int:
        """Query the Module Status register.

        Returns:
            int: The value of the Module Status register.
        """
        command = _get_mon_module_command(":READ:MODULE:STATUS")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def module_event_status_register(self) -> int:
        """Query the Module Event Status register.

        Returns:
            int: The value of the Module Event Status register.
        """
        command = _get_mon_module_command(":READ:MODULE:EVENT:STATUS")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def module_event_mask_register(self) -> int:
        """Query the Module Event Mask register.

        Returns:
            int: The value of the Module Event Mask register.
        """
        command = _get_mon_module_command(":READ:MODULE:EVENT:MASK")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def module_event_channel_status_register(self) -> int:
        """Query the Module Event Channel Status register.

        Returns:
            int: The value of the Module Event Channel Status register.
        """
        command = _get_mon_module_command(":READ:MODULE:EVENT:CHANSTAT")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def module_event_channel_mask_register(self) -> int:
        """Query the Module Event Channel Mask register.

        Returns:
            int: The value of the Module Event Channel Mask register.
        """
        command = _get_mon_module_command(":READ:MODULE:EVENT:CHANMASK")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def module_supply_voltage(self) -> List[float]:
        """Query the module supply voltages.

        Returns:
            Tuple[str, str, str, str, str, str]: The module supply voltages.
        """
        command = _get_mon_module_command(":READ:MODULE:SUPPLY? (@0-6)")
        response = _write_command(self._serial, None, command, List[float])
        if len(response) != 7:
            raise ValueError("Wrong number of values were received, one value expected")

        return [float(string[:-1]) for string in response]

    @property
    def module_supply_voltage_p24v(self) -> float:
        """Query the module supply voltage +24 Volt.

        Returns:
            float: The module supply voltage +24 Volt.
        """
        command = _get_mon_module_command(":READ:MODULE:SUPPLY:P24V")
        response = _write_command(self._serial, None, command, float)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        voltage = response[0][:-1]
        return float(voltage)

    @property
    def module_supply_voltage_n24v(self) -> float:
        """Query the module supply voltage -24 Volt.

        Returns:
            float: The module supply voltage -24 Volt.
        """
        command = _get_mon_module_command(":READ:MODULE:SUPPLY:N24V")
        response = _write_command(self._serial, None, command, float)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        voltage = response[0][:-1]
        return float(voltage)

    @property
    def module_supply_voltage_p5v(self) -> float:
        """Query the module supply voltage +5 Volt.

        Returns:
            float: The module supply voltage +5 Volt.
        """
        command = _get_mon_module_command(":READ:MODULE:SUPPLY:P5V")
        response = _write_command(self._serial, None, command, float)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        voltage = response[0][:-1]
        return float(voltage)

    @property
    def module_supply_voltage_p3v(self) -> float:
        """Query the module internal supply voltage +3.3 Volt.

        Returns:
            float: The module internal supply voltage +3.3 Volt.
        """
        command = _get_mon_module_command(":READ:MODULE:SUPPLY:P3V")
        response = _write_command(self._serial, None, command, float)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        voltage = response[0][:-1]
        return float(voltage)

    @property
    def module_supply_voltage_p12v(self) -> float:
        """Query the module internal supply voltage +12 Volt.

        Returns:
            float: The module internal supply voltage +12 Volt.
        """
        command = _get_mon_module_command(":READ:MODULE:SUPPLY:P12V")
        response = _write_command(self._serial, None, command, float)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        voltage = response[0][:-1]
        return float(voltage)

    @property
    def module_supply_voltage_n12v(self) -> float:
        """Query the module internal supply voltage -12 Volt.

        Returns:
            float: The module internal supply voltage -12 Volt.
        """
        command = _get_mon_module_command(":READ:MODULE:SUPPLY:N12V")
        response = _write_command(self._serial, None, command, float)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        voltage = response[0][:-1]
        return float(voltage)

    @property
    def module_temperature(self) -> float:
        """Query the module temperature in degree Celsius.

        Returns:
            float: The module temperature in degree Celsius.
        """
        command = _get_mon_module_command(":READ:MODULE:TEMPERATURE")
        response = _write_command(self._serial, None, command, float)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        temperature = response[0][:-1]
        return float(temperature)

    @property
    def setvalue_changes_counter(self) -> int:
        """Query the setvalue changes counter.

        Returns:
            int: The setvalue changes counter.
        """
        command = _get_mon_module_command(":READ:MODULE:SETVALUE")
        response = _write_command(self._serial, None, command, int)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0])

    @property
    def firmware_name(self) -> str:
        """Query the module's firmware name.

        Returns:
            str: The firmware name.
        """
        command = _get_mon_module_command(":READ:FIRMWARE:NAME")
        response = _write_command(self._serial, None, command, str)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return response[0]

    @property
    def configuration_mode(self) -> bool:
        """Check if the device is in configuration mode.

        Returns:
            bool: true if in configuration mode, otherwise false.
        """
        command = _get_mon_module_command(":SYSTEM:USER:CONFIG")
        response = _write_command(self._serial, None, command, bool)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0]) == 1

    # Setters

    @serial_baud_rate.setter
    def serial_baud_rate(self, baud_rate: int) -> None:
        """Set the device's serial baud rate.

        Args:
            baud_rate (int): The serial baud rate to set.
        """
        command = _get_set_module_command(":CONF:SERIAL:BAUD", baud_rate)
        response = _write_command(self._serial, None, command, None)
        if len(response) != 1 or int(response[0]) != baud_rate:
            raise ValueError("Last command hasn't been processed.")

    @serial_echo_enable.setter
    def serial_echo_enable(self, enabled: int) -> None:
        """Enable or disable serial echo.

        Args:
            enabled (int): 1 to enable serial echo, 0 to disable.
        """
        if enabled not in [0, 1]:
            raise ValueError(
                "Invalid serial echo value. Please choose 1 for enabled or 0 for disabled."
            )

        command = _get_set_module_command(":CONF:SERIAL:ECHO", enabled)
        response = _write_command(self._serial, None, command, None)
        if len(response) != 1 or int(response[0]) != 1:
            raise ValueError("Last command hasn't been processed.")

    @filter_averaging_steps.setter
    def filter_averaging_steps(self, steps: int) -> None:
        """Set the number of digital filter averaging steps.

        Args:
            steps (int): The number of steps for filtering. Accepts values 1, 16, 64, 256, 512, or 1024.

        Raises:
            ValueError: If an invalid number of steps is provided.
        """
        valid_steps = [1, 16, 64, 256, 512, 1024]
        if steps not in valid_steps:
            raise ValueError(
                f"Invalid number of steps. Please choose from {valid_steps}."
            )

        command = _get_set_module_command(":CONF:AVER", str(steps))
        response = _write_command(self._serial, None, command, None)
        if len(response) != 1 or int(response[0]) != 1:
            raise ValueError("Last command hasn't been processed.")

    @kill_enable.setter
    def kill_enable(self, enable: int) -> None:
        """Set function kill enable (1) or kill disable (0).

        Args:
            enable (int): The kill enable value to set. Accepts 1 for enable or 0 for disable.
        """
        if enable not in [0, 1]:
            raise ValueError(
                "Invalid kill enable value. Please choose 1 for enable or 0 for disable."
            )

        command = _get_set_module_command(":CONF:KILL", str(enable))
        response = _write_command(self._serial, None, command, None)
        if len(response) != 1 or int(response[0]) != 1:
            raise ValueError("Last command hasn't been processed.")

    @adjustment.setter
    def adjustment(self, value: int) -> None:
        """Set the fine adjustment function on (1) or off (0).

        Args:
            value (int): The adjustment value to set. Accepts 1 for on or 0 for off.
        """
        if value not in [0, 1]:
            raise ValueError(
                "Invalid adjustment value. Please choose 1 for on or 0 for off."
            )

        command = _get_set_module_command(":CONF:ADJUST", str(value))
        response = _write_command(self._serial, None, command, None)
        if len(response) != 1 or int(response[0]) != 1:
            raise ValueError("Last command hasn't been processed.")

    @module_event_mask_register.setter
    def module_event_mask_register(self, mask: int) -> None:
        """Set the Module Event Mask register.

        Args:
            mask (int): The value to set in the Module Event Mask register.
        """
        command = _get_set_module_command(":CONF:EVENT:MASK", str(mask))
        response = _write_command(self._serial, None, command, None)
        if len(response) != 1 or int(response[0]) != 1:
            raise ValueError("Last command hasn't been processed.")

    @module_event_channel_mask_register.setter
    def module_event_channel_mask_register(self, mask: int) -> None:
        """Set the Module Event Channel Mask register.

        Args:
            mask (int): The value to set in the Module Event Channel Mask register.
        """
        command = _get_set_module_command(":CONF:EVENT:CHANMASK", str(mask))
        response = _write_command(self._serial, None, command, None)
        if len(response) != 1 or int(response[0]) != 1:
            raise ValueError("Last command hasn't been processed.")

    @module_can_address.setter
    def module_can_address(self, address: int) -> None:
        """Set the module's CAN bus address.

        Args:
            address (int): The CAN bus address to set (0-63).
        """
        if not (0 <= address <= 63):
            raise ValueError(
                "Invalid CAN bus address. Please choose an address between 0 and 63."
            )

        command = _get_set_module_command(":CONF:CAN:ADDR", str(address))
        response = _write_command(self._serial, None, command, None)
        if len(response) != 1 or int(response[0]) != 1:
            raise ValueError("Last command hasn't been processed.")

    @module_can_bitrate.setter
    def module_can_bitrate(self, bitrate: int) -> None:
        """Set the module's CAN bus bit rate.

        Args:
            bitrate (int): The CAN bus bit rate to set. Accepts 125000 or 250000.
        """
        if bitrate not in [125000, 250000]:
            raise ValueError(
                "Invalid CAN bus bitrate. Please choose either 125000 or 250000."
            )

        command = _get_set_module_command(":CONF:CAN:BITRATE", str(bitrate))
        response = _write_command(self._serial, None, command, None)
        if len(response) != 1 or int(response[0]) != 1:
            raise ValueError("Last command hasn't been processed.")

    def enter_configuration_mode(self, serial_number: int):
        """Set the device to configuration mode to change the CAN bitrate or address.

        Parameters:
            serial_number (int): The device serial number.

        """
        command = _get_set_module_command(":SYSTEM:USER:CONFIG", str(serial_number))
        _write_command(self._serial, None, command, None)

    def exit_configuration_mode(self):
        """Set the device back to normal mode."""
        command = _get_set_module_command(":SYSTEM:USER:CONFIG", "0")
        _write_command(self._serial, None, command, None)

    def set_serial_echo_enabled(self) -> None:
        """Enable serial echo."""
        self.serial_echo_enable = 1

    def set_serial_echo_disabled(self) -> None:
        """Disable serial echo."""
        self.serial_echo_enable = 0

    def reset_module_event_status(self) -> None:
        """Reset the Module Event Status register."""
        command = _get_set_module_command(":CONF:EVENT CLEAR", "")
        response = _write_command(self._serial, None, command, None)
        if len(response) != 1 or int(response[0]) != 1:
            raise ValueError("Last command hasn't been processed.")

    def clear_module_event_status_bits(self, bits: int) -> None:
        """Clear single bits or bit combinations in the Module Event Status register.

        Args:
            bits (int): The bits to clear in the Module Event Status register.
        """
        command = _get_set_module_command(":CONF:EVENT", str(bits))
        response = _write_command(self._serial, None, command, None)
        if len(response) != 1 or int(response[0]) != 1:
            raise ValueError("Last command hasn't been processed.")
