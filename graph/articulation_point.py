from collections import defaultdict
def singlePointOfFailure(connections):
    graph = defaultdict(list)
    for i in range(len(connections)):
        for j in range(len(connections[0])):
            if connections[i][j] == 1: graph[i].append(j)

    def helper(u, visited, parent, lower, discover, ap, time):
        # count of children for node u
        children = 0
        visited[u] = True

        # initiate discover time and lower time
        discover[u] = time
        lower[u] = time
        time += 1

        for v in graph.get(u):
            if visited[v] == False:
                parent[v] = u
                children += 1
                helper(v, visited, parent, lower, discover, ap, time)
                lower[u] = min(lower[u], lower[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and lower[v] >= discover[u]:
                    ap[u] = True

            elif v != parent[u]:
                lower[u] = min(lower[u], discover[v])

    V = len(connections)
    visited = [False] * V
    parent = [-1] * V
    discover = [float('inf')] * V
    lower = [float('inf')] * V
    ap = [False] * V
    for i in range(V):
        if visited[i] == False:
            helper(i, visited, parent, lower, discover, ap, 0)
    return ap
print(singlePointOfFailure([[0, 1], [1, 0]]))
print(singlePointOfFailure([[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]]))

