#Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # pos: (i, j)
        def setRowToAllZero(matrix, i):
            rows = len(matrix[0])
            allZeroRow = tuple( 0 for _ in range(rows) )
            matrix[i] = allZeroRow

        # check each row in matrix
        # if a row contain 0 as element, row idx should be stored.
        def checkEachRow(matrix):
            rows = len(matrix)
            zeroRowIdx = []
            for i in range(rows):
                if 0 in set(matrix[i]):
                    zeroRowIdx.append(i)
            return zeroRowIdx

        rowIdxToZero = checkEachRow(matrix)
        matrix = list(zip(*matrix))
        columnIdxToZero = checkEachRow(matrix)
        matrix = list(zip(*matrix))
        print(matrix)
        matrix = list(map(list, matrix))
        for i in rowIdxToZero:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        for j in columnIdxToZero:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        print(matrix)
s = Solution()
matrix = [[1, 0, 2, 3], [0, 3, 0, 4], [1, 2, 3, 4], [5,6,7,8]]
matrix2 = [[1,0]]
s.setZeroes(matrix)
s.setZeroes(matrix2)
