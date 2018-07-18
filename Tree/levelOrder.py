from tree import TreeNode;

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        def merge(dary1, dary2):
            if not dary1 and not dary2:
                return []
            if not dary1:
                return dary2
            if not dary2:
                return dary1
            merged = []
            i = 0
            while i < min(len(dary1), len(dary2)):
                merged.append(dary1[i] + dary2[i])
                i += 1
            merged.extend(dary1[i:])
            merged.extend(dary2[i:])
            return merged

        def traverse(node):
            nodes = []
            if not node:
                return [[]]
            if not node.left and not node.right:
                return [[node.val]]
            r1 = traverse(node.left)
            r2 = traverse(node.right)
            tmp = merge(r1, r2)
            nodes.append([node.val])
            nodes.extend(tmp)
            return nodes

        return traverse(root)
s = Solution()
root = TreeNode(3)
a1 = TreeNode(9)
b1 = TreeNode(20)
a2 = TreeNode(15)
b2 = TreeNode(7)
root.left = a1
root.right = b1
b1.left = a2
b1.right = b2

print(s.levelOrder(root))
