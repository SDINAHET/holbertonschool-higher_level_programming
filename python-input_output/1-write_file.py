#!/usr/bin/python3
"""
This module provides a function `write_file` that writes a string to a text
file (UTF8) and returns the number of characters written.

Functions:
    write_file(filename="", text=""): Writes a string to a file and returns the
    number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of
    characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to an empty
        string.
        text (str): The string to write into the file. Defaults to an empty
        string.

    Description:
        - The function opens the file in write mode.
        - If the file doesn't exist, it is created.
        - If the file already exists, its content is overwritten.
        - It returns the number of characters written into the file.

    Example:
        >>> nb_characters = write_file("my_first_file.txt", "This School is so
        cool!\n")
        >>> print(nb_characters)
        24
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
