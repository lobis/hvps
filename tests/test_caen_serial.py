import pytest

from hvps import CAEN


# find a way to only run these tests if a serial port connection exists


@pytest.mark.skip(reason="Needs fixing")
def test_caen_no_connection():
    with pytest.raises(Exception):
        # no ports available
        caen = CAEN(port=None, connect=False)

    with pytest.raises(Exception):
        # no ports available or cannot connect
        caen = CAEN(connect=True)
