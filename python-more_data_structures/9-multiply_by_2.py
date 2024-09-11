#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new dictionary with the same keys but double the values
    return {key: value * 2 for key, value in a_dictionary.items()}
