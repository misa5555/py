from collections import defaultdict
def feedingTime(classes):
    parent = [-1] * len(classes)

    def find_parent(node):
        if parent[node] != -1:
            find_parent(parent[node])
        else:
            return node

    def union(n1, n2):
        if len(set(n1).intersection(set(n2))) > 0:
            p1 = find_parent(n1)
            parent[n2] = p1


    for i in range(len(classes)):
        for j in range(i):




