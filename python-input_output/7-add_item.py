#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list
and saves the list to a file in JSON format.
"""


import sys
import os

# Dynamically import the required functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Main function to add command line arguments to a list and save to a
    file."""
    filename = "add_item.json"

    # Initialize an empty list if the file doesn't exist
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # Add command line arguments to the list (excluding the script name)
    my_list.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
