from tree import TreeNode
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

root = TreeNode(3)
a1 = TreeNode(9)
b1 = TreeNode(20)
a2 = TreeNode(15)
b2 = TreeNode(7)
root.left = a1
root.right = b1
b1.left = a2
b1.right = b2
