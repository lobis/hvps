from serial.tools import list_ports
from typing import List


def string_number_to_bit_array(string) -> List[bool]:
    """
    Converts a string representing a 32-bit integer into a list of bits.

    Args:
        string (str): The string to convert. It must be a string representing an integer (e.g. "01024").

    Returns:
        list: The list of 32 bits, from least significant to most significant.
    """

    try:
        string_as_int = int(string)
    except ValueError:
        raise ValueError(f"Invalid string '{string}'. Must be an integer.")

    return list(reversed([bool(int(bit)) for bit in f"{string_as_int:032b}"]))


def get_serial_ports() -> List[str]:
    """
    Get a list of available serial ports.

    Returns:
        list: A list of available serial ports.
    """
    return [port.device for port in list_ports.comports()]
