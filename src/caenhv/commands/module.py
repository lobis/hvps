from __future__ import annotations
import re

_mon_module_parameters = {
    "BDNAME": "Read out module name ( N1471 )",
    "BDNCH": "Read out number of Channels present ( 4 )",
    "BDFREL": "Read out Firmware Release ( XX.X )",
    "BDSNUM": "Read out value serial number ( XXXXX )",
    "BDILK": "Read out INTERLOCK status ( YES/NO )",
    "BDILKM": "Read out INTERLOCK mode ( OPEN/CLOSED )",
    "BDCTR": "Read out Control Mode (LOCAL / REMOTE )",
    "BDTERM": "Read out LOCAL BUS Termination status ( ON/OFF )",
    "BDALARM": "Read out Board Alarm status value ( XXXXX )",
}

_set_module_parameters = {
    "BDILKM": "VAL:OPEN/CLOSED Set Interlock Mode",
    "BDCLR": "Clear alarm signal",
}


def _get_mon_module_command(bd: int, parameter: str) -> bytes:
    parameter = parameter.upper()
    if parameter not in _mon_module_parameters:
        raise ValueError(
            f"Invalid parameter '{parameter}'. Valida parameters are: {_mon_module_parameters.keys()}"
        )
    return f"$BD:{bd:02d},CMD:MON,PAR:{parameter}\r\n".encode("utf-8")


def _get_set_module_command(bd: int, parameter: str, value: str | int | float) -> bytes:
    parameter = parameter.upper()
    if parameter not in _set_module_parameters:
        raise ValueError(
            f"Invalid parameter '{parameter}'. Valida parameters are: {_set_module_parameters.keys()}"
        )
    return f"$BD:{bd:02d},CMD:SET,PAR:{parameter},VAL:{value}\r\n".encode("utf-8")
