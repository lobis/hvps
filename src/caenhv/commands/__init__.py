from __future__ import annotations
import re

from .module import _get_set_module_command, _get_mon_module_command

import logging


def _parse_response(response: bytes, bd: int | None = None) -> tuple[bool, str]:
    logger = logging.getLogger(__name__)
    logger.debug(f"Response: {response}")

    try:
        response: str = response.decode("utf-8").strip()
    except UnicodeDecodeError:
        message = f"Error decoding response: '{response}'"
        logger.error(message)
        return False, message

    regex = re.compile(r"^#BD:(\d\d),CMD:OK,VAL:(.+)$")
    match = regex.match(response)
    if match is None:
        message = f"Invalid response: '{response}'"
        logger.error(message)
        return False, message
    bd_from_response = int(match.group(1))
    if bd is not None and bd != bd_from_response:
        message = (
            f"Invalid response: '{response}'. Mismatched bd: {bd_from_response} != {bd}"
        )
        logger.error(message)
        return (
            False,
            message,
        )
    value: str = match.group(2)
    logger.debug(f"Response result: {response} -> {value}")
    return True, value
