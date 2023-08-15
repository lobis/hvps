from __future__ import annotations

from ..hvps import Hvps
from .module import Module
from ...commands.iseg import _write_command_read_response


class Iseg(Hvps):
    def _write_command_read_response(
        self, command: bytes, expected_response_type: type | None
    ) -> str | None:
        return _write_command_read_response(
            ser=self._serial,
            lock=self._lock,
            logger=self._logger,
            command=command,
            expected_response_type=expected_response_type,
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._modules = {
            i: Module(
                module=i,
                write_command_read_response=self._write_command_read_response,
                logger=self._logger,
            )
            for i in [0]
        }
