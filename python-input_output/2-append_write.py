#!/usr/bin/python3
"""
This module provides a function `append_write` that appends a string to the
end of a text file (UTF8) and returns the number of characters added.

Functions:
    append_write(filename="", text=""): Appends a string to a file and returns
    the number of characters added.
"""

def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to an empty string.
        text (str): The string to append to the file. Defaults to an empty string.

    Description:
        - The function opens the file in append mode.
        - If the file doesn't exist, it is created.
        - It appends the text to the end of the file.
        - It returns the number of characters added to the file.

    Example:
        >>> nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
        >>> print(nb_characters_added)
        24
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
