##!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class inherits from BaseGeometry and provides
attributes and methods for handling rectangle shapes.
"""


from importlib import import_module

BaseGeometry = import_module('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    # Remove the __str__ method to get the default representation of
    # the object
