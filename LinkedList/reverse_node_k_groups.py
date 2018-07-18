# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def reverse_k(node, k):
  prev = node
  crt = node.next
  i = 0
  group_head, group_tail, next_group_head = node, None, None
  while i < k - 1 and crt:
    if not crt:
        return (None, None, None)
    ahead = crt.next
    crt.next = prev
    prev, crt = crt, ahead
    if i == k - 2:
        group_tail = prev
        next_group_head = crt
    i += 1
  return (group_head, group_tail, next_group_head)

def get_length(node):
  crt = node
  count = 0
  while crt:
    crt = crt.next
    count += 1
  return count
    
def reverseNodesInKGroups(l, k):
  if k == 1:
    return l
  head = ListNode(-1)
  head.next = l
  last_head = head
  crt = l
  operation_times = get_length(l) // k
  for i in range(operation_times):
    tmp = reverse_k(crt, k)
    group_head, group_tail, next_group_head = tmp[0], tmp[1], tmp[2]
    last_head.next = group_tail
    last_head = group_head
    crt = next_group_head

  group_head.next = next_group_head

  return head.next
    
head = ListNode(1)
k = 11
nodes = [ ListNode(i+1) for i in range(k)]
for i in range(k-1):
  nodes[i].next = nodes[i+1]
# l = reverseNodesInKGroups(nodes[0], 3)
# crt = l
# while crt:
#   print(crt.value)
#   crt = crt.next


def differentPlaylists(n, k, l):
  ans = 1
  for i in range(l):
    if i > k:
      ans *= (n - k)
      ans %= (10 ** 9 + 7)
    else:
      ans *= n - i
      ans %= (10 ** 9 + 7)
  return ans % (10 ** 9 + 7)

differentPlaylists(328653, 8786, 27853637)


