#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Delete the key-value pair if the key is found
        del a_dictionary[key]
    return a_dictionary
