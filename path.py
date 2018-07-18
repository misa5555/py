class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """


        def nextSteps(cor, grid):
            rows = len(grid)
            columns = len(grid[0])
            possibleMoves = []
            steps = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for step in steps:
                if 0 <=  cor[0] + step[0] < rows and 0 <= cor[1] + step[1] < columns and grid[cor[0] + step[0]][cor[1] + step[1]] == "1":
                    possibleMoves.append((cor[0] + step[0], cor[1] + step[1]))

            return possibleMoves

        def search(startCor, grid, visited):
            queue = [startCor]
            size = len(grid) * len(grid[0])
            while len(queue) > 0:
                #print(queue)
                targetCor = queue.pop(0)
                #print(visited)
                if targetCor in visited:
                    continue
                nextMoves = nextSteps(targetCor, grid)
                visited.add(targetCor)
                for nextCor in nextMoves:
                    if not nextCor in visited:
                        queue.append(nextCor)

            return visited

        if len(grid) == 0: return 0;
        rows = len(grid)
        columns = len(grid[0])
        visited = set([])
        count = 0

        for i in range(rows):
            for j in range(columns):
                if not (i, j) in visited and grid[i][j] == "1":
                    visitedFromThisSearch = search((i, j), grid, visited)
                    visited = visited.union(visitedFromThisSearch)
                    count += 1


        return count
s = Solution()
ary =[
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]]
ary2 = [
['1', '1', '0', '0', '0'],
['1', '1', '0', '0', '0'],
['0', '0', '1', '0', '0'],
['0', '0', '0', '1', '1']]
ary3 = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
ary4 = [["1"]]
ary5 = [
["1","1","1"],
["0","1","0"],
["1","1","1"]]
print(s.numIslands(ary))
print(s.numIslands(ary2))
print(s.numIslands(ary3))
print(s.numIslands(ary4))
