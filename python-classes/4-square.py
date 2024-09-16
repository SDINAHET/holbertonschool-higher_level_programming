#!/usr/bin/python3
"""
This module defines the Square class.

The Square class has a private instance attributs `size`, which is
used to represent the size of the square. The class validates that
the `size` is an integer and greater than or equal to 0 upon
initialization.

It also provides a method to calculate the area of the square.
"""


class Square:
    """Defines a square by a private instance attribute `size`."""

    def __init__(self, size=0):
        """
        Initialize the square with a private instance attribute size.

        Args:
            size (int): The size of the square (defaults is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.size = size  # This uses the setter method for validation

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The size of the set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
