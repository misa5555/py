class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.lookup = {}
        self.tail = None
        self.head = None
        self.counter = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.lookup.get(key):
            node = self.lookup[key]
            prev_node = node.prev
            next_node = node.next
            if prev_node:
                prev_node.next = next_node
            else:
                self.head = next_node
            self.tail.next = node
            self.tail = node
            return self.lookup[key].value
        else:
            print(-1)
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.lookup:
            new_node = Node(key, value)
            self.lookup[key] = new_node
            return
        node = Node(key, value)
        self.lookup[key] = node
        if not self.head:
            self.head = node
            self.tail = node
            self.counter += 1
            return
        self.tail.next = node
        self.tail = node
        if self.counter < self.cap:
            self.counter += 1
        else:
            old_head = self.head
            new_head = self.head.next
            self.head = new_head
            self.lookup[old_head.key] = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Your LRUCache object will be instantiated and called as such:
# cache = LRUCache(2)
#
# cache.put(1, 1)
# cache.put(2, 2)
# cache.get(1)
# cache.put(3, 3)
# cache.get(2)
# cache.put(4, 4)
# cache.get(1)
# cache.get(3)
# cache.get(4)
#["LRUCache","put","get","put","get","get"]
#[[1],[2,1],[2],[3,2],[2],[3]]
cache2 = LRUCache(1)
cache2.put(2,1)
cache2.get(2)
cache2.put(3,2)
cache2.get(2)
cache2.get(3)
#["LRUCache","put","put","put","put","get","get"]
#[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
cache3 = LRUCache(2)
cache3.put(2,1)
cache3.put(1,1)
cache3.put(2,3)
cache3.put(4,1)
cache3.get(1)
cache3.get(2)