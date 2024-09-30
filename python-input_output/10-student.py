#!/usr/bin/python3
"""
This module defines the `Student` class, representing a student with
attributes for first name, last name, and age. The class provides a method
to retrieve a dictionary representation of the student instance.
"""


class Student:
    """
    A class representing a Student.

    Attributes:
    ----------
    first_name : str
        The first name of the student.
    last_name : str
        The last name of the student.
    age : int
        The age of the student.

    Methods:
    -------
    to_json(attrs=None):
        Retrieves a dictionary representation of the Student instance.
        If attrs is a list of strings, only attribute names contained in this
        list are retrieved. Otherwise, all attributes are retrieved.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
            If provided, only attributes in this list are included in the
            returned dictionary. If not provided, all attributes are retrieved.

        Returns:
            dict: A dictionary representing the Student instance.
        """
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(
                self, key) for key in attrs if hasattr(self, key)}
        else:
            return self.__dict__
