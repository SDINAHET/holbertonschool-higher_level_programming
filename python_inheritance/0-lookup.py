#!/usr/bin/python3
"""module for function lookup"""


def lookup(obj):
    """ Returns the list of available attributes and methods of an object."""
    return dir(obj)
