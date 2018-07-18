class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        dp = [[ int(cell) for cell in row ] for row in matrix]
        for r in range(row):
            for c in range(col):
                if c >= 1 and dp[r][c] == 1 and dp[r][c-1] > 0:
                    dp[r][c] = dp[r][c-1] + 1

        stack_dp = list(zip(*dp))
        ans = 0
        for j in range(col):
            stack = list(stack_dp[j])
            min_wid = float('inf')
            height = 0
            for height in stack:
            while stack:
                tmp = stack.pop()
                height += 1
                if tmp == 0:
                    height = 0
                    min_wid = float('inf')
                    continue

                min_wid = min(min_wid, tmp)

                ans = max(ans, min_wid * height)
        print(ans)
        return ans


matrix = [ ["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
s = Solution()
# s.maximalRectangle(matrix)
matrix2 = [ ["1","0","1","0","0"],
           ["1","0","1","1","1"],
           ["1","1","1","1","1"]]
# s.maximalRectangle(matrix2)
matrix3 = [["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]
# s.maximalRectangle(matrix3)
matrix4 = [["0","0","0","1","0","1","1","1"],["0","1","1","0","0","1","0","1"],["1","0","1","1","1","1","0","1"],["0","0","0","1","0","0","0","0"],["0","0","1","0","0","0","1","0"],["1","1","1","0","0","1","1","1"],["1","0","0","1","1","0","0","1"],["0","1","0","0","1","1","0","0"],["1","0","0","1","0","0","0","0"]]
# s.maximalRectangle(matrix4)
matrix5 = [
    ["0","1","1","0","0","1","0","1","0","1"],
    ["0","0","1","0","1","0","1","0","1","0"],
    ["1","0","0","0","0","1","0","1","1","0"],
    ["0","1","1","1","1","1","1","0","1","0"],
    ["0","0","1","1","1","1","1","1","1","0"],
    ["1","1","0","1","0","1","1","1","1","0"],
    ["0","0","0","1","1","0","0","0","1","0"],
    ["1","1","0","1","1","0","0","1","1","1"],
    ["0","1","0","1","1","0","1","0","1","1"]]
s.maximalRectangle(matrix5)
