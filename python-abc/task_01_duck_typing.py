#!/usr/bin/python3
"""
Shapes Module

This module defines an abstract base class `Shape` and its concrete
implementations `Circle` and `Rectangle`.
It provides a blueprint for creating different shapes and calculates their area
and perimeter.

Classes:
    Shape (ABC): An abstract base class that requires subclasses to implement
    the `area` and `perimeter` methods.
    Circle (Shape): A concrete class representing a circle, providing
    implementations for the area and perimeter methods.
    Rectangle (Shape): A concrete class representing a rectangle, providing
    implementations for the area and perimeter methods.

Functions:
    shape_info(shape): Prints the area and perimeter of the provided shape
    object.

Example:
    To use this module, create instances of `Circle` and `Rectangle` and pass
    them to `shape_info`:

        circle = Circle(radius=5)
        rectangle = Rectangle(width=4, height=7)

        shape_info(circle)     # Outputs area and perimeter of the circle
        shape_info(rectangle)  # Outputs area and perimeter of the rectangle
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract Base Class representing a generic Shape.

    Methods:
        area(): Abstract method that must be implemented by any subclass to
        calculate the area of the shape.
        perimeter(): Abstract method that must be implemented by any subclass
        to calculate the perimeter of the shape.
    """

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Circle Class representing a circle, inheriting from Shape.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        area(): Returns the area of the circle.
        perimeter(): Returns the perimeter (circumference) of the circle.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return abs(2 * math.pi * self.radius) # 2*Pi*r en absolu


class Rectangle(Shape):
    """
    Rectangle Class representing a rectangle, inheriting from Shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Function to print the area and perimeter of a given shape.

    This function uses duck typing to assume that the shape has area() and
    perimeter() methods.

    Args:
        shape (Shape): An object of a class inheriting from Shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
