from functools import cached_property

import serial

from ..commands.channel import _get_set_channel_command, _get_mon_channel_command
from ..commands import _parse_response

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
    def db(self) -> int:
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

    def wait_for_vset(
        self, timeout: float = 30.0, timedelta: float = 0.5, voltage_diff: float = 0.5
    ) -> bool:
        """Wait for the vset value to stabilize within a specified voltage difference.

        Args:
            timeout (float, optional): The maximum time to wait in seconds. Defaults to 30.0.
            timedelta (float, optional): The time interval between checks in seconds. Defaults to 0.5.
            voltage_diff (float, optional): The maximum voltage difference to consider as stabilized. Defaults to 0.5.

        Returns:
            bool: True if the vset value stabilized within the specified voltage difference, False otherwise.
        """
        t = 0.0
        while t < timeout:
            t += timedelta
            sleep(timedelta)
            if abs(self.vset - self.vmon) < abs(voltage_diff):
                return True
        return False

    # Getters
    @property
    def vset(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "VSET"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def vmin(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "VMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def vmax(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "VMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def vdec(self) -> int:
        self.write(_get_mon_channel_command(self._bd, self._channel, "VDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def vmon(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "VMON"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def iset(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "ISET"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def imin(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "IMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def imax(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "IMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def isdec(self) -> int:
        self.write(_get_mon_channel_command(self._bd, self._channel, "ISDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def imon(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "IMON"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def imrange(self) -> bool:
        self.write(_get_mon_channel_command(self._bd, self._channel, "IMRANGE"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        if response not in ["HIGH", "LOW"]:
            raise ValueError(f"Unexpected response {response}")
        return response == "HIGH"

    @property
    def imdec(self) -> int:
        self.write(_get_mon_channel_command(self._bd, self._channel, "IMDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def maxv(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "MAXV"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def mvmin(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "MVMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def mvmax(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "MVMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def mvdec(self) -> int:
        self.write(_get_mon_channel_command(self._bd, self._channel, "MVDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def rup(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "RUP"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rupmin(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "RUPMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rupmax(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "RUPMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rupdec(self) -> int:
        self.write(_get_mon_channel_command(self._bd, self._channel, "RUPDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def rdw(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "RDW"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rdwmin(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "RDWMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rdwmax(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "RDWMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def rdwdec(self) -> int:
        self.write(_get_mon_channel_command(self._bd, self._channel, "RDWDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def trip(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "TRIP"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def tripmin(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "TRIPMIN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def tripmax(self) -> float:
        self.write(_get_mon_channel_command(self._bd, self._channel, "TRIPMAX"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return float(response)

    @property
    def tripdec(self) -> int:
        self.write(_get_mon_channel_command(self._bd, self._channel, "TRIPDEC"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return int(response)

    @property
    def pdwn(self) -> str:
        self.write(_get_mon_channel_command(self._bd, self._channel, "PDWN"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return str(response)

    @property
    def pol(self) -> str:
        self.write(_get_mon_channel_command(self._bd, self._channel, "POL"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        return str(response)

    @property
    def stat(self) -> str:
        self.write(_get_mon_channel_command(self._bd, self._channel, "STAT"))
        response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: parse status
        return str(response)

    # Setters
    @vset.setter
    def vset(self, value: float) -> None:
        self.write(_get_set_channel_command(self._bd, self._channel, "VSET", value))
        response = _parse_response(self._serial.readline(), bd=self._bd)

    @iset.setter
    def iset(self, value: float) -> None:
        self.write(_get_set_channel_command(self._bd, self._channel, "ISET", value))
        response = _parse_response(self._serial.readline(), bd=self._bd)

    @maxv.setter
    def maxv(self, value: float) -> None:
        self.write(_get_set_channel_command(self._bd, self._channel, "MAXV", value))
        response = _parse_response(self._serial.readline(), bd=self._bd)

    @rup.setter
    def rup(self, value: float) -> None:
        self.write(_get_set_channel_command(self._bd, self._channel, "RUP", value))
        response = _parse_response(self._serial.readline(), bd=self._bd)

    @rdw.setter
    def rdw(self, value: float) -> None:
        self.write(_get_set_channel_command(self._bd, self._channel, "RDW", value))
        response = _parse_response(self._serial.readline(), bd=self._bd)

    @trip.setter
    def trip(self, value: float) -> None:
        self.write(_get_set_channel_command(self._bd, self._channel, "TRIP", value))
        response = _parse_response(self._serial.readline(), bd=self._bd)

    @pdwn.setter
    def pdwn(self, value: float) -> None:
        self.write(_get_set_channel_command(self._bd, self._channel, "PDWN", value))
        response = _parse_response(self._serial.readline(), bd=self._bd)

    @imrange.setter
    def imrange(self, value: float) -> None:
        self.write(_get_set_channel_command(self._bd, self._channel, "IMRANGE", value))
        response = _parse_response(self._serial.readline(), bd=self._bd)

    def on(self) -> None:
        """Turn on the channel."""
        self.write(_get_set_channel_command(self._bd, self._channel, "ON", None))
        response = _parse_response(self._serial.readline(), bd=self._bd)

    def off(self) -> None:
        """Turn off the channel."""
        self.write(_get_set_channel_command(self._bd, self._channel, "OFF", None))
        response = _parse_response(self._serial.readline(), bd=self._bd)
