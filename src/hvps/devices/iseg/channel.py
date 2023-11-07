from __future__ import annotations

import inspect
from typing import List

from hvps.utils import check_command_input

from ...commands.iseg.channel import (
    _get_set_channel_command,
    _get_mon_channel_command,
    _MON_CHANNEL_COMMANDS,
    _SET_CHANNEL_COMMANDS,
)

from ..channel import Channel as BaseChannel
from ...utils.utils import check_command_output_and_convert


class Channel(BaseChannel):
    def _write_command_read_response_channel_mon(
        self, method_name: str, expected_response_type: type | None
    ) -> str | int | float | List | None:
        command = _MON_CHANNEL_COMMANDS[method_name]["command"]
        check_command_input(_MON_CHANNEL_COMMANDS, method_name)
        response = self._write_command_read_response(
            command=_get_mon_channel_command(channel=self.channel, command=command),
            expected_response_type=expected_response_type,
        )
        return check_command_output_and_convert(
            method_name, None, response, _MON_CHANNEL_COMMANDS
        )

    def _write_command_read_response_channel_set(
        self,
        method_name: str,
        value: str | int | float | None,
        expected_response_type: type | None,
    ) -> str | None:
        command = _SET_CHANNEL_COMMANDS[method_name]["command"]
        check_command_input(_SET_CHANNEL_COMMANDS, method_name, value)
        response = self._write_command_read_response(
            command=_get_set_channel_command(
                channel=self.channel, command=command, value=value
            ),
            expected_response_type=expected_response_type,
        )
        if response != "1":
            raise ValueError("Last command haven't been processed.")
        return response

    # Getters
    @property
    def trip_action(
        self,
    ) -> int:  # Instruction for NHR or SHR only. Instruction for NHS
        """
        Query the current action to be taken when a current trip occurs for the channel.

        Returns:
            The current action value.
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def trip_timeout(
        self,
    ) -> int:  # Instruction for NHR or SHR only. Instruction for NHS
        """
        Query the current action to be taken when a current trip occurs for the channel.

        Returns:
            The current action value.
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def external_inhibit_action(
        self,
    ) -> int:  # Instruction for NHR or SHR only. Instruction for NHS
        """
        Query the action that should happen when an External Inhibit for the channel occurs.

        Returns:
            The current action value.
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def output_mode(self) -> int:  # Instruction for NHR or SHR only.
        """
        Query the configured channel output mode.

        Returns:
            The current output mode value.

        Output Mode allowed values: 1, 2, 3.
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def available_output_modes(self) -> List[int]:  # Instruction for NHR or SHR only
        """
        Query the available channel output modes as a list.

        Returns:
            The list of available output mode values.

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=List[int],
        )

    @property
    def output_polarity(self) -> str:  # Instruction for NHR or SHR only
        """
        Query the current output polarity of the channel.

        Returns:
            The current output polarity. "p" for positive, "n" for negative.

        Example:
            polarity = channel.output_polarity
            print(polarity)  # Example output: "n"
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=str,
        )

    @property
    def available_output_polarities(
        self,
    ) -> List[str]:  # Instruction for NHR or SHR only
        """
        Query the available channel output polarities as a list.

        Returns:
            The list of available output polarity values.

        Output Polarity List:
            "p" - Positive
            "n" - Negative

        Example:
            polarities = channel.available_output_polarities
            print(polarities)  # Example output: ["p", "n"]
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=List[str],
        )

    @property
    def voltage_set(self) -> float:
        """
        Query the voltage set Vset in Volt.

        Returns:
            float: The voltage set Vset in Volt.

        Example:
            voltage = channel.voltage_set
            print(voltage)  # Example output: 1234.0
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def voltage_limit(self) -> float:  # Instruction for SHR only
        """
        Query the voltage limit Vlim in Volt.

        Returns:
            float: The voltage limit Vlim in Volt.

        Example:
            limit = channel.voltage_limit
            print(limit)  # Example output: 3000.0
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def voltage_nominal(self) -> float:
        """
        Query the channel voltage nominal Vnom in Volt.

        Returns:
            float: The channel voltage nominal Vnom in Volt.

        Example:
            nominal = channel.voltage_nominal
            print(nominal)  # Example output: 6000.0
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def voltage_mode(self) -> float:  # Instruction for NHR or SHR only
        """
        Query the configured channel voltage mode with polarity sign in Volt.

        Returns:
            float: The configured channel voltage mode with polarity sign in Volt.

        Example:
            mode = channel.voltage_mode
            print(mode)  # Example output: 6.0
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def voltage_mode_list(self) -> List[float]:  # Instruction for NHR or SHR only
        """
        Query the available channel voltage modes as a list.

        Returns:
            List[float]: The 3 available channel voltage modes as a list of strings.

        Example:
            mode_list = channel.voltage_mode_list
            print(mode_list)  # Example output: [2.0E3, 4.0E3, 6.0E3]
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=List[float],
        )

    @property
    def voltage_bounds(self) -> float:
        """
        Query the channel voltage bounds in Volt.

        Returns:
            float: The channel voltage bounds in Volt.

        Example:
            bounds = channel.voltage_bounds
            print(bounds)  # Example output: 0.00000E3
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def set_on(self) -> bool:
        """
        Query the channel control bit "Set On".

        Returns:
            bool: True if the channel control bit is set on, False otherwise.

        Example:
            is_on = channel.set_on
            print(is_on)  # Example output: True
        """
        return (
            self._write_command_read_response_channel_mon(
                method_name=inspect.currentframe().f_code.co_name,
                expected_response_type=int,
            )
            == 1
        )

    @property
    def emergency_off(self) -> bool:
        """
        Query the channel control bit "Set Emergency Off".

        Returns:
            bool: True if the channel control bit is set to Emergency Off, False otherwise.

        Example:
            is_emergency_off = channel.emergency_off
            print(is_emergency_off)  # Example output: False
        """
        return (
            self._write_command_read_response_channel_mon(
                method_name=inspect.currentframe().f_code.co_name,
                expected_response_type=int,
            )
            == 1
        )

    @property
    def current_set(self) -> float:
        """
        Query the current set (Iset) in Ampere.

        Returns:
            float: The current set value.

        Example:
            current = channel.current_set
            print(current)  # Example output: 50.000E-6

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def current_limit(self) -> float:  # Instruction for SHR only
        """
        Query the current limit (Ilim) in Ampere.

        Returns:
            float: The current limit value.

        Example:
            limit = channel.current_limit
            print(limit)  # Example output: 5.00000E-3

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def current_nominal(self) -> float:
        """
        Query the current nominal (Inom) in Ampere.

        Returns:
            float: The current nominal value.

        Example:
            nominal = channel.current_nominal
            print(nominal)  # Example output: 6.00000E-3

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def current_mode(self) -> float:  # Instruction for NHR or SHR only
        """
        Query the configured channel current mode in Ampere.

        Returns:
            float: The current mode value.

        Example:
            mode = channel.current_mode
            print(mode)  # Example output: 2.00000E-3

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def current_mode_list(self) -> List[float]:  # Instruction for NHR or SHR only
        """
        Query the available channel current modes as a list.

        Returns:
            List[float]: The list of available current modes.

        Example:
            modes = channel.current_mode_list
            print(modes)  # Example output: [6.0E-3, 4.0E-3, 2.0E-3]

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=List[float],
        )

    @property
    def current_bounds(self) -> float:
        """
        Query the channel current bounds in Ampere.

        Returns:
            float: The channel current bounds.

        Example:
            bounds = channel.current_bounds
            print(bounds)  # Example output: 0.00000E-3

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def current_ramp_speed(self) -> float:  # Instruction for EHS, NHR or SHR only
        """
        Query the channel current ramp speed in Ampere/second.

        Returns:
            float: The channel current ramp speed.

        Example:
            speed = channel.current_ramp_speed
            print(speed)  # Example output: 2.0000E-3

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def voltage_ramp_speed(self) -> float:  # Instruction for EHS, NHR or SHR only
        """
        Query the channel voltage ramp speed in Volt/second.

        Returns:
            float: The channel voltage ramp speed.

        Example:
            speed = channel.voltage_ramp_speed
            print(speed)  # Example output: 0.25000E3

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def voltage_ramp_speed_minimum(
        self,
    ) -> float:  # Instruction for EHS, NHR or SHR only
        """
        Query the channel voltage ramp speed minimum in Volt/second.

        Returns:
            float: The channel voltage ramp speed minimum.

        Example:
            speed_min = channel.voltage_ramp_speed_minimum
            print(speed_min)  # Example output: 0.00005E3

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def voltage_ramp_speed_maximum(
        self,
    ) -> float:  # Instruction for EHS, NHR or SHR only
        """
        Query the channel voltage ramp speed maximum in Volt/second.

        Returns:
            float: The channel voltage ramp speed maximum.

        Example:
            speed_max = channel.voltage_ramp_speed_maximum
            print(speed_max)  # Example output: 1.20000E3

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def current_ramp_speed_minimum(
        self,
    ) -> float:  # Instruction for EHS, NHR or SHR only
        """
        Query the channel current ramp speed minimum in Ampere/second.

        Returns:
            float: The channel current ramp speed minimum.

        Example:
            speed_min = channel.current_ramp_speed_minimum
            print(speed_min)  # Example output: 1.0000E-3

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def current_ramp_speed_maximum(
        self,
    ) -> float:  # Instruction for EHS, NHR or SHR only
        """
        Query the channel current ramp speed maximum in Ampere/second.

        Returns:
            float: The channel current ramp speed maximum.

        Example:
            speed_max = channel.current_ramp_speed_maximum
            print(speed_max)  # Example output: 6.0000E-3

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def channel_control(self) -> int:
        """
        Query the Channel Control register.

        Returns:
            int: The Channel Control register value.

        Example:
            control = channel.channel_control
            print(control)  # Example output: 8

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def channel_status(self) -> int:
        """
        Query the Channel Status register.

        Returns:
            int: The Channel Status register value.

        Example:
            status = channel.channel_status
            print(status)  # Example output: 132

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def channel_event_mask(self) -> int:
        """
        Query the Channel Event Mask register.

        Returns:
            int: The Channel Event Mask register value.

        Example:
            mask = channel.channel_event_mask
            print(mask)  # Example output: 0
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=int,
        )

    @property
    def measured_voltage(self) -> float:
        """
        Query the measured channel voltage in Volt.

        Returns:
            float: The measured channel voltage.

        Example:
            voltage = channel.measured_voltage
            print(voltage)  # Example output: 1234.56
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def measured_current(self) -> float:
        """
        Query the measured channel current in Ampere.

        Returns:
            float: The measured channel current.

        Example:
            current = channel.measured_current
            print(current)  # Example output: 0.00123456
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def channel_voltage_ramp_up_speed(
        self,
    ) -> float:  # Instruction for EHS, NHR or SHR only
        """
        Query the channel voltage ramp up speed in Volt/second.

        Returns:
            float: The channel voltage ramp up speed in Volt/second.

        Example:
            speed = channel.channel_voltage_ramp_up_speed
            print(speed)  # Example output: 0.250E3
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def channel_voltage_ramp_down_speed(
        self,
    ) -> float:  # Instruction for EHS, NHR or SHR only
        """
        Query the channel voltage ramp down speed in Volt/second.

        Returns:
            float: The channel voltage ramp down speed in Volt/second.

        Example:
            speed = channel.channel_voltage_ramp_down_speed
            print(speed)  # Example output: 0.12500E3
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def channel_current_ramp_up_speed(self) -> float:
        """
        Query the channel current ramp up speed in Ampere/second.

        Returns:
            float: The channel current ramp up speed in Ampere/second.

        Example:
            speed = channel.channel_voltage_ramp_down_speed
            print(speed)  # Example output: 0.12500E3
        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    @property
    def channel_current_ramp_down_speed(self) -> float:
        """
        Query the channel current ramp down speed in Ampere/second.

        Returns:
            float: The channel current ramp down speed in Ampere/second.

        """
        return self._write_command_read_response_channel_mon(
            method_name=inspect.currentframe().f_code.co_name,
            expected_response_type=float,
        )

    # Setters

    @trip_action.setter
    def trip_action(
        self, action: int
    ) -> None:  # Instruction for NHR or SHR only. Instruction for NHS
        """
        Set the action to be taken when a current trip occurs for the channel.

        Args:
            action: The action value to set. Possible values are:
                    - 0: No action (Trip status flag will be set after timeout)
                    - 1: Turn off the channel with ramp
                    - 2: Shut down the channel without ramp
                    - 3: Shut down the whole module without ramp
                    - 4: Disable the Delayed Trip function
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=action,
            expected_response_type=None,
        )
        if self.trip_action != action:
            raise ValueError("Last command haven't been processed.")

    @trip_timeout.setter
    def trip_timeout(
        self, timeout: int
    ) -> None:  # Instruction for NHR or SHR only. Instruction for NHS
        """
        Set the trip timeout with one millisecond resolution.

        Args:
            timeout: The timeout value to set in milliseconds. Must be in the range 1 to 4095 ms.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=timeout,
            expected_response_type=None,
        )
        if self.trip_timeout != timeout:
            raise ValueError("Last command haven't been processed.")

    @external_inhibit_action.setter
    def external_inhibit_action(
        self, action: int
    ) -> None:  # Instruction for NHR or SHR only. Instruction for NHS
        """
        Set the action to be taken when an External Inhibit event occurs for the channel.

        Args:
            action: The action value to set. Possible values are:
                    - 0: No action (External Inhibit status flag will be set)
                    - 1: Turn off the channel with ramp
                    - 2: Shut down the channel without ramp
                    - 3: Shut down the whole module without ramp
                    - 4: Disable the External Inhibit function
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=action,
            expected_response_type=None,
        )
        # if self.external_inhibit_action != action:
        #    raise ValueError("Last command haven't been processed.")

    @output_mode.setter
    def output_mode(self, mode: int) -> None:  # Instruction for NHR or SHR only.
        """
        Set the channel output mode.

        Args:
            mode: The output mode value to set.

        Raises:
            ValueError: If the specified mode value is not allowed.

        Output Mode allowed values: 1, 2, 3.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=mode,
            expected_response_type=None,
        )
        if self.output_mode != mode:
            raise ValueError("Last command haven't been processed.")

    @output_polarity.setter
    def output_polarity(
        self, polarity: str
    ) -> None:  # Instruction for NHR or SHR only.
        """
        Set the output polarity of the channel.

        Args:
            polarity: The output polarity to set. Valid values are "p" for positive and "n" for negative.

        Raises:
            ValueError: If an invalid polarity value is provided.

        Example:
            channel.output_polarity("n")
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=polarity,
            expected_response_type=None,
        )
        if self.output_polarity != polarity:
            raise ValueError("Last command haven't been processed.")

    @voltage_set.setter
    def voltage_set(self, vset: float) -> None:
        """
        Set the channel voltage set.

        Args:
            vset (float): The voltage set value to set in Volt.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=vset,
            expected_response_type=None,
        )
        if not (
            self.voltage_set == round(vset, 1) or self.voltage_set == -round(vset, 1)
        ):
            raise ValueError("Last command haven't been processed.")

    @voltage_bounds.setter
    def voltage_bounds(self, vbounds: float) -> None:
        """
        Set the channel voltage bounds.

        Args:
            vbounds (float): The voltage bounds value to set in Volt.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=vbounds,
            expected_response_type=None,
        )
        if self.voltage_bounds != vbounds:
            raise ValueError("Last command haven't been processed.")

    @current_set.setter
    def current_set(self, iset: float) -> None:
        """
        Set the channel current set.

        Args:
            iset (float): The current set value to set in Ampere.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=iset,
            expected_response_type=None,
        )
        if not (self.current_set == iset or self.current_set == -iset):
            raise ValueError("Last command haven't been processed.")

    @current_bounds.setter
    def current_bounds(self, ibounds: float) -> None:
        """
        Set the channel current bounds.

        Args:
            ibounds (float): The current bounds value to set in Ampere.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=ibounds,
            expected_response_type=None,
        )
        if self.current_bounds != ibounds:
            raise ValueError("Last command haven't been processed.")

    def set_channel_voltage_ramp_up_down_speed(
        self, speed: int
    ) -> None:  # Instruction for EHS, NHR or SHR only
        """
        Set the channel voltage ramp speed for up and down direction in Volt/second.

        Args:
            speed (int): The voltage ramp speed in Volt/second.

        Example:
            channel.set_channel_voltage_ramp_up_down_speed(250)
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=speed,
            expected_response_type=None,
        )
        if (
            self.channel_voltage_ramp_up_speed != speed
            or self.channel_voltage_ramp_down_speed != speed
        ):
            raise ValueError("Last command haven't been processed.")

    @channel_voltage_ramp_up_speed.setter
    def channel_voltage_ramp_up_speed(
        self, speed: int
    ) -> None:  # Instruction for EHS, NHR or SHR only
        """
        Set the channel voltage ramp up speed in Volt/second.

        Args:
            speed (int): The voltage ramp up speed in Volt/second.

        Example:
            channel.set_channel_voltage_ramp_up_speed(250)
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=speed,
            expected_response_type=None,
        )
        if self.channel_voltage_ramp_up_speed != speed:
            raise ValueError("Last command haven't been processed.")

    @channel_voltage_ramp_down_speed.setter
    def channel_voltage_ramp_down_speed(
        self, speed: float
    ) -> None:  # Instruction for EHS, NHR or SHR only
        """
        Set the channel voltage ramp down speed in Volt/second.

        Args:
            speed (float): The channel voltage ramp down speed to set in Volt/second.

        Example:
            channel.set_channel_voltage_ramp_down_speed(125.0)
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=speed,
            expected_response_type=None,
        )
        if self.channel_voltage_ramp_down_speed != speed:
            raise ValueError("Last command haven't been processed.")

    def set_channel_current_ramp_up_down_speed(
        self, speed: float
    ) -> None:  # Instruction for EHS, NHR or SHR only
        """
        Set the channel current ramp speed for up and down direction in Ampere/second.

        Args:
            speed (float): The channel current ramp down speed to set in Ampere/second.

        Example:
            channel.set_channel_current_ramp_up_down_speed(125.0)
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=speed,
            expected_response_type=None,
        )
        if (
            self.channel_current_ramp_up_speed != speed
            or self.channel_current_ramp_down_speed != speed
        ):
            raise ValueError("Last command haven't been processed.")

    @channel_current_ramp_up_speed.setter
    def channel_current_ramp_up_speed(
        self, speed: float
    ) -> None:  # Instruction for EHS, NHR or SHR only
        """
        Set the channel current ramp up speed in Ampere/second.

        Args:
            speed (float): The channel current ramp up speed to set in Ampere/second.

        Example:
            channel.set_channel_current_ramp_up_speed(125.0)
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=speed,
            expected_response_type=None,
        )
        if self.channel_current_ramp_up_speed != speed:
            raise ValueError("Last command haven't been processed.")

    @channel_current_ramp_down_speed.setter
    def channel_current_ramp_down_speed(
        self, speed: float
    ) -> None:  # Instruction for EHS, NHR or SHR only
        """
        Set the channel current ramp down speed in Ampere/second.

        Args:
            speed (float): The channel current ramp down speed to set in Ampere/second.

        Example:
            channel.set_channel_current_ramp_down_speed(125.0)
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=speed,
            expected_response_type=None,
        )
        if self.channel_current_ramp_down_speed != speed:
            raise ValueError("Last command haven't been processed.")

    def switch_on_high_voltage(self) -> None:
        """
        Switch on the high voltage with the configured ramp speed.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=None,
            expected_response_type=None,
        )

    def switch_off_high_voltage(self) -> None:
        """
        Switch off the high voltage with the configured ramp speed.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=None,
            expected_response_type=None,
        )

    def shutdown_channel_high_voltage(self) -> None:
        """
        Shut down the channel high voltage (without ramp). The channel stays in Emergency Off until the command EMCY CLR is given.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=None,
            expected_response_type=None,
        )

    def clear_channel_emergency_off(self) -> None:
        """
        Clear the channel from state emergency off. The channel goes to state off.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=None,
            expected_response_type=None,
        )

    def clear_event_status(self) -> None:
        """
        Clear the Channel Event Status register.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=None,
            expected_response_type=None,
        )

    def clear_event_bits(self, bits: int) -> None:
        """
        Clears single bits or bit combinations in the Channel Event Status register
        by writing a one to the corresponding bit position.

        Args:
            bits: The bits or bit combinations to clear. Should be provided as an integer.
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=bits,
            expected_response_type=None,
        )

    def set_event_mask(self, mask: int) -> None:
        """
        Set the Channel Event Mask register

        Args:
            mask: new mask value
        """
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name,
            value=mask,
            expected_response_type=None,
        )
