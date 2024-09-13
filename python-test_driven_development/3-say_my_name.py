#!/usr/bin/python3
"""
This module defines a function `say_my_name` that prints a formatted string
containing the first and last name provided as input.
"""


def say_my_name(first_name="", last_name=""):
    """Function that prints 'My name is <first name> <last name>'

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print. Default is an empty string.

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.
    """
    if first_name is None and last_name is None:
        raise TypeError("say_my_name() missing 'first_name' and 'last_name'")

    if not isinstance(first_name, (str, type(None))):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, (str, type(None))):
        raise TypeError("last_name must be a string")

    if first_name and last_name:
        print(f"My name is {first_name} {last_name}")
    elif first_name:
        print(f"My name is {first_name} ")
    else:
        print("No name provided")
