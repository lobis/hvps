from hvps import Caen
import pytest


def test_caen_module():
    caen = Caen(connect=False, logging_level="DEBUG")

    # for CAEN, modules are dynamically created
    [caen.module(i) for i in range(0, 32)]

    # check exception takes place
    with pytest.raises(Exception):
        caen.module(-1)

    with pytest.raises(Exception):
        caen.module(35)
