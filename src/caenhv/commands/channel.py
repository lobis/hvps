from __future__ import annotations

_mon_channel_parameters = {
    "VSET": "Read out VSET value(XXXX.X V)",
    "VMIN": "Read out VSET minimum value(0 V)",
    "VMAX": "Read out VSET maximum value(8000.0 V)",
    "VDEC": "Read out VSET number of decimal digits",
    "VMON": "Read out VMON value(XXXX.X V)",
    "ISET": "Read out ISET value(XXXX.XX µA)",
    "IMIN": "Read out ISET minimum value(0 µA)",
    "IMAX": "Read out ISET maximum value(3000.00 µA)",
    "ISDEC": "Read out ISET number of decimal digits",
    "IMON": "Read out IMON value(XXXX.XX µA)",
    "IMRANGE": "Read out IMON RANGE value(HIGH / LOW)",
    "IMDEC": "Read out IMON number of decimal digits(2 HR, 3 LR)",
    "MAXV": "Read out MAXVSET value(XXXX V)",
    "MVMIN": "Read out MAXVSET minimum value(0 V)",
    "MVMAX": "Read out MAXVSET maximum value(8100 V)",
    "MVDEC": "Read out MAXVSET number of decimal digits",
    "RUP": "Read out RAMP UP value(XXX V/S)",
    "RUPMIN": "Read out RAMP UP minimum value(1 V/S)",
    "RUPMAX": "Read out RAMP UP maximum value(500 V/S)",
    "RUPDEC": "Read out RAMP UP number of decimal digits",
    "RDW": "Read out RAMP DOWN value(XXX V/S)",
    "RDWMIN": "Read out RAMP DOWN minimum value(1 V/S)",
    "RDWMAX": "Read out RAMP DOWN maximum value(500 V/S)",
    "RDWDEC": "Read out RAMP DOWN number of decimal digits",
    "TRIP": "Read out TRIP time value(XXXX.X S)",
    "TRIPMIN": "Read out TRIP time minimum value(0 S)",
    "TRIPMAX": "Read out TRIP time maximum value(1000.0 S)",
    "TRIPDEC": "Read out TRIP time number of decimal digits",
    "PDWN": "Read out POWER DOWN value(RAMP / KILL)",
    "POL": "Read out POLARITY value('+' / '-')",
    "STAT": "Read out Channel status value(XXXXX)",
}

_set_channel_parameters = {
    "VSET": "VAL:XXXX.X Set VSET value",
    "ISET": "VAL:XXXX.XX Set ISET value",
    "MAXV": "VAL:XXXX Set MAXVSET value",
    "RUP": "VAL:XXX Set RAMP UP value",
    "RDW": "VAL:XXX Set RAMP DOWN value",
    "TRIP": "VAL:XXXX.X Set TRIP time value",
    "PDWN": "VAL:RAMP/KILL Set POWER DOWN mode value",
    "IMRANGE": "VAL:HIGH/LOW Set IMON RANGE value",
    "ON": "Set Ch ON",
    "OFF": "Set Ch OFF",
}


def _get_mon_channel_command(bd: int, channel: int, parameter: str) -> bytes:
    parameter = parameter.upper()
    if parameter not in _mon_channel_parameters:
        raise ValueError(
            f"Invalid parameter '{parameter}'. Valid parameters are: {_set_channel_parameters.keys()}"
        )
    return f"$BD:{bd:02d},CMD:MON,CH:{channel:01d},PAR:{parameter}\r\n".encode("utf-8")


def _get_set_channel_command(
    bd: int, channel: int, parameter: str, value: str | int | float | None
) -> bytes:
    parameter = parameter.upper()
    if parameter not in _set_channel_parameters:
        raise ValueError(
            f"Invalid parameter '{parameter}'. Valid parameters are: {_set_channel_parameters.keys()}"
        )

    if parameter in ["ON", "OFF"]:
        if value is not None:
            raise ValueError(f"Parameter '{parameter}' does not accept a value")
        return f"$BD:{bd:02d},CMD:SET,CH:{channel:01d},PAR:{parameter}\r\n".encode(
            "utf-8"
        )
    elif parameter == "IMRANGE":
        if value not in ["HIGH", "LOW"]:
            raise ValueError(f"Parameter '{parameter}' only accepts 'HIGH' or 'LOW'")
    elif parameter == "PDWN":
        if value not in ["RAMP", "KILL"]:
            raise ValueError(f"Parameter '{parameter}' only accepts 'RAMP' or 'KILL'")

    return (
        f"$BD:{bd:02d},CMD:SET,CH:{channel:01d},PAR:{parameter},VAL:{value}\r\n".encode(
            "utf-8"
        )
    )
