#!/usr/bin/python3
"""defines a Node"""


class Node:
    """Represents Node class."""

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list.
                Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter/set method to retrieve the data."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the position of the square."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

        """defines a SinglyLinkedList"""


class SinglyLinkedList:
    """Represents SinglyLinkedList class."""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list."""
        new_n = Node(value)
        if self.__head is None:
            self.__head = new_n
        elif self.__head.data > value:
            new_n.next_node = self.__head
            self.__head = new_n
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new_n.next_node = temp.next_node
            temp.next_node = new_n

    def __str__(self):
        """Returns a string representation of the linked list."""
        list_v = []
        temp = self.__head
        while temp is not None:
            list_v.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(list_v))
