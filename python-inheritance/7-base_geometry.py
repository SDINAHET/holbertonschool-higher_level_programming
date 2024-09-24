#!/usr/bin/python3
"""module for class BaseGeometry"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer greater than 0.

        Args:
            name: The name of the variable (for error messages --> string).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        # if type(value) is not int:
        #     raise TypeError("{} must be an integer".format(name))
        # if value <= 0:
        #     raise ValueError("{} must be greater than 0".format(name))
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
