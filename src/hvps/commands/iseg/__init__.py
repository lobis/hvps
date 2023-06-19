from __future__ import annotations
import re

from src.hvps.commands.iseg.channel import (
    _get_set_channel_command,
    _get_mon_channel_command,
)

import logging


def _parse_response(response: bytes) -> str:
    # TODO: implement
    pass
