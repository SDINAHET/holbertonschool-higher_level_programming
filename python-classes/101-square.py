#!/usr/bin/python3
"""
Module 101-square
Defines a class Square that represents a square.
"""


class Square:
    """
    Class that defines a square by:
    - size: size of the square's side (must be an integer >= 0)
    - position: tuple representing the square's position (must be a tuple of 2
    positive integers)

    Methods:
        area: Returns the current square area.
        my_print: Prints the square using the character '#', respecting the
        position attribute.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square.

        Args:
            size (int): Size of the square, default is 0.
            position (tuple): Position of the square, default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): Position of the square, must be a tuple of 2
            positive integers.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#', respecting the position
        attribute.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Return the string representation of the square.

        This method allows the square to be printed directly using the print()
        function.
        """
        if self.__size == 0:
            return ""

        result = "\n" * self.__position[1]
        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size
            if i != self.__size - 1:
                result += "\n"
        return result
