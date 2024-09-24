#!/usr/bin/python3
"""
VerboseList Module

This module defines the VerboseList class, which extends the built-in list class
and provides notification messages for certain list operations such as append,
extend, remove, and pop.

Classes:
    VerboseList: Extends the Python list class and prints messages during list
    modification operations.

Usage example:

    >>> vl = VerboseList([1, 2, 3])
    >>> vl.append(4)
    Added [4] to the list.
    >>> vl.extend([5, 6])
    Extended the list with [2] items.
    >>> vl.remove(2)
    Removed [2] from the list.
    >>> vl.pop()
    Popped [6] from the list.
    >>> vl.pop(0)
    Popped [1] from the list.
"""


class VerboseList(list):
    """
    VerboseList Class that extends the built-in list class and provides
    notification messages for certain list operations (append, extend, remove, pop).

    Methods:
        append(item): Adds an item to the list and prints a notification.
        extend(iterable): Extends the list and prints a notification with the number of items added.
        remove(item): Removes an item from the list and prints a notification.
        pop(index=-1): Removes and returns an item from the list, printing a notification.
    """

    def append(self, item):
        """
        Add an item to the list and print a notification.

        Args:
            item: The item to add to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with elements from the iterable and print a notification.

        Args:
            iterable: An iterable whose items will be added to the list.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of the item from the list and print a notification.

        Args:
            item: The item to remove from the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return the item at the given index and print a notification.

        Args:
            index: The index of the item to pop (default is the last item).

        Returns:
            The item that was removed.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
