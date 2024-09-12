#!/usr/bin/python3
"""
This module provides a function `add_integer` which adds two integers or
floats, casting them to integers if necessary.
"""
import sys  # Add this import statement to resolve the undefined variable error


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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Check for float overflow
    if isinstance(a, float):
        if (a > sys.float_info.max or a < -sys.float_info.max):
            raise OverflowError("a is too large to be converted to an integer")
    if isinstance(b, float):
        if (b > sys.float_info.max or b < -sys.float_info.max):
            raise OverflowError("b is too large to be converted to an integer")

    return int(a) + int(b)
