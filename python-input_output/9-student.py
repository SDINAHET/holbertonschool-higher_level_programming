#!/usr/bin/python3
"""
This module defines the `Student` class, which represents a student
with attributes for first name, last name, and age. The class also provides
a method to retrieve a dictionary representation of a student instance.
"""


class Student:
    """
    A class used to represent a Student.

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
    to_json():
        Retrieves a dictionary representation of the Student instance.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the student's first name, last name,
            and age.
        """
        return self.__dict__
