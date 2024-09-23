#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.

    Example:
        >>> is_same_class(1, int)
        True
        >>> is_same_class(1, float)
        False
        >>> is_same_class(1, object)
        True
    """
    return type(obj) is a_class
