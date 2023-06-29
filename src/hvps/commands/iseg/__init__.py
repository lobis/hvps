from __future__ import annotations
from typing import List

import logging
import serial
import re


def _write_command(
    ser: serial.Serial,
    command: bytes,
    expected_response_type: type | None,
    response: bool = True,
) -> List[str] | None:
    """Write a command to a device and parses the response.

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
    response_value = _parse_response(ser.readline(), expected_response_type)

    return response_value


def _parse_response(response: bytes, expected_response_type: type | None) -> List[str]:
    """Parse the response from a device.

    Args:
        response (bytes): The response received from the device.

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

    if expected_response_type == float or expected_response_type == List[float]:
        # pattern for a float in scientific notation followed or not by units
        pattern = (
            r"^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?(\s*[a-zA-Z]+(/+[a-zA-Z]+)?)?$"
        )
    elif expected_response_type == int or expected_response_type == List[int]:
        pattern = r"^[-+]?\d+$"
    elif expected_response_type == str or expected_response_type == List[str]:
        pattern = r"^[\x00-\x7F]+$"
    elif expected_response_type is None:
        return response.split(",")
    else:
        raise ValueError(
            f"expected value type of {response}, {expected_response_type}, is not float, int or str"
        )

    split_response = response.split(",")

    for r in split_response:
        match = re.match(pattern, r)
        if not match:
            raise ValueError(
                f"Invalid response: {response}, can't be identified as a {expected_response_type}, missmatch in RE"
            )

    return split_response
