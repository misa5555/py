class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # create graph from prerequisites
        from collections import defaultdict
        graph = defaultdict(list)
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])

        visited = [-1] * ( numCourses)
        def cycle(n):
            visited[n] = 0
            for nei in graph[n]:
                if visited[nei] == 1:
                    continue
                if visited[nei] == 0:
                    return True
                if cycle(nei):
                    return True
            visited[n] = 1
            return False

        #print(graph) {0: [1, 3], 1: [2, 3], 2: [0]})
        for i in range(numCourses):
            if cycle(i) == True:
                return False
        return True




s= Solution()
ans = s.canFinish(4, [[1,0],[2,1],[0,2],[3,1],[3,0]])
print(ans) # False
print(s.canFinish(2, [[1,0]])) # True
print(s.canFinish(2, [[1,0], [0, 1]])) # False
print(s.canFinish(3, [[0,1],[0,2],[1,2]])) # True
print(s.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]])) #False