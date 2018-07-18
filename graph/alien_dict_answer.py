class Solution:
    def toposort(self, node, graph, visited, stack):
        if visited[node] == 1:
            return False
        elif visited[node] == 2:
            return

        visited[node] = 1
        for adjacent in graph[node]:
            if self.toposort(adjacent, graph, visited, stack) == False:
                return False

        visited[node] = 2
        stack.append(node)

        return

    def alienOrder(self, words):
        graph = {}
        lastWord = ''
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

            i = 0
            while i < len(lastWord) and i < len(word) and lastWord[i] == word[i]:
                i += 1
            if i < len(lastWord) and i < len(word):
    k/;
    kk7.\"0"
stack = []
        for node in graph:
            if self.toposort(node, graph, visited, stack) == False:
                return ""

        return ''.join(stack)[::-1]


