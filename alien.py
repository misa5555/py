from collections import defaultdict
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def createGraph(words):
            graph = defaultdict(list)
            for i in range(0, len(words) - 1):
                # compare words[i] and words[i+1]
                length = min(len(words[i]), len(words[i+1]))
                for j in range(0, length):
                    if words[i][j] != words[i+1][j]:
                        graph[words[i][j]].append(words[i+1][j])
                        break
            return graph

        def search(graph, node, visited, stack):
            neighbors = graph.get(node)
            visited[node] = -1
            if neighbors:
                for neighbor in neighbors:
                    if visited.get(neighbor) == -1:
                        return False
                    elif not visited.get(neighbor):
                        if search(graph, neighbor, visited, stack) == False:
                            return False
            visited[node] = 1
            stack.insert(0, node)
            return True

        def sortWords(words):
            graph = createGraph(words)
            if len(graph) == 0:
                return words[0]
            visited = {}
            stack = []
            for key, item in graph.items():
                if visited.get(key) != 1:
                    canSearch = search(graph, key, visited, stack)
                    if canSearch == False:
                        return ""
            return "".join(stack)
        return sortWords(words)

ary = ["wrt","wrf","er","ett","rftt"]
ary2 = [
  "z",
  "x",
  "z"
]
ary3= ["z", "z"]
s = Solution()
print(s.alienOrder(ary))
print(s.alienOrder(ary2))
print(s.alienOrder(ary3))
