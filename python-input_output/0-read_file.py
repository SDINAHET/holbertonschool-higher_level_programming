#!/usr/bin/python3
"""
This module provides a function `read_file` that reads a text file (UTF8)
and prints its contents to stdout.

Functions:
    read_file(filename=""): Reads a UTF8 text file and prints its content.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty
        string, but you should provide the path to a file.

    Description:
        - The function opens the file in UTF8 encoding.
        - It reads the entire content and prints it to stdout.
        - No additional newlines are added beyond what is present in the file.

    Example:
        >>> read_file("example.txt")
        (The content of the file 'example.txt' is printed to stdout.)
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
