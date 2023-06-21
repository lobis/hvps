def string_to_bit_array(string):
    """
    Converts a string into a bit array.

    Args:
        string (str): The input string to be converted.

    Returns:
        list: A list of integers representing the individual bits of the input string.

    Example:
        input_string = "Hi"
        bit_array = string_to_bit_array(input_string)
        print(bit_array)

        [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]
    """
    bit_array = []
    for char in string:
        ascii_value = ord(char)
        binary_string = bin(ascii_value)[2:].zfill(8)  # Convert to 8-bit binary string
        bit_array.extend([int(bit) for bit in binary_string])
    return bit_array
