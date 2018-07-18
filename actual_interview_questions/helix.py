"""
We need to sort a list of strings using a new ordering scheme. We have some
characters we prefer, and would like to treat them like they were at the
beginning of the alphabet.

Given a list of strings to sort, and a string of characters in order of
preference, please implement PrefSort, in your preferred language:

  PrefSort(List<String> mystrings, String preferred)
    -> List<String>

Examples:

  PrefSort(["pony", "horse", "zebra"], "zp") # zpabcdefg
    -> ["zebra", "pony", "horse"]

  PrefSort(["alice", "connor", "barbara", "bob"], "o")    #  oabcdefg...
    -> ["alice", "bob", "barbara", "connor"]

  PrefSort(["a", "b", "-", "~"], "~-")
    -> ["~", "-", "a", "b"]
"""
# zp => {z:0, p:1, a:2, b: 3 .......}
# pony => 1,10,16,
# {pony: '1,10,16...', 'horse': '1,4,'}
import string


def convert(strg, order):
    # '-~'
    order_dict = {}
    for i in range(len(order)):
        order_dict[order[i]] = i
    '''
    order_dict = {}
    for i, ch in enumerate(string.ascii_lowercase):
        if ch in order:
            order_dict[ch] = order.find(ch)
        else:
            order_dict[ch] = i + len(order)
    '''
    # print(order_dict)
    tmp = ''
    for i in range(len(strg)):
        idx = string.ascii_lowercase.find(strg[i]) + len(order)

        new_idx = order_dict.get(strg[i])
        print(new_idx)
        if new_idx != None and new_idx >= 0:
            idx = new_idx
        tmp += str(idx)
    # 'pony' => '194', zebra => '023'
    return tmp


# ary: ["pony", "horse", "zebra"], "zp
def _PrefSort(ary, s):
    order = {}
    for i in range(len(s)):
        order[s[i]] = i

    memo = {}
    ary_to_sort = []
    ans = []
    for j in range(len(ary)):
        converted_string = convert(ary[j], s)  # '0,17, 39, 89'
        memo[converted_string] = ary[j]  # ['1,17, 39, 89': 'pony', '8,3,4,6,',: 'horse', '0,6,89']
        ary_to_sort.append(converted_string)  # ['0,17, 39, 89', ]

    ary_to_sort.sort()
    for el in ary_to_sort:
        ans.append(memo[el])

    return ans

def PrefSort(ary, order):
    return sorted(ary, key=convert(ary, order))

print(PrefSort(["pony", "horse", "zebra"], "zp"))
print(PrefSort(["alice", "connor", "barbara", "bob"], "o"))
print(PrefSort(["a", "b", "-", "~"], "~-"))


# library to construct set-like operations on tree structures
# intersection, union, difference, etc

# Intersection of two trees
# where 'intersection' for two trees means
# that the path back to root node from any particular node
# is the same for both trees.

class Node:
    def __init(self, val):
        self.val = val
        self.right = None
        self.left


r1 = Node(-1)
r2 = Node(-1)


class TwoTrees:
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

    def self.

        intersection(self, r1, r2):

    def helper(n1, n2):
        if not n1 or not n2:
            return None

        if n1 and n2 and n1.val == n2.val:
            new_root = Node(n1.val)
            new_root.left = helper(n1.left, n2.left)  # Node(1)
            new_root.right = helper(n1.right, n2.right)  # None
        # else:
        #    tmp1 = helper(n1.left, n2)
        #    tmp2 = helper()

        return new_root

    return helper(r1, r2)


n0(0)
n1(1)
n2(1)
n3
n4

----------------------
m0(0)
m1(1)
m3
m4

r0(0)
r1(1)

= > [(n0, n1), (m0]