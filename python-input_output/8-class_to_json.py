#!/usr/bin/python3
"""
Module for class_to_json function.

This module provides a function for returning the dictionary description
with simple data structures (list, dictionary, string, integer, and boolean)
for JSON serialization of an object.

Functions:
    - class_to_json(obj): Returns the dictionary description for JSON
    serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representation of the object that includes only
        serializable attributes.
    """
    return obj.__dict__
