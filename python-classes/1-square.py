#!/usr/bin/python3
"""
This module defines a class Square.

The Square class has a private instance attribute `size`,
which is initialized via the constructor method.
"""


class Square:
    """Defines a square by a private instance attribute `size`."""

    def __init__(self, size):
        """Initialize the square with a private instance attribute size."""
        self.__size = size  # Private attribute
