#!/usr/bin/python3
"""
This module provides a function `save_to_json_file` that writes an Object
to a text file using a JSON representation.

Functions:
    save_to_json_file(my_obj, filename): Writes an object to a text file as
    JSON.
"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using a JSON representation.

    Args:
        my_obj (object): The object to write to the file.
        filename (str): The name of the file where the object will be saved.

    Returns:
        None: The function does not return any value.

    Description:
        - The function serializes the object to a JSON formatted string and
          writes it to the specified file.
        - If the object cannot be serialized, an exception will be raised.

    Example:
        >>> save_to_json_file([1, 2, 3], "my_list.json")
        >>> save_to_json_file({"name": "John", "age": 30}, "my_dict.json")
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
