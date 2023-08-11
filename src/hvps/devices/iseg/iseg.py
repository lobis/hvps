from __future__ import annotations

from ..hvps import Hvps
from .module import Module


class Iseg(Hvps):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._modules = {
            i: Module(ser=self._serial, logger=self._logger, lock=self._lock, module=i)
            for i in [0]
        }
