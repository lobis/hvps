from types import NoneType


import pytest

from utils import (
    check_command_input,
    string_number_to_bit_array,
    check_command_output_and_convert,
    remove_units,
)


def test_check_command_input():
    command_dict = {
        "CMD1": {
            "input_type": int,
            "allowed_input_values": None,
            "output_type": int,
            "possible_output_values": None,
        },
        "CMD2": {
            "input_type": float,
            "allowed_input_values": [4.0, 5.0],
            "output_type": int,
            "possible_output_values": None,
        },
        "CMD3": {
            "input_type": str,
            "allowed_input_values": ["value"],
            "output_type": int,
            "possible_output_values": None,
        },
    }

    # Test case 1: invalid command name
    with pytest.raises(ValueError) as exc_info:
        check_command_input(command_dict, "INVALID", 5)
    assert (
        str(exc_info.value)
        == "Invalid command 'INVALID'. Valid commands are: CMD1, CMD2, CMD3"
    )

    # Test case 2: invalid input type
    with pytest.raises(ValueError) as exc_info:
        check_command_input(command_dict, "CMD1", "5")
    assert str(exc_info.value) == "Value 5 must be a <class 'int'>."

    # Test case 3: invalid input value
    with pytest.raises(ValueError) as exc_info:
        check_command_input(command_dict, "CMD2", 3.0)
    assert str(exc_info.value) == "Value must be one of [4.0, 5.0]. Got 3.0."

    check_command_input(command_dict, "CMD2", 4.0)

    check_command_input(command_dict, "CMD3", "value")


import pytest

import pytest


def test_remove_units():
    # Test case 1: Valid value with units
    value = "10.5kg"
    result = remove_units(value)
    assert result == "10.5"

    # Test case 2: Valid value without units
    value = "5"
    result = remove_units(value)
    assert result == "5"


def test_check_command_output_and_convert():
    # Test case 1: Valid input and output types
    command_dict = {
        "command_name": {
            "input_type": str,
            "allowed_input_values": ["input1", "input2"],
            "output_type": int,
            "possible_output_values": [1, 2, 3],
        },
        "command_name_2": {
            "input_type": str,
            "allowed_input_values": ["input1", "input2"],
            "output_type": NoneType,
            "possible_output_values": None,
        },
    }
    command = "command_name"
    input_value = "input1"
    response = "2"
    result = check_command_output_and_convert(
        command, input_value, response, command_dict
    )
    assert result == 2

    # Test case 2: Invalid input type
    command = "command_name"
    input_value = 10  # Invalid input type (should be str)
    response = "2"
    with pytest.raises(ValueError, match=r"Value must be a <class 'str'>."):
        check_command_output_and_convert(command, input_value, response, command_dict)

    # Test case 3: Invalid input value
    command = "command_name"
    input_value = "input3"  # Invalid input value (not in allowed_input_values)
    response = "2"
    with pytest.raises(
        ValueError, match=r"Value must be one of \['input1', 'input2'\]. Got 'input3'."
    ):
        check_command_output_and_convert(command, input_value, response, command_dict)

    # Test case 4: No response expected but got a response
    command = "command_name_2"
    input_value = "input1"
    response = "2"
    with pytest.raises(ValueError, match=r"No response expected but got: '2'."):
        check_command_output_and_convert(command, input_value, response, command_dict)

    # Test case 5: Invalid output value
    command = "command_name"
    input_value = "input1"
    response = "4"  # Invalid output value (not in possible_output_values)
    with pytest.raises(
        ValueError, match=r"output value must be one of \[1, 2, 3\]. Got '4'."
    ):
        check_command_output_and_convert(command, input_value, response, command_dict)


def test_string_number_to_bit_array():
    for string, bit_array in [
        (
            "00003",
            [
                True,
                True,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
        ),
        (
            "00000",
            [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
        ),
        (
            "00001",
            [
                True,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
        ),
        (
            "01028",
            [
                False,
                False,
                True,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                True,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
        ),
    ]:
        assert string_number_to_bit_array(string) == bit_array
