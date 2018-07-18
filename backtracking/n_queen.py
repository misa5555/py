def nQueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    result = []
    from copy import deepcopy

    def cover(pos, board):
        i, j = pos
        b = deepcopy(board)
        b[i] = [1] * n
        for _i in range(n):
            b[_i][j] = 1
        l, m = i + 1, j + 1
        while 0 <= l < n and 0 <= m < n:
            b[l][m] = 1
            l += 1
            m += 1
        _l, _m = i - 1, j + 1
        while 0 <= _l < n and 0 <= _m < n:
            b[_l][_m] = 1
            _l -= 1
            _m += 1
        return b

    # col => 2 rows => [3, 1], board =>[[1, 1,1,1], [1,1,1,0], [1,1,1,1], [1,1,0,0]]
    def backtrack(col, rows, board):
        if col == n:
            result.append(rows)
            return

        for i in range(n):
            if board[i][col] == 0:
                new_board = cover((i, col), board)
                backtrack(col + 1, rows + [i+1], new_board)

    backtrack(0, [], board)
    return result
# print(nQueens(1))
# print(nQueens(4))
# print(nQueens(2))
print(nQueens(10))