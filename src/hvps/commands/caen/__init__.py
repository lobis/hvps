from __future__ import annotations
import re

import logging
import serial


def _write_command(
    ser: serial.Serial, bd: int, command: bytes, response: bool = True
) -> str | None:
    """Write a command to a device.

    Args:
        ser (Serial): The serial connection to the device.
        command (bytes): The command to write utf-8 encoded.
        response (bool, optional): Whether to wait for a response. Defaults to True.
    """
    logger = logging.getLogger(__name__)
    logger.debug(f"_write_command command: {command}")
    ser.write(command)
    if not response:
        return None

    bd_from_response, response_value = _parse_response(ser.readline())
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
    logger = logging.getLogger(__name__)
    logger.debug(f"Response: {response}")
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

    logger.debug(f"response parsing -> bd: {bd}, value: {value}")

    return bd, value
