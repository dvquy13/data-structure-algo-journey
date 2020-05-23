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
        self._head = None
        self._length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self._head
        for _ in range(1, index + 1):
            if node.next is None:
                return -1
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = Node(val, next=self._head)
        if self._head is not None:
            self._head.prev = new_head
        self._head = new_head
        self._length += 1
        return None

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self._head
        for _ in range(1, self._length):
            node = node.next
        new_node = Node(val, prev=node)
        node.next = new_node
        self._length += 1
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:
            return self.addAtHead(val)
        elif index == self._length:
            # Add at tail, not using addAtTail method to avoid reprocessing
            return self.addAtTail(val)
        elif index > self._length:
            return None
        node = self._head
        for _ in range(1, index + 1):
            node = node.next
        new_node = Node(val, next=node, prev=node.prev)
        node.prev.next = new_node
        node.prev = new_node
        self._length += 1
        return None

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self._head = self._head.next
        elif index >= self._length or index < 0:
            return None
        node = self._head
        for _ in range(1, index + 1):
            node = node.next
        if node.next == None:
            node.prev.next == None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self._length -= 1
        return None


# Your MyLinkedList object will be instantiated and called as such:
method_calls = ["MyLinkedList","addAtHead","addAtTail","addAtTail","get","get","addAtTail","addAtIndex","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","get","addAtHead","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtIndex","addAtTail","get","addAtIndex","addAtTail","addAtHead","addAtHead","addAtIndex","addAtTail","addAtHead","addAtHead","get","deleteAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","get","deleteAtIndex","addAtTail","addAtHead","addAtTail","deleteAtIndex","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtTail","addAtHead","addAtIndex","addAtHead","addAtHead","get","addAtHead","get","addAtHead","deleteAtIndex","get","addAtHead","addAtTail","get","addAtHead","get","addAtTail","get","addAtTail","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtHead","deleteAtIndex","get","addAtHead","addAtIndex","addAtTail","get","addAtIndex","get","addAtIndex","get","addAtIndex","addAtIndex","addAtHead","addAtHead","addAtTail","addAtIndex","get","addAtHead","addAtTail","addAtTail","addAtHead","get","addAtTail","addAtHead","addAtTail","get","addAtIndex"]
vals = [[],[84],[2],[39],[3],[1],[42],[1,80],[14],[1],[53],[98],[19],[12],[2],[16],[33],[4,17],[6,8],[37],[43],[11],[80],[31],[13,23],[17],[4],[10,0],[21],[73],[22],[24,37],[14],[97],[8],[6],[17],[50],[28],[76],[79],[18],[30],[5],[9],[83],[3],[40],[26],[20,90],[30],[40],[56],[15,23],[51],[21],[26],[83],[30],[12],[8],[4],[20],[45],[10],[56],[18],[33],[2],[70],[57],[31,24],[16,92],[40],[23],[26],[1],[92],[3,78],[42],[18],[39,9],[13],[33,17],[51],[18,95],[18,33],[80],[21],[7],[17,46],[33],[60],[26],[4],[9],[45],[38],[95],[78],[54],[42,86]]
first = MyLinkedList()
for i in range(1, len(method_calls)):
    if method_calls[i] != 'get':
        print(eval(f"first.{method_calls[i]}(*vals[i])"))
    else:
        if i == len(method_calls) - 2:
            import pdb; pdb.set_trace()
        print(first.get(*vals[i]))
#%
