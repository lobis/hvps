from hvps import Iseg
import pytest


def test_iseg_module():
    iseg = Iseg(connect=False)

    # for ISEG only one module exists
    iseg.module()
    iseg.module(0)

    # check exception takes place
    with pytest.raises(Exception):
        iseg.module(-1)

    with pytest.raises(Exception):
        iseg.module(1)
