#!/usr/bin/python3
"""
This module provides a function `load_from_json_file` that creates an
Object from a JSON file.

Functions:
    load_from_json_file(filename): Creates an object from a JSON file.
"""

import json

def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The object created from the JSON file.

    Description:
        - The function reads the JSON formatted string from the specified
          file and deserializes it into a Python object.
        - If the JSON string is invalid, an exception will be raised.

    Example:
        >>> my_list = load_from_json_file("my_list.json")
        >>> my_dict = load_from_json_file("my_dict.json")
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
