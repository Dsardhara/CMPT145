# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01
# Course number: 41442

import node as n


class LList(object):
    def __init__(self):
        """
        Purpose
            creates an empty list
        """
        self._size = 0  # how many elements in the stack
        self._head = None  # the node chain starts here; initially empty
        self._tail = None

    def is_empty(self):
        """
        Purpose
            Checks if the given list has no data in it
        Return:
            :return True if the list has no data, or False otherwise
        """
        return self._size == 0

    def size(self):
        """
        Purpose
            Returns the number of data values in the given list
        Return:
            :return The number of data values in the list
        """
        return self._size

    def prepend(self, val):
        """
        Purpose
            Insert val at the front of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is at index 0.
            The values previously in the list appear after the new value.
        Return:
            :return None
        """
        new_node = n.Node(val)
        if self._head is None:  # If the list is empty
            self._head = new_node
            self._tail = new_node
        else:
            new_node.set_next(self._head)
            self._head = new_node
        self._size += 1
        pass

    def append(self, val):
        """
        Purpose
            Insert val at the end of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is last in the list.
        Return:
            :return None
        """
        new_node = n.Node(val)
        if self._head is None:
            self._head = new_node
        else:
            self._tail.set_next(new_node)
        self._tail = new_node
        self._size += 1

    def get_index_of_value(self, val):
        """
        Purpose
            Return the smallest index of the given val.
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            none
        Return:
            :return True, idx if the val appears in self
            :return False, None if the vale does not appear in self
        """
        numb = self._head
        index = 0

        while numb is not None:
            if numb.get_data() == val:
                return tuple([True, index])
            numb = numb.get_next()
            index += 1

        return tuple([False, None])

    def remove_from_front(self):
        """
        Purpose
            Removes and returns the first value 
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in the list.
        Return:
            :return The pair (True, value) if self is not empty
            :return The pair (False, None) if self is empty
        """
        # numb = self._head
        if self._head is None:
            return tuple([False, None])

        val = self._head.get_data()
        self._head = self._head.get_next()
        self._size -= 1
        if self._size == 0:
            self._tail = None
        return tuple([True, val])

    def remove_from_back(self):
        """
        Purpose
            Removes and returns the last value
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in the list.
        Return:
            :return The pair True, value if self is not empty
            :return The pair False, None if self is empty
        """
        if self._head is None:
            return tuple([False, None])

        val = self._tail.get_data()
        self._size -= 1

        if self._size == 0:
            self._head = None
            self._tail = None
        else:
            active = self._head
            while active.get_next() != self._tail:
                active = active.get_next()
            active.set_next(None)
            self._tail = active

        return tuple([True, val])

    def retrieve_data(self, idx):
        """
        Purpose
            Return the value stored at the index idx
        Preconditions:
            :param idx:   a non-negative integer
        Post-conditions:
            none
        Return:
            :return (True, val) if val is stored at index idx and idx is valid
            :return (False, None) if the idx is not valid for the list
        """

        if idx < 0 or self._size <= idx:
            return tuple([False, None])
        numb = self._head
        index = 0

        while numb is not None:
            if index == idx:
                val=numb.get_data()
                return tuple([True, val])
            numb = numb.get_next()
            index += 1


    def set_data(self, idx, val):
        """
        Purpose
            Store val at the index idx
        Preconditions:
            :param val:   a value of any kind
            :param idx:   a non-negative integer
        Post-conditions:
            The value stored at index idx changes to val
        Return:
            :return True if the index was valid, False otherwise
        """
        pass
