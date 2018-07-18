class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        p1 = l1
        p2 = l2
        result = None
        prevNode = None
        head = None
        if p1.val < p2.val:
            head = ListNode(p1.val)
            p1 = p1.next
        else:
            head = ListNode(p2.val)
            p2 = p2.next
        ptr = head

        while p1 and p2:
            if p1.val <= p2.val:
                newNode = ListNode(p1.val)
                p1 = p1.next
            else:
                newNode = ListNode(p2.val)
                p2 = p2.next

            ptr.next = newNode
            ptr = newNode

        while p1:
            newNode = ListNode(p1.val)
            ptr.next = newNode
            ptr = newNode
            p1 = p1.next
        while p2:
            newNode = ListNode(p2.val)
            ptr.next = newNode
            ptr = newNode
            p1 = p2.next

        ptr.next = None

        return head
