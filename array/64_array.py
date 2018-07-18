class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # dp = [grid[0]] + [[grid[y][0]] + [-1 for x in range(n - 1)] for y in range(1, m)]
        dp = [[ -1 for x in range(n)] for y in range(m)]
        dp[0][0] = grid[0][0]
        print(dp)
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                print((i,j))
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        print(dp[-1][-1])
        return dp[-1][-1]

s = Solution()
grid = \
[[1,3,1],
 [1,5,1],
 [4,2,1]]
g2 = [[1,2,5],[3,2,1]]
s.minPathSum(grid)
s.minPathSum(g2)