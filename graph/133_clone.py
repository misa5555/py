# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        visited = {}


        def dfs(crt):

            if visited.get(crt.label):
                return visited.get(crt.label)
            else:
                copied = UndirectedGraphNode(crt.label)
                visited[copied.label] = copied

            for nei in crt.neighbors:
                copied.neighbors.append(dfs(nei))
            return copied

        ans = dfs(node)
        return ans
n0 = UndirectedGraphNode(0)
n1 = UndirectedGraphNode(1)
n2 = UndirectedGraphNode(2)
n0.neighbors = [n1, n2]
n1.neighbors = [n0, n2]
n2.neighbors = [n0, n1, n2]
s = Solution()
s.cloneGraph(n0)