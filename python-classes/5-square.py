#!/usr/bin/python3
"""
This module defines the Square class.

The Square class includes:
- A private instance attribute `size`.
- Property getter and setter for `size` to control access and validation.
- A method to calculate the square's area.
- A method to print the square with the character `#`.
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
        self.size = size # This uses the setter method for validation

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The size to set.

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

    def my_print(self):
        """
        Prints the square with the character `#` is stdout.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
