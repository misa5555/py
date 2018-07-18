class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def findParent(node, parents):

            if parents[node] == -1:
                return node
            else:
                return findParent(parents[node], parents)

        parents = [-1] * n

        for edge in edges:
            parentNode0 = findParent(edge[0], parents)
            parentNode1 = findParent(edge[1], parents)

            if parentNode0 == parentNode1:
                continue
            elif parents[parentNode0] == -1 and parents[parentNode1] != -1:
                parents[parentNode1] = parentNode0
            elif parents[parentNode1] == -1 and parents[parentNode0] != -1:
                parents[parentNode0] = parentNode1
            else:
                parents[parentNode0] = parentNode1
        return parents.count(-1)

s = Solution()
print(s.countComponents(5, [[0,1],[1,2],[3,4]]))
print(s.countComponents(5, [[0,1],[1,2],[0,2],[3,4]]))
