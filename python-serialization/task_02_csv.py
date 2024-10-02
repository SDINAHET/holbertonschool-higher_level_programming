#!/usr/bin/python3
"""
This module provides functionality to convert CSV data to JSON format.

Functions:
    convert_csv_to_json(filename): Reads data from a CSV file and writes it as
    JSON.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Converts a CSV file to a JSON file.

    Args:
        filename (str): The name of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False if an error
        occurred.
    """
    try:
        # Open the CSV file and read its contents using DictReader
        with open(filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = list(csv_reader)  # Convert the CSV rows into a list
            # of dictionaries

        # Serialize the data list to JSON and write it to 'data.json'
        with open('data.json', mode='w') as json_file:
            json.dump(
                data_list,
                json_file,
                indent=4,  # Adds indentation and newlines for readability
                # separators=(',', ': ') Ensures a clean separation betw items
            )

        print(f"Data from {filename} has been converted to 'data_02.json'.")
        return True

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
