#!/usr/bin/python3
"""
This module defines a Rectangle class with private attributes for width and
height, and methods to calculate the area and perimeter of the rectangle.
"""


class Rectangle:
    """
    Class that defines a rectangle with private instance attributes for width
    and height, and public class attributes to track the number of instances
    and print symbol.
    """

    # Public class attributes
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle instance with optional width and height, and
        increments the instance count.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the number of instances

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle. If width or height is 0,
        returns 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using the
        character(s) in print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = str(self.print_symbol) * self.__width
        return "\n".join([rect for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation that can recreate the instance using
        eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted and
        decrements the instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement the number of instances
