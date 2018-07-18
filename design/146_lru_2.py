class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity):

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.dic.get(key)
        if node:
            self._remove(node)
            self._append(node)
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.dic.get(key)
        if node:
            self._remove(node)
            self._append(node)
        else:
            node = Node(key, value)
            self._append(node)
            self.dic[key] = node
            if len(self.dic) == self.cap + 1:
                node_to_remove = self.head.next
                self._remove(self.head.next)
                del self.dic[node_to_remove.key]

    def _remove(self, node):
        before = node.prev
        ahead = node.next
        before.next = ahead
        ahead.prev = before

    def _append(self, node):
        old_tail = self.tail.prev
        old_tail.next = node
        node.prev = old_tail
        node.next = self.tail
        self.tail.prev = node

