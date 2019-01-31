class Deque(object):

    def __init__(self):
        """
        Create a new empty Deque, and it needs no parameters.
        """
        self.items = []

    def is_empty(self):
        """
        Check if the Deque is empty or not.
        """
        return self.items == []

    def add_front(self, item):
        """
        Add item in the front of the Deque.
        """
        self.items.append(item)

    def add_rear(self, item):
        """
        Add item in the rear of the Deque.
        """
        self.items.insert(0, item)

    def remove_front(self):
        """
        Remove the front item from the Deque.
        """
        return self.items.pop()

    def remove_rear(self):
        """
        Remove the last item from the Deque.
        """
        return self.items.pop(0)

    def size(self):
        """
        Returns the size of the Deque.
        """
        return len(self.items)
