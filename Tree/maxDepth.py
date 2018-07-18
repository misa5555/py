from tree import *


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def depth(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            else:
                return 1 + max(depth(node.left), depth(node.right))

        return depth(root)
