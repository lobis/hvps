from __future__ import annotations

from ..hvps import Hvps
from .module import Module
from ...commands.caen.channel import validate_board_number
from ...commands.caen import _write_command_read_response


class Caen(Hvps):
    def _write_command_read_response(self, bd: int, command: bytes) -> str | None:
        return _write_command_read_response(
            ser=self._serial,
            lock=self._lock,
            logger=self._logger,
            bd=bd,
            command=command,
        )

    def module(self, module: int = 0) -> Module:
        self._logger.debug(f"Getting module {module}")
        validate_board_number(module)
        if module not in self._modules:
            self._logger.debug(f"Creating module {module}")
            self._modules[module] = Module(
                module=module,
                write_command_read_response=self._write_command_read_response,
                logger=self._logger,
            )
        return self._modules[module]
