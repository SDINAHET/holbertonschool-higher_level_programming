#!/usr/bin/python3
"""
This module provides a function `to_json_string` that returns the JSON
representation of an object (string).

Functions:
    to_json_string(my_obj): Returns the JSON representation of an object.
"""

def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        str: The JSON representation of the object.

    Description:
        - The function uses the `json` module to serialize the object.
        - If the object cannot be serialized, a TypeError is raised.

    Example:
        >>> to_json_string([1, 2, 3])
        '[1, 2, 3]'

        >>> to_json_string({"id": 12, "name": "John"})
        '{"id": 12, "name": "John"}'
    """
    import json
    return json.dumps(my_obj)
