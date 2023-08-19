# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01
# Course number: 41442

from a6q2_Container import Container
class Stack(Container):
    def __init__(self):
        """
        Purpose :creates an empty stack
        """
        super().__init__()

    def size(self):
        """
        Purpose
            returns the number of data values in the stack
        Return:
            The number of data values in the stack
        """

        return super().get_size()

    def push(self, data):
        """
        Purpose
            adds the given data value to the stack
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the stack
        Return:
            (none)
        """

        super().push_value(data)

    def peek(self):
        """
        Purpose
            returns the value from the top of given stack
            without removing it
            Note: the stack cannot be empty!
        Post-condition:
            None
        Return:
            the value at the top of the stack
        """

        return super().peek_value()

    def pop(self):
        """
        Purpose
            Removes and returns a data value from the stack.
            Note: the stack cannot be empty!
        Post-condition:
            the first value is removed from the stack
        Return:
            the first value in the stack, or None
        """

        return super().pop_value()
