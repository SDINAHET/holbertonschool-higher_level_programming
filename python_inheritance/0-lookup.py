#!/usr/bin/python3
"""
This module defines a function called `lookup`.

The function returns a list of available attributes and methods
for a given object, using the built-in `dir()` function.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of strings representing the object's attributes
        and methods.
    """
    return dir(obj)
