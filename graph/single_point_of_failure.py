# https://codefights.com/interview-practice/task/qmKLsQcqeEBckLx2q
def singlePointOfFailure(connections):
    from collections import defaultdict
    graph = defaultdict(list)
    for i in range(len(connections)):
        for j in range(len(connections)):
            if connections[i][j] == 1:
                graph[i].append(j)

    def dfs(node, ignore, visited):
        visited.add(node)

        for nei in graph.get(node):
            if nei not in visited:
                return dfs(nei, ignore, visited)
        return

    ans = 0
    for n1, v in graph.items():
        for n2 in v:
            visited = set()
            ignore = (n1, n2)
            graph[n1].remove(n2)
            graph[n2].remove(n1)
            dfs(n1, ignore, visited)
            if len(visited) != len(connections[0]) - 1:
                ans += 1
            graph[n1].append(n2)
            graph[n2].append(n1)

    return ans

print(singlePointOfFailure([[0, 1, 1], [1, 0, 1], [1, 1, 0]]))
print(singlePointOfFailure([[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]]))

