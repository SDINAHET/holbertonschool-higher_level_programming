#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        # Create a new list excluding the item at the specified index
        my_list = my_list[:idx] + my_list[idx+1:]
    return my_list
