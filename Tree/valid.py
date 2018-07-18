from tree import TreeNode
class Solution(object):

    def _isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def checkBST(root):
            if not root.right and root.left:
                previousSet = checkBST(root.left)
                if previousSet != False and root.val > root.left.val:
                    return (previousSet[0], root.val)
                else:
                    return False
            elif not root.left and root.right:
                previousSet = checkBST(root.right)
                if previousSet != False and root.val < root.right.val:
                    return (root.val, previousSet[1])
                else:
                    return False
            elif not root.right and not root.left:
                return (root.val, root.val)
            previousSetLeft = checkBST(root.left)
            previousSetRight = checkBST(root.right)
            if previousSetLeft == False or previousSetRight == False:
                return False
            if (root.val > root.left.val and root.val < root.right.val) and (root.val > previousSetLeft[1] and root.val < previousSetRight[0]):
                    return True
            else:
                return False

        return checkBST(root) != False


    def isValidBST(self, root):
        stack = []
        pre = None
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop()
            if pre is not None and pre.val >= top.val:
                return False
            pre = top
            cur = top.right
        return True
s = Solution()
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
# print(s.isValidBST(root))

# r2 = TreeNode(1)
# r2.left = TreeNode(1)
# print(s.isValidBST(r2))
#
# r2 = TreeNode(5)
# l1 = TreeNode(14)
# l2 = TreeNode(1)
# r2.left = l1
# l1.left = l2
# print(s.isValidBST(r2))
#
r3 = TreeNode(3)
l1 = TreeNode(1)
r1 = TreeNode(5)
l1l = TreeNode(0)
l1r = TreeNode(2)
l1rr = TreeNode(3)
r1l = TreeNode(4)
r1r = TreeNode(6)
r3.left = l1
r3.right = r1
l1.left = l1l
l1.right = l1r
l1r.right = l1rr
r1.left = r1l
r1.right = r1r
print(s.isValidBST(r3))

# # [3,null,30,10,  null,null,15,null,45]
# r4 = TreeNode(3)
# l1 = TreeNode(30)
# l2 = TreeNode(10)
# l3 = TreeNode(15)
# l4 = TreeNode(45)
# r4.right = l1
# l1.left = l2
# l2.right = l3
# l2.right = l4
# print(s.isValidBST(r4))