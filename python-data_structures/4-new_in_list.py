#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Check if idx is out of bounds (negative or larger than the list size)
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy of the original list

    # Create a copy of the original list
    new_list = my_list[:]

    # Replace the element at the specific index
    new_list[idx] = element

    return new_list
