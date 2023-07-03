from __future__ import annotations

from ..hvps import Hvps
from .module import Module
from ...commands.caen.channel import validate_board_number


class Caen(Hvps):
    def module(self, module: int = 0) -> Module:
        self._logger.debug(f"Getting module {module}")
        validate_board_number(module)
        if module not in self._modules:
            self._logger.debug(f"Creating module {module}")
            self._modules[module] = Module(self._serial, self._logger, module)
        return self._modules[module]
