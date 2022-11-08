from __future__ import annotations

import serial
from serial.tools import list_ports
from typing import Dict

from .module import Module


class CaenHV:
    def __init__(
        self, baudrate: int = 9600, port: str | None = None, connect: bool = True
    ):
        self._modules: Dict[int, Module] = {}
        if port is None:
            ports = [port.device for port in serial.tools.list_ports.comports()]
            if len(ports) == 0:
                raise Exception("No ports available")
            port = ports[0]

        self._serial = serial.Serial()
        self._serial.port = port
        self._serial.baudrate = baudrate

        if connect:
            self._serial.open()
        # TODO: automatic module detection (connect to all in range 0..31) and baudrate detection (by getting module name)

    def __del__(self):
        if hasattr(self, "_serial"):
            self._serial.close()

    def __getitem__(self, bd: int) -> Module:
        return self.module(bd)

    def __len__(self):
        return len(self._modules)

    def __iter__(self):
        for device in self._modules.values():
            yield device

    def __next__(self):
        return next(self._modules.values())

    @property
    def is_open(self) -> bool:
        return self._serial.is_open

    @property
    def connected(self) -> bool:
        return self.is_open

    @property
    def serial(self):
        return self._serial

    @property
    def modules(self):
        return self._modules

    def connect(self):
        self._serial.open()

    def module(self, bd: int = 0) -> Module:
        _module = Module(self._serial, bd)
        if bd not in self._modules:
            self._modules[bd] = _module
        return self._modules[bd]
