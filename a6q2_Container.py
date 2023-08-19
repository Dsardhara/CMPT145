# Name: Darshan Sardhara
# Instructor Name: Lauresa
# NSID: WLZ670
# Course Name: CMPT 145
# Student ID: 11355677
# section Number: 01
# Course number: 41442

import node as N


class Container:
    def __init__(self):
        self.__size = 0
        self.__first = None

    def is_empty(self):
        return self.__size == 0

    def get_size(self):
        return self.__size

    def push_value(self, data):
        n_node = N.Node(data)
        if self.__first is None:
            self.__first = n_node
        else:
            n_node.set_next(self.__first)
            self.__first = n_node
        self.__size += 1

    def pop_value(self):
        if self.__size == 0:
            return None
        value = self.__first.get_data()
        self.__first = self.__first.get_next()
        self.__size -= 1
        return value

    def peek_value(self):
        return self.__first.get_data()
