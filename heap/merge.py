from queue import PriorityQueue
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        pq = PriorityQueue()
        dummy = ListNode(float('Inf'))
        for node in lists:
            if node: pq.put((node, node.val))

        result_ptr = dummy
        while not pq.empty():
            target = pq.get()[0]

            result_ptr.next = target
            result_ptr = target
            if target.next: pq.put((target.next, target.next.val))

        return dummy.next
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(2)
l1.next = l2
l2.next = l3

l4 = ListNode(1)
l5 = ListNode(1)
l6 = ListNode(2)
l4.next = l5
l5.next = l6

lists = [l1, l4]
s = Solution()
re = s.mergeKLists(lists)
ptr = re
while ptr:
    print(ptr.val)
    ptr = ptr.next

