#!/usr/bin/python3
"""
This module defines a function `text_indentation` that prints a text
with 2 new lines after each of these characters: `.`, `?`, and `:`.
"""

def text_indentation(text):
    """Print text with two new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    # Print the result, removing any leading or trailing spaces from each line
    print("\n".join([line.strip() for line in result.split("\n")]))
