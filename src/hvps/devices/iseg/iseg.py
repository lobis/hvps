from __future__ import annotations

from ..hvps import Hvps
from .module import Module


class Iseg(Hvps):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._modules = {0: Module(self._serial, self._logger, 0)}
