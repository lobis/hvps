import inspect

from ...commands.caen.channel import (
    _get_set_channel_command,
    _get_mon_channel_command,
    _MON_CHANNEL_COMMANDS,
)
from ...commands.caen import _write_command
from ...utils import string_number_to_bit_array, check_command_output_and_convert
from ..channel import Channel as BaseChannel

from time import sleep


class Channel(BaseChannel):
    def __init__(self, *args, bd: int, **kwargs):
        super().__init__(*args, **kwargs)
        self._bd = bd

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
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def voltage_set(self) -> float:
        return self.vset

    @property
    def vmin(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def vmax(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def vdec(self) -> int:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def vmon(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def iset(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def imin(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def imax(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def isdec(self) -> int:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def imon(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def imrange(self) -> str:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    def imrange_high(self) -> bool:
        return self.imrange == "HIGH"

    def imrange_low(self) -> bool:
        return self.imrange == "LOW"

    @property
    def imdec(self) -> int:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def maxv(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def mvmin(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def mvmax(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def mvdec(self) -> int:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def rup(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def rupmin(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def rupmax(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def rupdec(self) -> int:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def rdw(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def rdwmin(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def rdwmax(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def rdwdec(self) -> int:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def trip(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def tripmin(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def tripmax(self) -> float:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def tripdec(self) -> int:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def pdwn(self) -> str:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    @property
    def pol(self) -> str:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        if response not in ["+", "-"]:
            raise ValueError(f"Invalid polarity: {response}")
        return check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )

    def polarity_positive(self) -> bool:
        return self.pol == "+"

    def polarity_negative(self) -> bool:
        return self.pol == "-"

    @property
    def stat(self) -> dict:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _mon_channel_methods_to_commands[method_name]
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, command_name),
        )
        # TODO: check_command_output_and_convert returns an int so make string_number_to_bit_array take an int
        check_command_output_and_convert(
            command_name, None, response, _MON_CHANNEL_COMMANDS
        )
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
        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_channel_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(
                self._bd, self._channel, command_name, value
            ),
        )
        if self.vset != value:
            raise ValueError(f"Could not set VSET to {value}")

    @iset.setter
    def iset(self, value: float) -> None:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_channel_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(
                self._bd, self._channel, command_name, value
            ),
        )
        if self.iset != value:
            raise ValueError(f"Could not set ISET to {value}")

    @maxv.setter
    def maxv(self, value: float) -> None:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_channel_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(
                self._bd, self._channel, command_name, value
            ),
        )
        if self.maxv != value:
            raise ValueError(f"Could not set MAXV to {value}")

    @rup.setter
    def rup(self, value: float) -> None:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_channel_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(
                self._bd, self._channel, command_name, value
            ),
        )
        if self.rup != value:
            raise ValueError(f"Could not set RUP to {value}")

    @rdw.setter
    def rdw(self, value: float) -> None:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_channel_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(
                self._bd, self._channel, command_name, value
            ),
        )
        if self.rdw != value:
            raise ValueError(f"Could not set RDW to {value}")

    @trip.setter
    def trip(self, value: float) -> None:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_channel_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(
                self._bd, self._channel, command_name, value
            ),
        )
        if self.trip != value:
            raise ValueError(f"Could not set TRIP to {value}")

    @pdwn.setter
    def pdwn(self, value: float) -> None:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_channel_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(
                self._bd, self._channel, command_name, value
            ),
        )
        if self.pdwn != value:
            raise ValueError(f"Could not set PDWN to {value}")

    @imrange.setter
    def imrange(self, value: float) -> None:
        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_channel_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(
                self._bd, self._channel, command_name, value
            ),
        )
        if self.imrange != value:
            raise ValueError(f"Could not set IMRANGE to {value}")

    def turn_on(self) -> None:
        """Turn on the channel."""
        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_channel_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(
                self._bd, self._channel, command_name, None
            ),
        )

    def turn_off(self) -> None:
        """Turn off the channel."""
        method_name = inspect.currentframe().f_code.co_name
        command_name = _set_channel_methods_to_commands[method_name]
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(
                self._bd, self._channel, command_name, None
            ),
        )


_mon_channel_methods_to_commands = {
    "vset": "VSET",
    "vmin": "VMIN",
    "vmax": "VMAX",
    "vdec": "VDEC",
    "vmon": "VMON",
    "iset": "ISET",
    "imin": "IMIN",
    "imax": "IMAX",
    "isdec": "ISDEC",
    "imon": "IMON",
    "imrange": "IMRANGE",
    "imdec": "IMDEC",
    "maxv": "MAXV",
    "mvmin": "MVMIN",
    "mvmax": "MVMAX",
    "mvdec": "MVDEC",
    "rup": "RUP",
    "rupmin": "RUPMIN",
    "rupmax": "RUPMAX",
    "rupdec": "RUPDEC",
    "rdw": "RDW",
    "rdwmin": "RDWMIN",
    "rdwmax": "RDWMAX",
    "rdwdec": "RDWDEC",
    "trip": "TRIP",
    "tripmin": "TRIPMIN",
    "tripmax": "TRIPMAX",
    "tripdec": "TRIPDEC",
    "pdwn": "PDWN",
    "pol": "POL",
    "stat": "STAT",
}
_set_channel_methods_to_commands = {
    "vset": "VSET",
    "iset": "ISET",
    "maxv": "MAXV",
    "rup": "RUP",
    "rdw": "RDW",
    "trip": "TRIP",
    "pdwn": "PDWN",
    "imrange": "IMRANGE",
    "turn_on": "ON",
    "turn_off": "OFF",
}
