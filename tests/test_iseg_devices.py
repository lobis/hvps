from hvps import Iseg
import pytest


def test_iseg_init(caplog):
    caplog.set_level("DEBUG")

    Iseg(connect=False)

    assert caplog.text == ""

    iseg = Iseg(connect=False, logging_level="DEBUG")

    assert iseg.baudrate == 115200
    assert "Using baud rate 115200" in caplog.text
    assert "Using port " in caplog.text
    assert "Using timeout " in caplog.text


def test_iseg_module(caplog):
    iseg = Iseg(connect=False)

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

    iseg = Iseg(connect=False, logging_level="DEBUG")

    module = iseg.module()

    channel = module.channel(0)

    assert "Creating channel 0" in caplog.text

    print(f"channel: {channel.channel}")
