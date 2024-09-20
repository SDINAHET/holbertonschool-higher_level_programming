#!/usr/bin/python3
"""
Module 102-square
Defines a class Square that represents a square and allows comparison based
on area.
"""


class Square:
    """
    Class that defines a square by:
    - size: size of the square's side (must be a float or integer >= 0)

    Methods:
        area: Returns the current square area.
        Comparison operators are supported (==, !=, <, <=, >, >=) based on the
        square's area.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (float or int): The size of the square's side, default is 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if the area of this square is equal to the area of another
        square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if the area of this square is not equal to the area of
        another square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if the area of this square is less than the area of another
        square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if the area of this square is less than or equal to the area
        of another square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if the area of this square is greater than the area of
        another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if the area of this square is greater than or equal to the
        area of another square."""
        return self.area() >= other.area()
