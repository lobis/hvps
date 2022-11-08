from __future__ import annotations
import re

from .module import _get_set_module_command, _get_mon_module_command


def _parse_response(response: bytes, bd: int | None = None) -> tuple[bool, str]:
    try:
        response: str = response.decode("utf-8").strip()
    except UnicodeDecodeError:
        return False, f"Error decoding response: '{response}'"

    regex = re.compile(r"^#BD:(\d\d),CMD:OK,VAL:(.+)$")
    match = regex.match(response)
    if match is None:
        return False, f"Invalid response: '{response}'"
    bd_from_response = int(match.group(1))
    if bd is not None and bd != bd_from_response:
        return (
            False,
            f"Invalid response: '{response}'. Mismatched bd: {bd_from_response} != {bd}",
        )
    value: str = match.group(2)
    return True, value
