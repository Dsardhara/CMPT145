import node as N

class Container:

    def __init__(self):
        """
        Initializes an empty container.
        """
        self._size = 0
        self._first = None

    def is_empty(self):
        """
        Checks if the container is empty.

        Returns:
            bool: True if the container is empty, False otherwise.
        """
        return self._size == 0

    def get_size(self):
        """
        Returns the number of elements in the container.

        Returns:
            int: The number of elements in the container.
        """
        return self._size

    def push_value(self, data):
        """
        Adds a new value to the beginning of the container.

        Args:
            data: The value to be added to the container.
        """
        n_node = N.Node(data)
        if self._first is None:
            self._first = n_node
        else:
            n_node.set_next(self._first)
            self._first = n_node
        self._size += 1

    def pop_value(self):
        """
        Removes and returns the value from the beginning of the container.

        Returns:
            The value removed from the container, or None if the container is empty.
        """
        if self._size == 0:
            return None
        value = self._first.get_data()
        self._first = self._first.get_next()
        self._size -= 1
        return value

    def peek_value(self):
        """
        Returns the value from the beginning of the container without removing it.

        Returns:
            The value from the beginning of the container, or None if the container is empty.
        """
        return self._first.get_data()
