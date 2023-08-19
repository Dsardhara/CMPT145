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
        super().__init__()

    def size(self):
        return super().get_size()

    def push(self, data):
        super().push_value(data)

    def peek(self):
        return super().peek_value()

    def pop(self):
        return super().pop_value()
