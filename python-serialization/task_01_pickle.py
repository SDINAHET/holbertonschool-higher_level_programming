#!/usr/bin/python3
"""
This module defines a CustomObject class that can be serialized and
deserialized using the pickle module.

Class:
    CustomObject: A class with attributes name, age, and is_student.
                  Provides methods to serialize and deserialize objects.
"""


import pickle


class CustomObject:
    """
    A class representing a custom object with name, age, and is_student
    attributes.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject with name, age, and is_student.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted string.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object and save it to the specified file using
        pickle.

        Args:
            filename (str): The name of the file where the object will be
            serialized.

        Returns:
            None
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            # print(f"Object serialized and saved to '{filename}'.")
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and load an object from the specified file using pickle.

        Args:
            filename (str): The name of the file from which to deserialize the
            object.

        Returns:
            CustomObject: The deserialized object, or None if there was an
            error.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            # print(f"Object deserialized from '{filename}'.")
            return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error deserializing object: {e}")
            return None
