# https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/

#%%
class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def size(self):
        return self._size

    def isEmpty(self):
        return self._head == None

    def valueAt(self, index):
        if self._invalid_index(index):
            return None
        curr = self._head
        for _ in range(1, index + 1):
            curr = curr.next
        return curr.val

    def pushFront(self, item):
        node = Node(item, next=self._head)
        if self._head:
            self._head.prev = node
        self._head = node
        self._size += 1
        return None

    def popFront(self):
        popNode = self._head
        self._head = self._head.next
        self._head.prev = None
        self._size -= 1
        return popNode.val

    def pushBack(self, value):
        node = Node(value, prev=self._tail)
        if self._tail:
            self._tail.next = node
        self._tail = node
        self._size += 1
        return None

    def popBack(self):
        popNode = self._tail
        self._tail = self._tail.prev
        self._tail.next = None
        self._size -= 1
        return popNode.val

    def front(self):
        return self._head.val

    def back(self):
        return self._tail.val

    def insert(self, value, index):
        if self._invalid_index(index):
            return None
        if index == self.size():
            return self.pushBack(value)
        if index == 0:
            return self.pushFront(value)
        curr = self._head
        for _ in range(1, index + 1):
            curr = curr.next
        node = Node(value, prev=curr.prev, next=curr)
        curr.prev = node
        self._size += 1
        return None

    def removeAt(self, index):
        if self._invalid_index(index):
            return None
        if index == 0:
            self.popFront()
            return None
        if index == self.size():
            self.popBack()
            return None
        curr = self._head
        for _ in range(1, index + 1):
            curr = curr.next
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self._size -= 1
        return None

    def _invalid_index(self, index):
        return not (index >= self.size() or index < 0)
