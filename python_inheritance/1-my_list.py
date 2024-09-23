#!/usr/bin/python3
"""module for class my_list"""


class MyList(list):
    """
    A subclass of the built-in list that includes a method to print the list
    sorted in ascending order.

    Public Methods:
        - print_sorted(self): Prints the list sorted in ascending order.

    Example:
        >>> my_list = MyList()
        >>> my_list.append(3)
        >>> my_list.append(1)
        >>> my_list.append(2)
        >>> print(my_list)
        [3, 1, 2]
        >>> my_list.print_sorted()
        [1, 2, 3]
        >>> print(my_list)
        [3, 1, 2]
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.

        This method does not modify the original list.

        Example:
            >>> my_list = MyList([5, 2, 9, 1])
            >>> my_list.print_sorted()
            [1, 2, 5, 9]
        """
        print(sorted(self))
