#!/usr/bin/python3
"""
This module defines the `Student` class, representing a student with
attributes for first name, last name, and age. The class provides methods
for serialization and deserialization.
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
    reload_from_json(json):
        Replaces all attributes of the Student instance based on a dictionary.
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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a
        dictionary.

        Args:
            json (dict): A dictionary where the keys are attribute names
            and values are the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
