#!/usr/bin/python3
"""
This module defines a function `print_square(size)` that prints
a square of a given size with the character '#'.
"""


def print_square(size):
    """Print a square with the character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If `size` is not an integer or if `size` is a float
        and is less than 0.
        ValueError: If `size` is less than 0.
    """
    if isinstance(size, float):
        if size < 0:
            raise ValueError("size must be >= 0")
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
