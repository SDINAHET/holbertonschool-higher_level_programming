#!/usr/bin/python3
"""
This module defines a Rectangle class with private attributes for width and
height, and methods to calculate the area and perimeter of the rectangle.
"""


class Rectangle:
    """
    Represents a rectangle with private instance attributes for width and
    height, and methods to calculate the area and perimeter, and a string
    representation.

    Attributes:
        width (int): The width of the rectangle (must be an integer >= 0).
        height (int): The height of the rectangle (must be an integer >= 0).
    """

    # Public class attribute to track the number of instances
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.

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
        """Returns the perimeter of the rectangle.

        If either width or height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle with the
        character '#'.

        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for _ in range(self.__height):
            rect_str.append("#" * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """Returns a string representation of the rectangle that can recreate
        a new instance.

        The format is: Rectangle(width, height)
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement the number of instances
