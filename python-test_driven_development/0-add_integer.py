#!/usr/bin/python3
"""
This module provides a function `add_integer` which adds two integers or
floats, casting them to integers if necessary.
"""


def add_integer(a, b=98):
    """Adds two integers or floats, casting them to integers if necessary.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.

    Returns:
        int: The sum of `a` and `b` as an integer.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
