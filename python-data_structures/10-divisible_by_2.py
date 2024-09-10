#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create a new list to store True or False values
    result = []

    # Iterate through the original list and check divisibility by 2
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
