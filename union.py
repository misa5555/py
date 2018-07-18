class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def findParent(node, parent):
            if parent[node] == -1:
                return node
            return findParent(parent[node], parent)


        parent = [-1] * n



        for edge in edges:
            parent0 = findParent(edge[0], parent)
            parent1 = findParent(edge[1], parent)
            if parent0 == parent1:
                return False
            else:
                parent[edge[1]] = parent0

        numOfRoot = 0
        for pa in parent:
            if pa == -1:
                numOfRoot += 1
        return numOfRoot == 1

s = Solution()
print(s.validTree(5, [[0,1],[0,2],[2,3],[2,4]]))
print(s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
