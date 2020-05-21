# https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/

#%%
class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.head
        for _ in range(1, index + 1):
            if node.next is None:
                return -1
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = Node(val, next=self.head)
        if self.head is not None:
            self.head.prev = new_head
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.head
        while node.next is not None:
            node = node.next
        new_node = Node(val, prev=node)
        node.next = new_node
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = self.head
        for i in range(1, index + 1):
            if i == index and node.next == None:
                new_node = Node(val, prev=node)
                return
            elif node.next == None:
                return
            else:
                node = node.next
        new_node = Node(val, next=node, prev=node.prev)
        node.prev.next = new_node
        node.prev = new_node
        return None

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self.head
        for _ in range(1, index + 1):
            if node.next == None:
                return
            else:
                node = node.next
        if node.prev == None:
            self.head = self.head.next
        elif node.next == None:
            node.prev.next == None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        return None


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.deleteAtIndex(1)
param_1 = obj.get(1)
#%%
