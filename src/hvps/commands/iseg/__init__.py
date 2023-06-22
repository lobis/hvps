from __future__ import annotations
import re

"""
from .module import (
    _get_mon_module_command,
    _get_set_module_command,
)
"""

from .channel import (
    _get_mon_channel_command,
    _get_set_channel_command,
)

import logging
import serial


def _write_command(
    ser: serial.Serial, command: bytes, response: bool = True
) -> list[str] | None:
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

    # echo reading
    response_value = ser.readline()
    if response_value != command:
        raise ValueError(
            f"Invalid handshake echo response: {response_value}. expected {command}"
        )
    # response reading
    response_value = _parse_response(ser.readline())

    return response_value


def _parse_response(response: bytes) -> list[str]:
    """Parse the response from a device.

    Args:
        response (bytes): The response received from the device.
        bd (int | None, optional): The expected bd value. Defaults to None.

    Returns:
        str: The parsed value extracted from the response.

    Raises:
        ValueError: If the response is invalid, cannot be decoded, or does not match the expected pattern.
    """
    logger = logging.getLogger(__name__)
    logger.debug(f"Response: {response}")

    try:
        response: str = response.decode("ascii").strip()
    except UnicodeDecodeError:
        raise ValueError(f"Invalid response: {response}")

    return response.split(',')
