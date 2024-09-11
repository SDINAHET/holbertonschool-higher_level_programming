#!/usr/bin/python3

def best_score(a_dictionary):
    # Check if the dictionary is valid (not None or empty)
    if a_dictionary:
        # Return the key with the highest value
        return max(a_dictionary, key=a_dictionary.get)
    return None
