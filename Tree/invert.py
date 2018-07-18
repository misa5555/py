class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        leftTree = root.left
        rightTree = root.right

        root.right = self.invertTree(leftTree)
        root.left = self.invertTree(rightTree)
        return root