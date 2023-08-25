from __future__ import annotations
import inspect

from hvps.utils import check_command_input

from ...commands.caen.channel import (
    _get_set_channel_command,
    _get_mon_channel_command,
    _MON_CHANNEL_COMMANDS,
    _SET_CHANNEL_COMMANDS,
)

from ...utils import string_number_to_bit_array, check_command_output_and_convert
from ..channel import Channel as BaseChannel

from time import sleep


class Channel(BaseChannel):
    def __init__(self, *args, bd: int, **kwargs):
        super().__init__(*args, **kwargs)
        self._bd = bd

    def _write_command_read_response_channel_mon(
        self, method_name: str
    ) -> str | int | float | None:
        command = _MON_CHANNEL_COMMANDS[method_name]["command"]
        check_command_input(_MON_CHANNEL_COMMANDS, method_name)
        response = self._write_command_read_response(
            bd=self.bd,
            command=_get_mon_channel_command(
                bd=self.bd, channel=self.channel, command=command
            ),
        )
        return check_command_output_and_convert(
            command, None, response, _MON_CHANNEL_COMMANDS
        )

    def _write_command_read_response_channel_set(
        self, method_name: str, value: str | int | float | None
    ) -> str | None:
        command = _SET_CHANNEL_COMMANDS[method_name]["command"]
        check_command_input(_SET_CHANNEL_COMMANDS, method_name, value)
        return self._write_command_read_response(
            bd=self.bd,
            command=_get_set_channel_command(
                bd=self.bd, channel=self.channel, command=command, value=value
            ),
        )

    @property
    def bd(self) -> int:
        """The bd value of the channel.

        Returns:
            int: The bd value.
        """
        return self._bd

    def wait_for_vset(self, timeout: float = 60.0):
        """Wait for the vset value to stabilize within a specified voltage difference.

        Args:
            timeout (float, optional): The maximum time to wait in seconds. Defaults to 60.0 seconds.

        Raises:
            TimeoutError: If the vset value does not stabilize within the specified timeout.

        """
        timedelta = 0.5  # 0.5 seconds
        t = 0.0
        while t < timeout:
            t += timedelta
            sleep(timedelta)
            if self.voltage_target_reached:
                return

        # Could not stabilize within the specified timeout
        raise TimeoutError(f"Could not stabilize vset within {timeout} seconds.")

    # Getters
    @property
    def vset(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def voltage_set(self) -> float:
        return self.vset

    @property
    def vmin(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def vmax(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def vdec(self) -> int:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def vmon(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def iset(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def imin(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def imax(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def isdec(self) -> int:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def imon(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def imrange(self) -> str:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    def imrange_high(self) -> bool:
        return self.imrange == "HIGH"

    def imrange_low(self) -> bool:
        return self.imrange == "LOW"

    @property
    def imdec(self) -> int:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def maxv(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def mvmin(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def mvmax(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def mvdec(self) -> int:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def rup(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def rupmin(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def rupmax(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def rupdec(self) -> int:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def rdw(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def rdwmin(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def rdwmax(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def rdwdec(self) -> int:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def trip(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def tripmin(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def tripmax(self) -> float:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def tripdec(self) -> int:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def pdwn(self) -> str:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    @property
    def pol(self) -> str:
        return self._write_command_read_response_channel_mon(
            inspect.currentframe().f_code.co_name
        )

    def polarity_positive(self) -> bool:
        return self.pol == "+"

    def polarity_negative(self) -> bool:
        return self.pol == "-"

    @property
    def stat(self) -> dict:
        command = _MON_CHANNEL_COMMANDS[inspect.currentframe().f_code.co_name]
        response = self._write_command_read_response(
            bd=self.bd,
            command=_get_mon_channel_command(
                bd=self.bd, channel=self.channel, command=command
            ),
        )
        # TODO: check_command_output_and_convert returns an int so make string_number_to_bit_array take an int
        check_command_output_and_convert(command, None, response, _MON_CHANNEL_COMMANDS)
        bit_array = string_number_to_bit_array(response)

        return {
            "ON": bit_array[0],  # True: ON, False: OFF
            "RUP": bit_array[1],  # True: Channel Ramp UP
            "RDW": bit_array[2],  # True: Channel Ramp DOWN
            "OVC": bit_array[3],  # True: IMON >= ISET
            "OVV": bit_array[4],  # True: VMON > VSET + 2.5 V
            "UNV": bit_array[5],  # True: VMON < VSET – 2.5 V
            "MAXV": bit_array[6],  # True: VOUT in MAXV protection
            "TRIP": bit_array[7],  # True: Ch OFF via TRIP (Imon >= Iset during TRIP)
            "OVP": bit_array[8],  # True: Output Power > Max
            "OVT": bit_array[9],  # True: TEMP > 105°C
            "DIS": bit_array[
                10
            ],  # True: Ch disabled (REMOTE Mode and Switch on OFF position)
            "KILL": bit_array[11],  # True: Ch in KILL via front panel
            "ILK": bit_array[12],  # True: Ch in INTERLOCK via front panel
            "NOCAL": bit_array[13],  # True: Calibration Error
            # "NC": bit_array[14]  # True: Not Connected
        }

    @property
    def voltage_target_reached(self) -> bool:
        stat = self.stat
        return not stat["OVV"] and not stat["UNV"]

    @property
    def on(self) -> bool:
        return self.stat["ON"]

    @property
    def off(self) -> bool:
        return not self.on

    @property
    def kill(self) -> bool:
        return self.stat["KILL"]

    # Setters
    @vset.setter
    def vset(self, value: float) -> None:
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name, value=value
        )
        if self.vset != value:
            raise ValueError(f"Could not set VSET to {value}")

    @iset.setter
    def iset(self, value: float) -> None:
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name, value=value
        )
        if self.iset != value:
            raise ValueError(f"Could not set ISET to {value}")

    @maxv.setter
    def maxv(self, value: float) -> None:
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name, value=value
        )
        if self.maxv != value:
            raise ValueError(f"Could not set MAXV to {value}")

    @rup.setter
    def rup(self, value: float) -> None:
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name, value=value
        )
        if self.rup != value:
            raise ValueError(f"Could not set RUP to {value}")

    @rdw.setter
    def rdw(self, value: float) -> None:
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name, value=value
        )
        if self.rdw != value:
            raise ValueError(f"Could not set RDW to {value}")

    @trip.setter
    def trip(self, value: float) -> None:
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name, value=value
        )
        if self.trip != value:
            raise ValueError(f"Could not set TRIP to {value}")

    @pdwn.setter
    def pdwn(self, value: float) -> None:
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name, value=value
        )
        if self.pdwn != value:
            raise ValueError(f"Could not set PDWN to {value}")

    @imrange.setter
    def imrange(self, value: float) -> None:
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name, value=value
        )
        if self.imrange != value:
            raise ValueError(f"Could not set IMRANGE to {value}")

    def turn_on(self) -> None:
        """Turn on the channel."""
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name, value=None
        )

    def turn_off(self) -> None:
        """Turn off the channel."""
        self._write_command_read_response_channel_set(
            method_name=inspect.currentframe().f_code.co_name, value=None
        )
