from __future__ import annotations
from serial.tools import list_ports
from typing import List, Dict
import re


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


def remove_units(value: str) -> str:
    """
    Remove the units from a value.

    Returns:
        The value without units.
    """
    # Regular expression pattern to match the units at the end of the string
    pattern = r"[A-Za-z/%]+?$"

    # Remove the units using regex substitution
    value_without_units = re.sub(pattern, "", value)

    return value_without_units


def check_command_input(
    command_dict: Dict, method: str, input_value: int | float | str | None = None
) -> None:
    """
    Check the input type and value of a command.

    Args:
        method (str): The method.
        input_value (int | float | str | None): The input value.
        command_dict (Dict): The command dictionary, Must be of the form:
            "method_name": {"command": associated command,
                                "input_type": input_type,
                                "allowed_input_values": allowed_input_values,
                                "output_type": output_type,
                                "possible_output_values": possible_output_values}
                                ...
                            }
    Throws:
        ValueError: If the input value is not of the correct type, is not in the allowed values list or
                    if the command is not in the command dictionary.
    """
    if method not in command_dict.keys():
        valid_methods_string = ", ".join(command_dict.keys())
        raise ValueError(
            f"Invalid method '{method}'. Valid methods are: {valid_methods_string}"
        )

    input_type = command_dict[method]["input_type"]
    allowed_input_values = command_dict[method]["allowed_input_values"]

    if input_type is None:
        if input_value is not None:
            raise ValueError(f"Method {method} does not take an input value.")
        else:
            return
    if input_type is str:
        if not isinstance(input_value, str):
            raise ValueError(
                f"Value {input_value} must be a string. Got {type(input_value)} instead."
            )
    if input_type is int or input_type is float:
        if not isinstance(input_value, (int, float)):
            raise ValueError(
                f"Value {input_value} must be a number. Got {type(input_value)} instead."
            )

    if allowed_input_values and input_value not in allowed_input_values:
        raise ValueError(
            f"Value must be one of {allowed_input_values}. Got {input_value}."
        )


def check_command_output_and_convert(
    method: str,
    input_value: int | float | str | None | List[int] | List[float] | List[str],
    response: str | List[str] | None,
    command_dict: Dict,
) -> int | float | str | None | List[int] | List[float] | List[str]:
    """
    Check output types and convert the response if necessary.

    Args:
        method (str): The method's name.
        input_value (int | float | str | None | List[int] | List[float] | List[str]): The input value.
        response (str | List[str] | None): The response.
        command_dict (Dict): The command dictionary, Must be of the form:
            "command_name": {"input_type": input_type,
                                "allowed_input_values": allowed_input_values,
                                "output_type": output_type,
                                "possible_output_values": possible_output_values}
                                ...
                            }
    Throws:
        ValueError: If the input value is not of the correct type, the response is not of the
        correct type or any of them is not in the allowed/possible values list.

    Returns:

    """
    output_type = command_dict[method]["output_type"]
    possible_output_values = command_dict[method]["possible_output_values"]

    if output_type is None:
        if response is not None:
            raise ValueError(f"No response expected but got: '{response}'.")
        else:
            return None
    else:
        if output_type is float or output_type is int:
            try:
                value = output_type(remove_units(response))
            except ValueError:
                raise ValueError(
                    f"Invalid string '{response}'. Must be a {output_type}."
                )
        elif output_type is List[float]:
            response = response.split(",")
            try:
                value = [float(remove_units(v)) for v in response]
            except ValueError:
                raise ValueError(
                    f"Invalid string '{response}'. Must be a list of float."
                )
        elif output_type is List[int]:
            try:
                response = response.split(",")
                value = [int(v) for v in response]
            except ValueError:
                raise ValueError(f"Invalid string '{response}'. Must be a list of int.")
        else:
            value = response

    if possible_output_values and value not in possible_output_values:
        raise ValueError(
            f"output value must be one of {possible_output_values}. Got '{value}'."
        )
    return value
