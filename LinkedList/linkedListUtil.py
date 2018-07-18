
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def generateLL(ary):
    head = None
    prevNode = None
    for i in range(len(ary)):
        node = ListNode(ary[i])
        if prevNode:
            prevNode.next = node
        prevNode = node
        if i == 0:
            head = node
    return head

def printLL(head):
    ptr = head
    ary = []
    while ptr:
        ary.append(ptr.val)
        print("val: %s, next: %s" % (ptr.val, ptr.next))
        ptr = ptr.next
    print(ary)
