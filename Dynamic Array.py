import ctypes


class DynamicArray(object):

    # init method
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.original_array = self.make_array(self.capacity)

    # Special methods
    def __len__(self):
        """
        :return: the length of the array.
        """
        return self.n

    def __getitem__(self, item):
        """
        Returns the item at the given index.
        """
        if not 0 <= item < self.n:
            return IndexError("Item is out of bounce.")
        return self.original_array[item]

    # Public methods
    def append(self, element):
        """
        Adds an element to at the last index in the array.
        """
        if self.n == self.capacity:
            self._resize(2*self.capacity)  # resizing by 2x if size is not enough

        self.original_array[self.n] = element
        self.n += 1

    def make_array(self, new_capacity):
        """
        Make a new array with the defined capacity.
        """
        return (new_capacity * ctypes.py_object)()

    # Private methods
    def _resize(self, new_capacity):
        """
        Resize the array by 2x the original capacity.
        """
        temp_array = self.make_array(new_capacity)
        for i in range(self.n):
            temp_array[i] = self.original_array[i]
        self.original_array = temp_array
        self.capacity = new_capacity
