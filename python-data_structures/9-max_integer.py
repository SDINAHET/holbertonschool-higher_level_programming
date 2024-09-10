#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    # Initialize max_value with the first element of the list
    max_value = my_list[0]

    # Loop through the list to find the maximum value
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
