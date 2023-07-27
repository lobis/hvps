from __future__ import annotations
from typing import List

import logging
import serial
import re


# TODO: change name to arg response
def _write_command(
    ser: serial.Serial,
    logger: logging.Logger,
    command: bytes,
    expected_response_type: type | None,
    response: bool = True,
) -> str | List[str] | None:
    """
    Implements the protocol of the HVPS for sending a command and parses its response

    Args:
        ser: The serial port.
        logger: The logger.
        command: The command to send.
        expected_response_type: The expected type of the response.
        response: Whether to expect a response or not.

    Throws:
        ValueError: If the response is invalid, cannot be decoded, or does not match the expected pattern.

    Returns:
        str | List[str] | None: The parsed response.
    """
    logger.debug(f"Send command: {command}")
    ser.write(command)
    if not response:
        return None

    # echo reading
    response = ser.readline()
    logger.debug(f"Received response: {response}")
    if response != command:
        raise ValueError(
            f"Invalid handshake echo response: {response}. expected {command}"
        )

    # response reading
    response = ser.readline()
    response = _parse_response(response, expected_response_type)

    return response


def _parse_response(
    response: bytes, expected_response_type: type | None
) -> str | List[str]:
    """Parse the response from a device.

    Args:
        response (bytes): The response received from the device.

    Returns:
        str: The parsed value extracted from the response.

    Raises:
        ValueError: If the response is invalid, cannot be decoded, or does not match the expected pattern.
    """

    try:
        response = response.decode("ascii").strip()
    except UnicodeDecodeError:
        raise ValueError(f"Invalid response: {response}")

    if expected_response_type == float or expected_response_type == List[float]:
        # pattern for a float in scientific notation followed or not by units
        pattern = (
            r"^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?(\s*[a-zA-Z%]+(/+[a-zA-Z]+)?)?$"
        )
    elif expected_response_type == int or expected_response_type == List[int]:
        pattern = r"^[-+]?\d+(\s*[a-zA-Z]+(/+[a-zA-Z]+)?)?$"
    elif expected_response_type == str or expected_response_type == List[str]:
        pattern = r"^[\x00-\x7F]+$"
    elif expected_response_type is None:
        split_response = response.split(",")
        if len(split_response) == 1:
            return split_response[0]
        return split_response
    else:
        raise ValueError(
            f"expected value type of {response}, {expected_response_type}, is not float, int or str"
        )

    split_response = response.split(",")
    split_response = [s for s in split_response if not s == ""]
    for r in split_response:
        match = re.match(pattern, r)
        if not match:
            raise ValueError(
                f"Invalid response: {response}, can't be identified as a {expected_response_type}, missmatch in RE"
            )
    if len(split_response) == 1:
        return split_response[0]
    return split_response
