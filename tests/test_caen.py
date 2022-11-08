import pytest

from caenhv import CaenHV


def test_caen_no_connection():
    with pytest.raises(Exception):
        caen = CaenHV()
