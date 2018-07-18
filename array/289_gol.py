class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row, column = len(board), len(board[0])
        vector = [(1,0), (0,1), (-1,0), (0, -1), (-1, 1), (-1, -1), (1, -1), (1,1)]
        for i in range(row):
            for j in range(column):
                neighbors = 0
                for v in vector:
                    _i, _j = i + v[0], j + v[1]
                    if 0 <= _i < row and 0 <= _j < column:
                        neighbors += board[_i][_j] & 1
                if ( board[i][j] & 1 ) == 1:
                    if 2 <= neighbors <= 3:
                        board[i][j] += 2
                else:
                    if neighbors == 3:
                        board[i][j] += 2

        for i in range(row):
            for j in range(column):
                board[i][j] >>= 1

