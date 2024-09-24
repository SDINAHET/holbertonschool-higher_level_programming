#!/usr/bin/python3
"""
Module that defines a CountedIterator class.

This module provides a custom iterator, `CountedIterator`, which extends the
built-in iterator obtained from an iterable. The class tracks how many items
have been iterated over and provides a method to retrieve this count.

Classes:
    CountedIterator: Extends the functionality of an iterator by keeping track
    of the number of items iterated.
"""


class CountedIterator:
    """
    CountedIterator Class that extends the built-in iterator object.

    This class wraps around an iterator and keeps track of how many items
    have been iterated over.

    Attributes:
        iterator (iterator): The original iterator object.
        count (int): The number of items that have been iterated.

    Methods:
        __next__(): Fetch the next item and increment the count.
        get_count(): Returns the current count of iterated items.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable object.

        Args:
            iterable: The iterable object to be wrapped in the iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.

        Raises:
            StopIteration: If there are no more items in the iterator.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        Return the current count of items iterated.

        Returns:
            int: The number of items that have been iterated over.
        """
        return self.count
