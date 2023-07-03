from __future__ import annotations
import re

import logging
import serial


def _write_command(
    ser: serial.Serial,
    logger: logging.Logger,
    bd: int,
    command: bytes,
    response: bool = True,
) -> str | None:
    logger.debug(f"Sending command: {command}")
    if not ser.is_open:
        logger.error("Serial port is not open")
        raise serial.SerialException("Serial port is not open")

    ser.write(command)
    if not response:
        logger.warning(
            "Calling _write_command without expecting a response. Manual readout of the response is required."
        )
        return None

    response = ser.readline()
    logger.debug(f"Received response: {response}")
    bd_from_response, response_value = _parse_response(response)
    if bd_from_response != bd:
        raise ValueError(
            f"Invalid response: {response_value}. Expected board number {bd}, got {bd_from_response}"
        )

    return response_value


def _parse_response(response: bytes) -> (int, str):
    """Parse the response from a device.

    Args:
        response (bytes): The response received from the device. (e.g. b"#BD:01,CMD:OK,VAL:42\r\n").

    Returns:
        (int, str): The board number and the value of the response.

    Raises:
        ValueError: If the response is invalid, cannot be decoded, or does not match the expected pattern.
    """

    if response == b"":
        raise ValueError(
            "Empty response. There was no response from the device. Check that the device is connected and correctly "
            "configured (baudrate)."
        )

    try:
        response: str = response.decode("utf-8").strip()
    except UnicodeDecodeError:
        raise ValueError(f"Invalid response: {response}")

    regex = re.compile(r"^#BD:(\d{2}),CMD:OK(?:,VAL:(.+))?$")
    match = regex.match(response)
    if match is None:
        raise ValueError(f"Invalid response: '{response}'. Could not match regex")
    bd = int(match.group(1))
    value: str | None = match.group(2) if match.group(2) else None

    return bd, value
