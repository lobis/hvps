from __future__ import annotations
import re

from src.hvps.commands.caen.module import (
    _get_mon_module_command,
    _get_set_module_command,
)
from src.hvps.commands.caen.channel import (
    _get_mon_channel_command,
    _get_set_channel_command,
)

import logging


def _parse_response(response: bytes, bd: int | None = None) -> str:
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
        response: str = response.decode("utf-8").strip()
    except UnicodeDecodeError:
        raise ValueError(f"Invalid response: {response}")

    regex = re.compile(r"^#BD:(\d\d),CMD:OK,VAL:(.+)$")
    match = regex.match(response)
    if match is None:
        raise ValueError(f"Invalid response: '{response}'. Could not match regex")
    bd_from_response = int(match.group(1))
    if bd is not None and bd != bd_from_response:
        message = (
            f"Invalid response: '{response}'. Mismatched bd: {bd_from_response} != {bd}"
        )
        raise ValueError(message)

    value: str = match.group(2)
    logger.debug(f"Response result: {response} -> {value}")
    return value
