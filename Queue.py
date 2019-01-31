class Queue(object):

    def __init__(self):
        """
        Create a new empty Queue, and it needs no parameters.
        """
        self.items = []

    def is_empty(self):
        """
        Check if the Queue is empty or not.
        """
        return self.items == []

    def enqueue(self, item):
        """
        Add an item to the Queue. It takes parameter "item" to add to the Queue.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Remove the front item in the Queue.
        """
        return self.items.pop()

    def size(self):
        """
        Returns the size of the Queue.
        """
        return len(self.items)