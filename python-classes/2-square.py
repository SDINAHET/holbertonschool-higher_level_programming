#!/usr/bin/python3
"""
This module defines the Square class.

The Square class has a private instance attribute `size`, which is
used to represent the size of the square. The class validates that
the `size` is an integer and greater than or equal to 0 upon
initialization.

Example:
    To create a square, you can use the following syntax:

        my_square = Square(3)

    This will create a square with size 3.
"""


class Square:
    """Defines a square by a private instance attribute size."""

    def __init__(self, size=0):
        """
        Initialize the square with a private instance attribute size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
