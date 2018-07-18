from linkedListUtil import *
class Solution(object):
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

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        print(length)
        halfHead = head
        firstHalfTail = None
        for i in range(length // 2):
            if i == length // 2 - 1:
                firstHalfTail = halfHead
            halfHead = halfHead.next
        firstHalfTail.next = None
        reverstSecondHalf = self.reverseList(halfHead)

        ptr1 = head
        ptr2 = reverstSecondHalf

        while ptr1 and ptr2:
            nextP1 = ptr1.next
            nextP2 = ptr2.next
            ptr1.next = ptr2
            if nextP1:
                ptr2.next = nextP1
            else:
                ptr2.next = nextP2
            ptr1 = nextP1
            ptr2 = nextP2

        #printLL(head)
        return head

ary = [1,2,3,4,5]
ll = generateLL(ary)
printLL(ll)
s = Solution()
s.reorderList(ll)
