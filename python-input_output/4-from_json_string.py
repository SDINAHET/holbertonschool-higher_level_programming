#!/usr/bin/python3
"""
This module provides a function `from_json_string` that returns an object
(Python data structure) represented by a JSON string.

Functions:
    from_json_string(my_str): Returns an object represented by a JSON string.
"""

def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python data structure represented by the JSON string.

    Description:
        - The function uses the `json` module to deserialize the JSON string.
        - If the JSON string doesn't represent a valid object, a
        JSONDecodeError
          will be raised.

    Example:
        >>> from_json_string("[1, 2, 3]")
        [1, 2, 3]

        >>> from_json_string('{"id": 12, "name": "John"}')
        {'id': 12, 'name': 'John'}
    """
    import json
    return json.loads(my_str)
