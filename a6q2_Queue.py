# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01
# Course number: 41442

from a6q2_Container import Container

class Queue(Container):
    def __init__(self):
        super().__init__()
        self.__head = 0
        self.__tail = 0

    def size(self):
        return self.get_size()

    def enqueue(self, data):
        # new_node = N.Node(data, None)
        self.push_value(data)
        if self._size == 1:
            self.__head = self._first
        self.__tail = self._first

    def dequeue(self):
        if self._first is None:
            return None
        data = self.__head.get_data()
        self.__head = self.__head.get_next()
        self._size -= 1
        if self.__head is None:
            self.__tail = None
        return data

    def peek(self):
        first_node = self.__head
        result = first_node.get_data()
        return result
