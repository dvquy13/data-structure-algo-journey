#%%
class Array:
    _HALF_THRESHOLD = 1/4

    def __init__(self, cap: int):
        self._array = [0] * cap
        self._cap = cap
        self._length = 0

    def size(self):
        return self._length

    def capacity(self):
        return self._cap

    def isEmpty(self):
        return self._length == 0

    def itemAt(self, index):
        return self._array[index]

    def _copy(self, new_array):
        for i in range(self.size()):
            new_array._array[i] = self._array[i]
            new_array._length += 1
        return new_array

    def _morph(self, new_array):
        # TODO: Find a better way to handle this awkwardness.
        # How to properly generate new instance?
        self._array = new_array._array
        self._cap = new_array.capacity()
        self._length = new_array.size()

    def _resize_cap(self, multiplier: int):
        new_array = Array(self.capacity() * multiplier)
        new_array = self._copy(new_array)
        self._morph(new_array)

    def append(self, item):
        if self._length == self._cap:
            self._resize_cap(2)
        self._array[self._length] = item
        self._length += 1

    def insert(self, item, index):
        if self._length == self._cap:
            self._resize_cap(2)
        for i in range(self._length-1, index-1, -1):
            self._array[i+1] = self._array[i]
        self._array[index] = item
        self._length += 1

    def pop(self):
        if self.size() < self._HALF_THRESHOLD * self.capacity():
            self._resize_cap(0.5)
        item = self.itemAt(self.size() - 1)
        self._length -= 1
        return item

    def removeAt(self, index):
        if self.size() < self._HALF_THRESHOLD * self.capacity():
            self._resize_cap(0.5)
        item = self.itemAt(index)
        for i in range(index, self._length-1):
            self._array[i] = self._array[i+1]
        self._length -= 1
        return item


array = Array(4)
for n in [8,3,2]:
    array.append(n)
assert array.capacity() == 4
assert array.size() == 3
array.insert(4, 1)
assert array.size() == 4
assert array.itemAt(1) == 4
pop_item = array.pop()
assert pop_item == 2
assert array.size() == 3
rm_item = array.removeAt(0)
assert rm_item == 8
assert array.size() == 2
assert array.itemAt(1) == 3

# %%
