from ..module import Module as BaseModule
from .channel import Channel


class Module(BaseModule):
    def channel(self, channel: int) -> Channel:
        return super().channel(channel)
