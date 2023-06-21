import serial

from ..commands.caen.channel import (
    _get_set_channel_command,
    _get_mon_channel_command,
)
from ..commands.caen import _parse_response
from ..utils import string_to_bit_array

from time import sleep


class Channel:
    """Represents a channel of a device.

    Args:
        _serial (serial.Serial): The serial connection to the device.
        bd (int): The bd value.
        channel (int): The channel number.
    """

    def __init__(self, _serial: serial.Serial, bd: int, channel: int):
        self._serial = _serial
        self._bd = bd
        self._channel = channel

    @property
    def bd(self) -> int:
        """The bd value of the channel.

        Returns:
            int: The bd value.
        """
        return self._bd

    @property
    def channel(self) -> int:
        """The channel number.

        Returns:
            int: The channel number.
        """
        return self._channel

    def wait_for_vset(self, timeout: float = 60.0, allowed_difference: float = 1.0):
        """Wait for the vset value to stabilize within a specified voltage difference.

        Args:
            timeout (float, optional): The maximum time to wait in seconds. Defaults to 60.0 seconds.
            allowed_difference (float, optional): The maximum voltage difference to consider as stabilized.
                Defaults to 1.0 V.

        Raises:
            TimeoutError: If the vset value does not stabilize within the specified timeout.

        """
        timedelta = 0.5  # 0.5 seconds
        t = 0.0
        while t < timeout:
            t += timedelta
            sleep(timedelta)
            if abs(self.vset - self.vmon) < abs(allowed_difference):
                return

        # Could not stabilize within the specified timeout
        raise TimeoutError(f"Could not stabilize vset within {timeout} seconds.")

    # Getters
    @property
    def vset(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "VSET"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def vmin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "VMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def vmax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "VMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def vdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "VDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def vmon(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "VMON"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def iset(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "ISET"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def imin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "IMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def imax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "IMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def isdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "ISDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def imon(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "IMON"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def imrange(self) -> bool:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "IMRANGE"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        if response not in ["HIGH", "LOW"]:
            raise ValueError(f"Unexpected response {response}")
        return response == "HIGH"

    @property
    def imdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "IMDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def maxv(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "MAXV"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def mvmin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "MVMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def mvmax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "MVMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def mvdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "MVDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def rup(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RUP"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rupmin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RUPMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rupmax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RUPMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rupdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RUPDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def rdw(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RDW"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rdwmin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RDWMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rdwmax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RDWMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rdwdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RDWDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def trip(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "TRIP"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def tripmin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "TRIPMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def tripmax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "TRIPMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def tripdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "TRIPDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def pdwn(self) -> str:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "PDWN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return str(response)

    @property
    def pol(self) -> str:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "POL"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return str(response)

    @property
    def stat(self) -> str:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "STAT"))
        response = _parse_response(self._serial.readline(), bd=self._bd)

        bit_array = string_to_bit_array("response")

        mapping = {
            "ON": bool(bit_array[0]),  # True: ON, False: OFF
            "RUP": bool(bit_array[1]),  # True: Channel Ramp UP
            "RDW": bool(bit_array[2]),  # True: Channel Ramp DOWN
            "OVC": bool(bit_array[3]),  # True: IMON >= ISET
            "OVV": bool(bit_array[4]),  # True: VMON > VSET + 2.5 V
            "UNV": bool(bit_array[5]),  # True: VMON < VSET – 2.5 V
            "MAXV": bool(bit_array[6]),  # True: VOUT in MAXV protection
            "TRIP": bool(
                bit_array[7]
            ),  # True: Ch OFF via TRIP (Imon >= Iset during TRIP)
            "OVP": bool(bit_array[8]),  # True: Output Power > Max
            "OVT": bool(bit_array[9]),  # True: TEMP > 105°C
            "DIS": bool(
                bit_array[10]
            ),  # True: Ch disabled (REMOTE Mode and Switch on OFF position)
            "KILL": bool(bit_array[11]),  # True: Ch in KILL via front panel
            "ILK": bool(bit_array[12]),  # True: Ch in INTERLOCK via front panel
            "NOCAL": bool(bit_array[13]),  # True: Calibration Error
            # TODO: qué es NC (Not Connected es la propuesta de chatGPT)
            # "NC": bool(bit_array[14])  # True: Not Connected
        }

        return str(mapping)

    # Setters
    @vset.setter
    def vset(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "VSET", value)
        )
        _ = _parse_response(self._serial.readline(), bd=self._bd)
        if self.vset != value:
            raise ValueError(f"Could not set VSET to {value}")

    @iset.setter
    def iset(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "ISET", value)
        )
        _ = _parse_response(self._serial.readline(), bd=self._bd)
        if self.iset != value:
            raise ValueError(f"Could not set ISET to {value}")

    @maxv.setter
    def maxv(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "MAXV", value)
        )
        _ = _parse_response(self._serial.readline(), bd=self._bd)
        if self.maxv != value:
            raise ValueError(f"Could not set MAXV to {value}")

    @rup.setter
    def rup(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "RUP", value)
        )
        _ = _parse_response(self._serial.readline(), bd=self._bd)
        if self.rup != value:
            raise ValueError(f"Could not set RUP to {value}")

    @rdw.setter
    def rdw(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "RDW", value)
        )
        _ = _parse_response(self._serial.readline(), bd=self._bd)
        if self.rdw != value:
            raise ValueError(f"Could not set RDW to {value}")

    @trip.setter
    def trip(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "TRIP", value)
        )
        _ = _parse_response(self._serial.readline(), bd=self._bd)
        if self.trip != value:
            raise ValueError(f"Could not set TRIP to {value}")

    @pdwn.setter
    def pdwn(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "PDWN", value)
        )
        _ = _parse_response(self._serial.readline(), bd=self._bd)
        if self.pdwn != value:
            raise ValueError(f"Could not set PDWN to {value}")

    @imrange.setter
    def imrange(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "IMRANGE", value)
        )
        _ = _parse_response(self._serial.readline(), bd=self._bd)
        if self.imrange != value:
            raise ValueError(f"Could not set IMRANGE to {value}")

    def on(self) -> None:
        """Turn on the channel."""
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "ON", None)
        )
        _ = _parse_response(self._serial.readline(), bd=self._bd)

    def off(self) -> None:
        """Turn off the channel."""
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "OFF", None)
        )
        _ = _parse_response(self._serial.readline(), bd=self._bd)
