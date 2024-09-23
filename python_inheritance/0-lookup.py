#!/usr/bin/python3
"""module for function lookup"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods are to be returned.

    Returns:
        A list of strings representing the attributes and methods available
        for the given object.

    Example:
        >>> class MyClass:
        ...     pass
        >>> lookup(MyClass)
        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__'
        , '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
        '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
        '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
        '__str__', '__subclasshook__', '__weakref__']
    """
    return dir(obj)
