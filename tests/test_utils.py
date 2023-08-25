from typing import List

import pytest

from hvps.utils import (
    check_command_input,
    string_number_to_bit_array,
    check_command_output_and_convert,
    remove_units,
)


def test_check_command_input():
    command_dict = {
        "MTH1": {
            "command": "CMD1",
            "input_type": int,
            "allowed_input_values": None,
            "output_type": int,
            "possible_output_values": None,
        },
        "MTH2": {
            "command": "CMD2",
            "input_type": float,
            "allowed_input_values": [4.0, 5.0],
            "output_type": int,
            "possible_output_values": None,
        },
        "MTH3": {
            "command": "CMD3",
            "input_type": str,
            "allowed_input_values": ["VALUE"],
            "output_type": int,
            "possible_output_values": None,
        },
    }

    # Test case 1: invalid command name
    with pytest.raises(ValueError) as exc_info:
        check_command_input(command_dict, "INVALID", 5)
    assert (
        str(exc_info.value)
        == "Invalid command 'None'. Valid commands are: CMD1, CMD2, CMD3"
    )

    # Test case 2: invalid input type
    with pytest.raises(ValueError) as exc_info:
        check_command_input(command_dict, "CMD1", "5")
    assert str(exc_info.value) == "Value 5 must be a number. Got <class 'str'> instead."

    # Test case 3: invalid input value
    with pytest.raises(ValueError) as exc_info:
        check_command_input(command_dict, "CMD2", 3.0)
    assert str(exc_info.value) == "Value must be one of [4.0, 5.0]. Got 3.0."

    check_command_input(command_dict, "CMD2", 4.0)

    check_command_input(command_dict, "CMD3", "VALUE")


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
        "method_name": {
            "command": "command_name",
            "input_type": str,
            "allowed_input_values": ["INPUT1", "INPUT2"],
            "output_type": int,
            "possible_output_values": [1, 2, 3],
        },
        "method_name_2": {
            "command": "command_name_2",
            "input_type": str,
            "allowed_input_values": ["INPUT1", "INPUT2"],
            "output_type": None,
            "possible_output_values": None,
        },
        "method_name_3": {
            "command": "command_name_3",
            "input_type": str,
            "allowed_input_values": ["INPUT1", "INPUT2"],
            "output_type": List[float],
            "possible_output_values": None,
        },
    }

    # Test case 1: Valid output type
    command = "method_name"
    input_value = "INPUT1"
    response = "2"
    result = check_command_output_and_convert(
        command, input_value, response, command_dict
    )
    assert result == 2

    # Test case 2: Valid output type
    command = "method_name_3"
    input_value = "INPUT1"
    response = "2.00,3E-6,4"
    result = check_command_output_and_convert(
        command, input_value, response, command_dict
    )
    assert result == [2.0, 0.000003, 4.0]

    # Test case 4: No response expected but got a response
    command = "method_name_2"
    input_value = "INPUT1"
    response = "2"
    with pytest.raises(ValueError, match=r"No response expected but got: '2'."):
        check_command_output_and_convert(command, input_value, response, command_dict)

    # Test case 5: Invalid output value
    command = "method_name"
    input_value = "INPUT1"
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
