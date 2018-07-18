from tree import *

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def isLeaf(node):
            return not node.left and not node.right
        if not p and not q:
            return True
        elif (not p and q ) or (p and not q):
            return False

        if isLeaf(p) and isLeaf(q):
            return p.val == q.val

        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False