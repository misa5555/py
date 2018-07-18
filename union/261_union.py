class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])

        def findParent(parent, i):
            if parent[i] == -1:
                return i
            else:
                return findParent(parent, parent[i])

        def union(parent, i, j):
            parent1 = findParent(parent, i)
            parent2 = findParent(parent, j)
            parent[parent2] = parent1

        parent = [-1] * n
        def isCyclic():
            for i in graph:
                for j in graph.get(i):
                    p_i = findParent(parent, i)
                    p_j = findParent(parent, j)
                    if p_i == p_j:
                        return True
                    else:
                        union(parent, i, j)
            print(parent)
            return False
        from collections import Counter
        if isCyclic():
            return False
        else:
            return Counter(parent).get(-1) == 1

s = Solution()
a = s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
print(a)

a2 = s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
print(a2)

a3 = s.validTree(4, [[0,1],[2,3]])
print(a3)
