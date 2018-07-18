from tree import TreeNode

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
       def inorder(node, k):
            ptr = node
            stack = []
            counter = 0
            while ptr:
                stack.append(ptr)
                ptr = ptr.left

            while k > 0:
                ptr = stack.pop()
                k -= 1
                if k == 0:
                    return ptr.value
                right = ptr.right
                while right:
                    stack.append(right)
                    right = right.left
            return -1


        def countNode(self, node):
            if not node:
                return 0
            return 1 + self.countNode(node.left) + self.countNode(node.right)

        def binarySearch(self, node, k):
            num_in_left = self.countNode(self, node.left)
            if self.countNode(self, node) == k:
                return node
            num_in_left = self.countNode(self, node.left)
            if num_in_left < k - 1:
                return self.binarySearch(self, node.right, k - num_in_left - 1)
            elif num_in_left > k:
                return self.binarySearch(self, node.left, k)
