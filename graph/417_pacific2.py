class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(matrix), len(matrix[0])

        p = []
        a = []
        for i in range(row):
            p.append((i, 0))
            a.append((i, col-1))
        for j in range(col):
            p.append((0, j))
            a.append((row-1, j))

        pmap = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        pmap[0] = [1 for _ in matrix[0]]
        for i in range(row):
            pmap[i][0] = 1

        amap = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        amap[-1] = [1 for _ in matrix[0]]
        for i in range(row):
            amap[i][-1] = 1

        def dfs(pos, omap):
            print(pos)
            i, j = pos
            if i < 0 or i >= row or j < 0 or j >= col:
                return False

            omap[i][j] = 1
            [dfs((_pos[0], _pos[1]), omap) for _pos in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] if
                    0<= _pos[0] < row and 0<= _pos[1] < col and matrix[_pos[0]][_pos[1]] >= matrix[i][j] and omap[_pos[0]][_pos[1]] == 0]



        for pa in a:
            dfs(pa, amap)
        for pp in p:
            dfs(pp, pmap)
        print(amap)
        print(pmap)
        result = []
        for i in range(row):
            for j in range(col):
                if amap[i][j] == 1 and pmap[i][j] == 1:
                    result.append((i, j))
        return result
matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
s = Solution()
# s.pacificAtlantic(matrix)
m2 = [[10,10,10],[10,1,10],[10,10,10]]
s.pacificAtlantic(m2)