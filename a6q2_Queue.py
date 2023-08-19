# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01
# Course number: 41442

from a6q2_Container import Container
import node as N
class Queue(Container):
    def _init_(self):
        super().__init__()
        self._head = None
        self._tail = None

    def size(self):
        return self.get_size()

    def enqueue(self, data):
        new_node = N.Node(data)
        if self._first is None:
            self._first = new_node
            self._head = self._first
        else:
            self._tail.set_next(new_node)
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self._head is None:
            return None
        data = self._head.get_data()
        self._head = self._head.get_next()
        self._size -= 1
        if self._head is None:
            self._tail = None
        return data

    def peek(self):
        return self._head.get_data()