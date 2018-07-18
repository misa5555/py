def bomber(field):
    row_dp = [[0 for _ in range(len(field[0]))] for _ in range(len(field))]
    col_dp = [[0 for _ in range(len(field))] for _ in range(len(field[0]))]

    def count(row, dp_row):
        crt = 0
        for j in range(len(row)):
            if row[j] == 'E':
                crt += 1
            elif row[j] == 'W':
                crt = 0
            else:
                dp_row[j] = crt

    def reverse_count(row, dp_row):
        crt = 0
        for j in range(len(row) - 1, -1, -1):
            if row[j] == 'E':
                crt += 1
            elif row[j] == 'W':
                crt = 0
            else:
                dp_row[j] += crt

    for i, row in enumerate(field):
        count(row, row_dp[i])
        reverse_count(row, row_dp[i])

    _field = list(zip(*field))

    for j, column in enumerate(_field):
        count(column, col_dp[j])
        reverse_count(column, col_dp[j])

    print(row_dp)
    print(col_dp)
    ans = 0
    for i in range(len(field)):
        for j in range(len(field[0])):
            print((i, j))
            ans = max(row_dp[i][j] + col_dp[j][i], ans)
    print(ans)
    return ans

field = [["0", "0", "E", "0"],
         ["W", "0", "W", "E"],
         ["0", "E", "0", "W"],
         ["0", "W", "0", "E"]]
_field = [["0", "0", "E", "0", "E"],
         ["W", "0", "W", "E", "0"],
         ["0", "E", "0", "W", "0"],
         ["0", "W", "0", "E", "0"]]
f3 =  [["E"],
 ["E"],
 ["E"]]
# bomber(field)
# bomber(_field)
bomber(f3)
