import serial
from typing import List

from ...commands.iseg.channel import (
    _get_set_channel_command,
    _get_mon_channel_command,
)
from ...commands.iseg import _write_command

from ..channel import Channel as BaseChannel


class Channel(BaseChannel):
    def set_voltage(self, vset: float):
        """
        Set the channel voltage set.

        Args:
            vset (float): The voltage set value to set in Volt.
        """
        command = _get_set_channel_command(self._channel, ":VOLT", vset)
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def switch_on_high_voltage(self):
        """
        Switch on the high voltage with the configured ramp speed.
        """
        command = _get_set_channel_command(self._channel, ":VOLT", "ON")
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def switch_off_high_voltage(self):
        """
        Switch off the high voltage with the configured ramp speed.
        """
        command = _get_set_channel_command(self._channel, ":VOLT", "OFF")
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def shutdown_channel_high_voltage(self):
        """
        Shut down the channel high voltage (without ramp). The channel stays in Emergency Off until the command EMCY CLR is given.
        """
        command = _get_set_channel_command(self._channel, ":VOLT EMCY", "OFF")
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def clear_channel_emergency_off(self):
        """
        Clear the channel from state emergency off. The channel goes to state off.
        """
        command = _get_set_channel_command(self._channel, ":VOLT EMCY", "CLR")
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def set_voltage_bounds(self, vbounds: float):
        """
        Set the channel voltage bounds.

        Args:
            vbounds (float): The voltage bounds value to set in Volt.
        """
        command = _get_set_channel_command(self._channel, ":VOLT:BOUNDS", vbounds)
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def set_current(self, iset: float):
        """
        Set the channel current set.

        Args:
            iset (float): The current set value to set in Ampere.
        """
        command = _get_set_channel_command(self._channel, ":CURR", iset)
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def set_current_bounds(self, ibounds: float):
        """
        Set the channel current bounds.

        Args:
            ibounds (float): The current bounds value to set in Ampere.
        """
        command = _get_set_channel_command(self._channel, ":CURR:BOUNDS", ibounds)
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def clear_event_status(self):
        """
        Clear the Channel Event Status register.
        """
        command = _get_set_channel_command(self._channel, ":EVENT CLEAR", None)
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def clear_event_bits(self, bits):
        """
        Clears single bits or bit combinations in the Channel Event Status register by writing a one to the corresponding bit position.

        Args:
            bits (int | str): The bits or bit combinations to clear. Can be provided as an integer or a string representing the bit combination.
        """
        command = _get_set_channel_command(self._channel, ":EVENT", bits)
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def set_trip_timeout(self, timeout):
        """
        Set the trip timeout with one millisecond resolution.

        Args:
            timeout (int): The timeout value to set in milliseconds. Must be in the range 1 to 4095 ms.
        """
        if not 1 <= timeout <= 4095:
            raise ValueError("Timeout value must be in the range 1 to 4095 ms.")
        command = _get_set_channel_command(self._channel, ":CONF:TRIP:TIME", timeout)
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def set_trip_action(self, action):
        """
        Set the action to be taken when a current trip occurs for the channel.

        Args:
            action (int): The action value to set. Possible values are:
                          - 0: No action (Trip status flag will be set after timeout)
                          - 1: Turn off the channel with ramp
                          - 2: Shut down the channel without ramp
                          - 3: Shut down the whole module without ramp
                          - 4: Disable the Delayed Trip function
        """
        if not 0 <= action <= 4:
            raise ValueError(
                "Invalid action value. Expected values are 0, 1, 2, 3, or 4."
            )
        command = _get_set_channel_command(self._channel, ":CONF:TRIP:ACTION", action)
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    @property
    def trip_action(self):
        """
        Query the current action to be taken when a current trip occurs for the channel.

        Returns:
            int: The current action value.
        """
        command = _get_mon_channel_command(self._channel, ":CONF:TRIP:ACTION")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Unexpected response. Multiple action values received.")
        if not 0 <= int(response[0]) <= 4:
            raise ValueError(
                "Invalid action value. Expected values are 0, 1, 2, 3, or 4."
            )
        return int(response[0])

    def set_external_inhibit_action(self, action):
        """
        Set the action to be taken when an External Inhibit event occurs for the channel.

        Args:
            action (int): The action value to set. Possible values are:
                          - 0: No action (External Inhibit status flag will be set)
                          - 1: Turn off the channel with ramp
                          - 2: Shut down the channel without ramp
                          - 3: Shut down the whole module without ramp
                          - 4: Disable the External Inhibit function
        """
        if not 0 <= action <= 4:
            raise ValueError(
                "Invalid action value. Expected values are 0, 1, 2, 3, or 4."
            )
        command = _get_set_channel_command(self._channel, ":CONF:INHP:ACTION", action)
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    def get_external_inhibit_action(self):
        """
        Query the action to be taken when an External Inhibit event occurs for the channel.

        Returns:
            int: The current action value.
        """
        command = _get_mon_channel_command(self._channel, ":CONF:INHP:ACTION")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Unexpected response. Multiple action values received.")
        if not 0 <= int(response[0]) <= 4:
            raise ValueError(
                "Invalid action value. Expected values are 0, 1, 2, 3, or 4."
            )
        return int(response[0])

    def set_output_mode(self, mode):
        """
        Set the channel output mode.

        Args:
            mode (int): The output mode value to set.

        Raises:
            ValueError: If the specified mode value is not allowed.

        Output Mode allowed values: 1, 2, 3.
        """
        allowed_modes = [1, 2, 3]
        if mode not in allowed_modes:
            raise ValueError("Invalid output mode. Allowed modes are: 1, 2, 3.")
        command = _get_set_channel_command(self._channel, ":CONF:OUTPUT:MODE", mode)
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Last command haven't been processed.")

    @property
    def output_mode(self):
        """
        Query the configured channel output mode.

        Returns:
            int: The current output mode value.

        Output Mode allowed values: 1, 2, 3.
        """
        command = _get_mon_channel_command(self._channel, ":CONF:OUTPUT:MODE")
        response = _write_command(self._serial, command)

        if len(response) != 1:
            raise ValueError("Wrong number of values were sent, one value expected")

        allowed_modes = [1, 2, 3]
        if int(response[0]) not in allowed_modes:
            raise ValueError("Invalid output mode. Allowed modes are: 1, 2, 3.")
        return int(response[0])

    @property
    def available_output_modes(self):
        """
        Query the available channel output modes as a list.

        Returns:
            list: The list of available output mode values.

        """
        command = _get_mon_channel_command(self._channel, ":CONF:OUTPUT:MODE:LIST")
        response = _write_command(self._serial, command)

        if 0 >= len(response) > 3:
            raise ValueError("Invalid number of output modes received.")

        try:
            output_values = [int(mode) for mode in response]
        except ValueError:
            raise ValueError("Invalid output mode value received.")

        allowed_modes = [1, 2, 3]
        for mode in output_values:
            if mode not in allowed_modes:
                raise ValueError(
                    f"Invalid output mode. Allowed modes are: {allowed_modes}"
                )

        return output_values

    def set_output_polarity(self, polarity: str):
        """
        Set the output polarity of the channel.

        Args:
            polarity (str): The output polarity to set. Valid values are "p" for positive and "n" for negative.

        Raises:
            ValueError: If an invalid polarity value is provided.

        Example:
            channel.set_output_polarity("n")
        """
        if polarity not in ["p", "n"]:
            raise ValueError(
                "Invalid polarity value. Valid values are 'p' for positive and 'n' for negative."
            )
        command = _get_set_channel_command(self._channel, ":CONF:OUTPUT:POL", polarity)
        response = _write_command(self._serial, command)
        if int(response[0]) != 1:
            raise ValueError("Not all commands before this query have been processed.")

    @property
    def output_polarity(self):
        """
        Query the current output polarity of the channel.

        Returns:
            str: The current output polarity. "p" for positive, "n" for negative.

        Example:
            polarity = channel.output_polarity
            print(polarity)  # Example output: "n"
        """
        command = _get_mon_channel_command(self._channel, ":CONF:OUTPUT:POL")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Not all commands before this query have been processed.")
        return response[0]

    @property
    def available_output_polarities(self):
        """
        Query the available channel output polarities as a list.

        Returns:
            list: The list of available output polarity values.

        Output Polarity List:
            "p" - Positive
            "n" - Negative

        Example:
            polarities = channel.available_output_polarities
            print(polarities)  # Example output: ["p", "n"]
        """
        command = _get_mon_channel_command(self._channel, ":CONF:OUTPUT:POL:LIST")
        response = _write_command(self._serial, command)

        if len(response) != 2:
            raise ValueError("Wrong number of values were sent, two values expected")

        for polarity in response:
            if polarity not in ["p", "n"]:
                raise ValueError(
                    "Invalid polarity value. Valid values are 'p' for positive and 'n' for negative."
                )

        return response

    @property
    def voltage_set(self):
        """
        Query the voltage set Vset in Volt.

        Returns:
            float: The voltage set Vset in Volt.

        Example:
            voltage = channel.voltage_set
            print(voltage)  # Example output: 1234.0
        """
        command = _get_mon_channel_command(self._channel, ":READ:VOLT")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were sent, one value expected")
        return float(response[0][:-1])

    @property
    def voltage_limit(self):
        """
        Query the voltage limit Vlim in Volt.

        Returns:
            float: The voltage limit Vlim in Volt.

        Example:
            limit = channel.voltage_limit
            print(limit)  # Example output: 3000.0
        """
        command = _get_mon_channel_command(self._channel, ":READ:VOLT:LIM")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were sent, one value expected")
        return float(response[0][:-1])

    @property
    def voltage_nominal(self):
        """
        Query the channel voltage nominal Vnom in Volt.

        Returns:
            float: The channel voltage nominal Vnom in Volt.

        Example:
            nominal = channel.voltage_nominal
            print(nominal)  # Example output: 6000.0
        """
        command = _get_mon_channel_command(self._channel, ":READ:VOLT:NOM")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were sent, one value expected")
        return float(response[0][:-1])

    @property
    def voltage_mode(self):
        """
        Query the configured channel voltage mode with polarity sign in Volt.

        Returns:
            str: The configured channel voltage mode with polarity sign in Volt.

        Example:
            mode = channel.voltage_mode
            print(mode)  # Example output: "6.0E3V"
        """
        command = _get_mon_channel_command(self._channel, ":READ:VOLT:MODE")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were sent, one value expected")
        return float(response[0][:-1])

    @property
    def voltage_mode_list(self):
        """
        Query the available channel voltage modes as a list.

        Returns:
            List[str]: The 3 available channel voltage modes as a list of strings.

        Example:
            mode_list = channel.voltage_mode_list
            print(mode_list)  # Example output: ["2.0E3V", "4.0E3V", "6.0E3V"]
        """
        command = _get_mon_channel_command(self._channel, ":READ:VOLT:MODE:LIST")
        response = _write_command(self._serial, command)
        if len(response) != 3:
            raise ValueError("Wrong number of values were sent, three values expected")
        return [float(modes[:-1]) for modes in response]

    @property
    def voltage_bounds(self):
        """
        Query the channel voltage bounds in Volt.

        Returns:
            str: The channel voltage bounds in Volt.

        Example:
            bounds = channel.voltage_bounds
            print(bounds)  # Example output: "0.00000E3V"
        """
        command = _get_mon_channel_command(self._channel, ":READ:VOLT:BOUNDS")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were sent, one value expected")
        return float(response[0][:-1])

    @property
    def is_set_on(self) -> bool:
        """
        Query the channel control bit "Set On".

        Returns:
            bool: True if the channel control bit is set on, False otherwise.

        Example:
            is_on = channel.is_set_on
            print(is_on)  # Example output: True
        """
        command = _get_mon_channel_command(self._channel, ":READ:VOLT:ON")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0][:-1]) == 1

    @property
    def is_set_emergency_off(self) -> bool:
        """
        Query the channel control bit "Set Emergency Off".

        Returns:
            bool: True if the channel control bit is set to Emergency Off, False otherwise.

        Example:
            is_emergency_off = channel.is_set_emergency_off
            print(is_emergency_off)  # Example output: False
        """
        command = _get_mon_channel_command(self._channel, ":READ:VOLT:EMCY")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return int(response[0][:-1]) == 1

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
        command = _get_mon_channel_command(self._channel, ":READ:CURR")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(
            response[0][:-1]
        )  # Remove the last character from the response (unit)

    @property
    def current_limit(self) -> float:
        """
        Query the current limit (Ilim) in Ampere.

        Returns:
            float: The current limit value.

        Example:
            limit = channel.current_limit
            print(limit)  # Example output: 5.00000E-3

        """
        command = _get_mon_channel_command(self._channel, ":READ:CURR:LIM")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(
            response[0][:-1]
        )  # Remove the last character from the response (unit)

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
        command = _get_mon_channel_command(self._channel, ":READ:CURR:NOM")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(
            response[0][:-1]
        )  # Remove the last character from the response (unit)

    @property
    def current_mode(self) -> float:
        """
        Query the configured channel current mode in Ampere.

        Returns:
            float: The current mode value.

        Example:
            mode = channel.current_mode
            print(mode)  # Example output: 2.00000E-3

        """
        command = _get_mon_channel_command(self._channel, ":READ:CURR:MODE")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(
            response[0][:-1]
        )  # Remove the last character from the response (unit)

    @property
    def current_mode_list(self) -> List[float]:
        """
        Query the available channel current modes as a list.

        Returns:
            List[float]: The list of available current modes.

        Example:
            modes = channel.current_mode_list
            print(modes)  # Example output: [6.0E-3, 4.0E-3, 2.0E-3]

        """
        command = _get_mon_channel_command(self._channel, ":READ:CURR:MODE:LIST")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        modes = [
            float(mode[:-1]) for mode in response
        ]  # Remove the last character from each mode (unit)
        return modes

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
        command = _get_mon_channel_command(self._channel, ":READ:CURR:BOUNDS")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(response[0][:-1])

    @property
    def current_ramp_speed(self) -> float:
        """
        Query the channel current ramp speed in Ampere/second.

        Returns:
            float: The channel current ramp speed.

        Example:
            speed = channel.current_ramp_speed
            print(speed)  # Example output: 2.0000E-3

        """
        command = _get_mon_channel_command(self._channel, ":READ:RAMP:CURR")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(response[0][:-3])

    @property
    def voltage_ramp_speed(self) -> float:
        """
        Query the channel voltage ramp speed in Volt/second.

        Returns:
            float: The channel voltage ramp speed.

        Example:
            speed = channel.voltage_ramp_speed
            print(speed)  # Example output: 0.25000E3

        """
        command = _get_mon_channel_command(self._channel, ":READ:RAMP:VOLT")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(response[0][:-3])

    @property
    def voltage_ramp_speed_minimum(self) -> float:
        """
        Query the channel voltage ramp speed minimum in Volt/second.

        Returns:
            float: The channel voltage ramp speed minimum.

        Example:
            speed_min = channel.voltage_ramp_speed_minimum
            print(speed_min)  # Example output: 0.00005E3

        """
        command = _get_mon_channel_command(self._channel, ":READ:RAMP:VOLT:MIN")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(response[0][:-3])

    @property
    def voltage_ramp_speed_maximum(self) -> float:
        """
        Query the channel voltage ramp speed maximum in Volt/second.

        Returns:
            float: The channel voltage ramp speed maximum.

        Example:
            speed_max = channel.voltage_ramp_speed_maximum
            print(speed_max)  # Example output: 1.20000E3

        """
        command = _get_mon_channel_command(self._channel, ":READ:RAMP:VOLT:MAX")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(response[0][:-3])

    @property
    def current_ramp_speed_minimum(self) -> float:
        """
        Query the channel current ramp speed minimum in Ampere/second.

        Returns:
            float: The channel current ramp speed minimum.

        Example:
            speed_min = channel.current_ramp_speed_minimum
            print(speed_min)  # Example output: 1.0000E-3

        """
        command = _get_mon_channel_command(self._channel, ":READ:RAMP:CURR:MIN")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(response[0][:-3])

    @property
    def current_ramp_speed_maximum(self) -> float:
        """
        Query the channel current ramp speed maximum in Ampere/second.

        Returns:
            float: The channel current ramp speed maximum.

        Example:
            speed_max = channel.current_ramp_speed_maximum
            print(speed_max)  # Example output: 6.0000E-3

        """
        command = _get_mon_channel_command(self._channel, ":READ:RAMP:CURR:MAX")
        response = _write_command(self._serial, command)
        if len(response) != 1:
            raise ValueError("Wrong number of values were received, one value expected")
        return float(response[0][:-3])
