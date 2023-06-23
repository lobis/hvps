def string_number_to_bit_array(string) -> list:
    """
    Converts a string representing a 16-bit integer into a list of bits.

    Args:
        string (str): The string to convert. It must be a string representing an integer (e.g. "01024").

    Returns:
        list: The list of 16 bits, from least significant to most significant.
    """

    try:
        string_as_int = int(string)
    except ValueError:
        raise ValueError(f"Invalid string '{string}'. Must be an integer.")

    return list(reversed([bool(int(bit)) for bit in f"{string_as_int:016b}"]))
