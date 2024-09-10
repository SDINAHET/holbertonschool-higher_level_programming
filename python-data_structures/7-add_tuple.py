#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by padding them
    # with zeros if needed
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Add the first and second elements of both tuples
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return new_tuple
