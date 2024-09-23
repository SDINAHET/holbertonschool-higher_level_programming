#!/usr/bin/python3
"""Module for class Square, inheriting from Rectangle."""


from importlib import import_module

Rectangle = import_module('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square that inherits from Rectangle."""

    def __init__(self, size):
        """
        Initializes the Square with size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Call the parent constructor

    def area(self):
        """Calculates the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
