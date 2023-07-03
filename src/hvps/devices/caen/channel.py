from ...commands.caen.channel import (
    _get_set_channel_command,
    _get_mon_channel_command,
)
from ...commands.caen import _write_command
from ...utils import string_number_to_bit_array
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
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "VSET"),
        )
        return float(response)

    @property
    def voltage_set(self) -> float:
        return self.vset

    @property
    def vmin(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "VMIN"),
        )
        return float(response)

    @property
    def vmax(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "VMAX"),
        )
        return float(response)

    @property
    def vdec(self) -> int:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "VDEC"),
        )
        return int(response)

    @property
    def vmon(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "VMON"),
        )
        return float(response)

    @property
    def iset(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "ISET"),
        )
        return float(response)

    @property
    def imin(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "IMIN"),
        )
        return float(response)

    @property
    def imax(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "IMAX"),
        )
        return float(response)

    @property
    def isdec(self) -> int:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "ISDEC"),
        )
        return int(response)

    @property
    def imon(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "IMON"),
        )
        return float(response)

    @property
    def imrange(self) -> bool:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "IMRANGE"),
        )
        if response not in ["HIGH", "LOW"]:
            raise ValueError(f"Unexpected response {response}")
        return response == "HIGH"

    @property
    def imdec(self) -> int:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "IMDEC"),
        )
        return int(response)

    @property
    def maxv(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "MAXV"),
        )
        return float(response)

    @property
    def mvmin(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "MVMIN"),
        )
        return float(response)

    @property
    def mvmax(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "MVMAX"),
        )
        return float(response)

    @property
    def mvdec(self) -> int:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "MVDEC"),
        )
        return int(response)

    @property
    def rup(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "RUP"),
        )
        return float(response)

    @property
    def rupmin(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "RUPMIN"),
        )
        return float(response)

    @property
    def rupmax(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "RUPMAX"),
        )
        return float(response)

    @property
    def rupdec(self) -> int:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "RUPDEC"),
        )
        return int(response)

    @property
    def rdw(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "RDW"),
        )
        return float(response)

    @property
    def rdwmin(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "RDWMIN"),
        )
        return float(response)

    @property
    def rdwmax(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "RDWMAX"),
        )
        return float(response)

    @property
    def rdwdec(self) -> int:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "RDWDEC"),
        )
        return int(response)

    @property
    def trip(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "TRIP"),
        )
        return float(response)

    @property
    def tripmin(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "TRIPMIN"),
        )
        return float(response)

    @property
    def tripmax(self) -> float:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "TRIPMAX"),
        )
        return float(response)

    @property
    def tripdec(self) -> int:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "TRIPDEC"),
        )
        return int(response)

    @property
    def pdwn(self) -> str:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "PDWN"),
        )
        return str(response)

    @property
    def pol(self) -> str:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "POL"),
        )
        if response not in ["+", "-"]:
            raise ValueError(f"Invalid polarity: {response}")
        return str(response)

    def polarity_positive(self) -> bool:
        return self.pol == "+"

    def polarity_negative(self) -> bool:
        return self.pol == "-"

    @property
    def stat(self) -> dict:
        response = _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_mon_channel_command(self._bd, self._channel, "STAT"),
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
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(self._bd, self._channel, "VSET", value),
        )
        if self.vset != value:
            raise ValueError(f"Could not set VSET to {value}")

    @iset.setter
    def iset(self, value: float) -> None:
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(self._bd, self._channel, "ISET", value),
        )
        if self.iset != value:
            raise ValueError(f"Could not set ISET to {value}")

    @maxv.setter
    def maxv(self, value: float) -> None:
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(self._bd, self._channel, "MAXV", value),
        )
        if self.maxv != value:
            raise ValueError(f"Could not set MAXV to {value}")

    @rup.setter
    def rup(self, value: float) -> None:
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(self._bd, self._channel, "RUP", value),
        )
        if self.rup != value:
            raise ValueError(f"Could not set RUP to {value}")

    @rdw.setter
    def rdw(self, value: float) -> None:
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(self._bd, self._channel, "RDW", value),
        )
        if self.rdw != value:
            raise ValueError(f"Could not set RDW to {value}")

    @trip.setter
    def trip(self, value: float) -> None:
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(self._bd, self._channel, "TRIP", value),
        )
        if self.trip != value:
            raise ValueError(f"Could not set TRIP to {value}")

    @pdwn.setter
    def pdwn(self, value: float) -> None:
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(self._bd, self._channel, "PDWN", value),
        )
        if self.pdwn != value:
            raise ValueError(f"Could not set PDWN to {value}")

    @imrange.setter
    def imrange(self, value: float) -> None:
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(self._bd, self._channel, "IMRANGE", value),
        )
        if self.imrange != value:
            raise ValueError(f"Could not set IMRANGE to {value}")

    def turn_on(self) -> None:
        """Turn on the channel."""
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(self._bd, self._channel, "ON", None),
        )

    def turn_off(self) -> None:
        """Turn off the channel."""
        _write_command(
            ser=self._serial,
            logger=self._logger,
            bd=self._bd,
            command=_get_set_channel_command(self._bd, self._channel, "OFF", None),
        )
