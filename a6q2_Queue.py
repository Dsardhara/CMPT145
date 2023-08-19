# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01
# Course number: 41442

from a6q2_Container import Container

class Queue(Container):
    def _init_(self):
        super().__init__()
        self._head = None
        self._tail = None

    def size(self):
        return self.get_size()

    def peek(self):
        return self._head.get_data()