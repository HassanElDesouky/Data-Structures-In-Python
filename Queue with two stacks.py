class QueueWithStacks(object):

    def __init__(self):
        """
        Use the built in list as stack.
        """
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                # Add the elements to the out_stack to reverse the order when called.
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
