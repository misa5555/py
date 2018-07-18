from linkedListUtil import *;
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        p1 = head
        p2 = head.next
        p1.next = None

        while p2:
            p2Next = p2.next
            p2.next = p1
            p1 = p2
            if p2Next:
                p2 = p2Next
            else:
                return p2
        #return p2
s = Solution()
l1 = generageLL([1,2])
printLL(l1)
l2 = s.reverseList(l1)
printLL(l2)
