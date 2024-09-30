#!/usr/bin/python3
""" My class module
This module defines the MyClass class, which represents an object
with a name and a number. The class provides methods to create
instances of the class and to represent those instances as strings.
"""


class MyClass:
    """ MyClass represents a simple class with a name and a number.

    Attributes:
        name (str): The name of the instance.
        number (int): The number associated with the instance,
                      initialized to 0 by default.

    Methods:
        __init__(self, name):
            Initializes a new instance of MyClass with the specified name.
        __str__(self):
            Returns a string representation of the instance in a formatted
            manner.
    """

    def __init__(self, name):
        """
        Initializes a new instance of MyClass.

        Args:
            name (str): The name to associate with the instance.
                        It should be a string value representing the
                        desired name for this MyClass object.

        Raises:
            TypeError: If the provided name is not a string.

        Example:
            >>> obj = MyClass("John")
            >>> print(obj.name)
            John
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.name = name
        self.number = 0  # The number is initialized to 0 by default.

    def __str__(self):
        """
        Returns a string representation of the MyClass instance.

        This method formats the output to display the name and number
        attributes of the instance in a readable format.

        Returns:
            str: A string representation of the instance in the format:
                 "[MyClass] <name> - <number>"

        Example:
            >>> obj = MyClass("Alice")
            >>> print(obj)
            [MyClass] Alice - 0
        """
        return "[MyClass] {} - {:d}".format(self.name, self.number)
