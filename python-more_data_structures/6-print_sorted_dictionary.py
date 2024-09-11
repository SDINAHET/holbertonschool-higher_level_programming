#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Sort the keys and print each key-value pair in sorted order
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
