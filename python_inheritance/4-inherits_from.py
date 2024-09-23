#!/usr/bin/python3
"""module for function inherits_from"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class that inherits from a_class,
        otherwise False.

    Example:
        >>> inherits_from(True, int)
        True
        >>> inherits_from(True, bool)
        False
        >>> inherits_from(True, object)
        True
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
