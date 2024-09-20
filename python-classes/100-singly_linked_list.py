#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines classes Node and SinglyLinkedList for implementing
a singly linked list.
"""


class Node:
    """
    Class that defines a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node or None): The next node in the list.

    Methods:
        data: Retrieve the data.
        data(value): Set the data, must be an integer.
        next_node: Retrieve the next node.
        next_node(value): Set the next node, must be a Node or None.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node or None): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data from the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data in the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node.

        Args:
            value (Node or None): The new next node.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines a singly linked list.

    Attributes:
        __head (Node or None): The head of the linked list.

    Methods:
        sorted_insert: Inserts a new Node into the list in increasing order.
    """

    def __init__(self):
        """Initialize a new empty singly linked list."""
        self.__head = None

    def __str__(self):
        """
        Return a string representation of the list.

        Returns:
            A string with each node's data on a new line.
        """
        node = self.__head
        result = []
        while node:
            result.append(str(node.data))
            node = node.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position (increasing order).

        Args:
            value (int): The data to be inserted in the new node.
        """
        new_node = Node(value)

        # Case: Insert at the head if the list is empty or value is smaller
        # than the head's data
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Traverse the list to find the correct position
            current = self.__head

            # Break the while loop into two lines for better readability
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node

            # Insert the new node at the correct position
            new_node.next_node = current.next_node
            current.next_node = new_node
