from __future__ import annotations

from ..hvps import Hvps
from .module import Module


class Caen(Hvps):
    def module(self, module: int = 0) -> Module:
        return super().module(module)
