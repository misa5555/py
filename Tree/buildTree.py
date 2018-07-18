from tree import TreeNode
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # preorder = [3, 9, 20, 15, 7]
        # inorder = [9, 3, 15, 20, 7]
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        root_val = preorder[0]
        i = 0
        while i < len(inorder) and inorder[i] != root_val:
            i += 1

        left_inorder = inorder[:i]
        right_inorder = inorder[i+1:]

        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1:]

        root.right = self.buildTree(right_preorder, right_inorder)
        root.left = self.buildTree(left_preorder, left_inorder)

        return root
