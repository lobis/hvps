from functools import cached_property

import serial

from ..commands.channel import _get_set_channel_command, _get_mon_channel_command
from ..commands import _parse_response

from time import sleep


class Channel:
    def __init__(self, _serial: serial.Serial, bd: int, channel: int):
        self._serial = _serial
        self._bd = bd
        self._channel = channel

    @property
    def db(self) -> int:
        return self._bd

    @property
    def channel(self) -> int:
        return self._channel

    def wait_for_vset(self, timeout: float = 30.0, timedelta: float = 0.5, voltage_diff: float = 0.5) -> bool:
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
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "VSET"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def vset(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "VSET"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def vmin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "VMIN"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def vmax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "VMAX"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def vdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "VDEC"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return int(response)

    @property
    def vmon(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "VMON"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def iset(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "ISET"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def imin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "IMIN"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def imax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "IMAX"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def isdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "ISDEC"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return int(response)

    @property
    def imon(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "IMON"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def imrange(self) -> bool:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "IMRANGE"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        if response not in ["HIGH", "LOW"]:
            raise ValueError(f"Unexpected response {response}")
        return response == "HIGH"

    @property
    def imdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "IMDEC"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return int(response)

    @property
    def maxv(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "MAXV"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def mvmin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "MVMIN"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def mvmax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "MVMAX"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def mvdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "MVDEC"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return int(response)

    @property
    def rup(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RUP"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def rupmin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RUPMIN"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def rupmax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RUPMAX"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def rupdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RUPDEC"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return int(response)

    @property
    def rdw(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RDW"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def rdwmin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RDWMIN"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def rdwmax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RDWMAX"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def rdwdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "RDWDEC"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return int(response)

    @property
    def trip(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "TRIP"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def tripmin(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "TRIPMIN"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def tripmax(self) -> float:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "TRIPMAX"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return float(response)

    @property
    def tripdec(self) -> int:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "TRIPDEC"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return int(response)

    @property
    def pdwn(self) -> str:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "PDWN"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return str(response)

    @property
    def pol(self) -> str:
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "POL"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return str(response)

    @property
    def stat(self) -> str:
        # TODO: parse status
        self._serial.write(_get_mon_channel_command(self._bd, self._channel, "STAT"))
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
        # TODO: handle error code
        return str(response)

    # Setters
    @vset.setter
    def vset(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "VSET", value)
        )
        code, response = _parse_response(self._serial.readline(), bd=self._bd)

    @iset.setter
    def iset(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "ISET", value)
        )
        code, response = _parse_response(self._serial.readline(), bd=self._bd)

    @maxv.setter
    def maxv(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "MAXV", value)
        )
        code, response = _parse_response(self._serial.readline(), bd=self._bd)

    @rup.setter
    def rup(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "RUP", value)
        )
        code, response = _parse_response(self._serial.readline(), bd=self._bd)

    @rdw.setter
    def rdw(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "RDW", value)
        )
        code, response = _parse_response(self._serial.readline(), bd=self._bd)

    @trip.setter
    def trip(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "TRIP", value)
        )
        code, response = _parse_response(self._serial.readline(), bd=self._bd)

    @pdwn.setter
    def pdwn(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "PDWN", value)
        )
        code, response = _parse_response(self._serial.readline(), bd=self._bd)

    @imrange.setter
    def imrange(self, value: float) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "IMRANGE", value)
        )
        code, response = _parse_response(self._serial.readline(), bd=self._bd)

    def on(self) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "ON", None)
        )
        code, response = _parse_response(self._serial.readline(), bd=self._bd)

    def off(self) -> None:
        self._serial.write(
            _get_set_channel_command(self._bd, self._channel, "OFF", None)
        )
        code, response = _parse_response(self._serial.readline(), bd=self._bd)
