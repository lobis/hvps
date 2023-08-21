from hvps import Iseg
import pytest


def test_iseg_module(caplog):
    iseg = Iseg()

    # for ISEG only one module exists
    iseg.module()
    iseg.module(0)

    # check exception takes place
    with pytest.raises(Exception):
        iseg.module(-1)

    with pytest.raises(Exception):
        iseg.module(1)


def test_iseg_channel(caplog):
    caplog.set_level("DEBUG")

    iseg = Iseg(logging_level="DEBUG")

    module = iseg.module()

    channel = module.channel(0)

    assert "Creating channel 0" in caplog.text

    print(f"channel: {channel.channel}")
