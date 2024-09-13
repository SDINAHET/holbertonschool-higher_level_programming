#!/usr/bin/python3
"""
This module defines a function `text_indentation` that prints a text
with 2 new lines after each of these characters: `.`, `?`, and `:`.
"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    result = ''
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in characters:
            result += '\n\n'
        i += 1

    print(result.strip())
