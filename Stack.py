class Stack(object):

    def __init__(self):
        """
        Create a new empty Stack, and it needs no parameters.
        """
        self.items = []

    def is_empty(self):
        """
        Check if the Stack is empty or not.
        """
        return self.items == []

    def push(self, item):
        """
        Add an item to the Stack. It takes parameter "item" to add to the Stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove the last item in the Stack.
        """
        return self.items.pop()

    def peek(self):
        """
        Returns the last item in the Stack, without modifying the stack.
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """
        Returns the size of the Stack.
        """
        return len(self.items)
