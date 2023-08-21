from hvps import Caen
import pytest


def test_caen_module(caplog):
    caplog.set_level("DEBUG")

    caen = Caen(logging_level="DEBUG")

    # for CAEN, modules are dynamically created
    [caen.module(i) for i in range(0, 32)]

    assert "Getting module 0" in caplog.text

    # check exception takes place
    with pytest.raises(Exception):
        caen.module(-1)

    with pytest.raises(Exception):
        caen.module(35)


def test_caen_channel(caplog):
    caplog.set_level("DEBUG")

    caen = Caen(logging_level="DEBUG")

    module = caen.module()

    channel = module.channel(0)

    assert "Creating channel 0" in caplog.text

    print(f"channel: {channel.channel}")
