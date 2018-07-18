class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_row = [1] * rows
        zero_col = [1] * cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_row[i] = 0
                    zero_col[j] = 0

        for i, n in enumerate(zero_row):
            if zero_row[i] == 0:
                for j in range(cols):
                    matrix[i][j] = 0

        for j, n in enumerate(zero_col):
            if zero_col[j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0
        print(matrix)
s = Solution()
s.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])