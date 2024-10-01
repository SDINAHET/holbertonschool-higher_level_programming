#!/usr/bin/python3
"""
This module provides two functions for basic JSON serialization and deserialization:
1. serialize_and_save_to_file: Saves a Python dictionary as a JSON file.
2. load_and_deserialize: Loads a JSON file and returns the deserialized Python dictionary.

Functions:
    serialize_and_save_to_file(data, filename): Serializes a dictionary to JSON and saves it to a file.
    load_and_deserialize(filename): Deserializes a JSON file into a dictionary.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename of the output JSON file.

    Returns:
        None

    Example:
        >>> data = {"name": "John", "age": 30, "city": "New York"}
        >>> serialize_and_save_to_file(data, 'data.json')
        Data serialized and saved to 'data.json'.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"Data serialized and saved to '{filename}'.")


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized data.

    Example:
        >>> data = load_and_deserialize('data.json')
        >>> print(data)
        {'name': 'John', 'age': 30, 'city': 'New York'}
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
