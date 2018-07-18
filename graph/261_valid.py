class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def next_node(num):
            nexts = []
            for e in edges:
                if num == e[0]:
                    nexts.append(e[1])
                    edges.remove(e)
                elif num == e[1]:
                    nexts.append(e[0])
                    edges.remove(e)
            return nexts
        print(next_node(1))
        print(edges)
        visited = [-1] * n
        # visigint => 0
        # visited => 1
        # def dfs(crt):
        #     visited[crt] = 0
        #     for nei in next_node(crt):
        #         if visited[nei] == -1:
        #             if not dfs(crt):
        #                 return False
        #         elif visited[nei] == 0:
        #             return False
        #     visited[crt] = 1
        #     return True
        #
        # ans = dfs(edges[0][0])
        # print(ans)



s = Solution()
# s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])