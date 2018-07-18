def maximalSquare(matrix):
    if not matrix:
        return 0
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        dp[i][0] = int(matrix[i][0])

    for j in range(len(matrix[0])):
        dp[0][j] = int(matrix[0][j])

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    print(dp)
    maxn = 0
    max_i, max_j = 0, 0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j] > maxn:
                max_i, max_j = i, j
                maxn = dp[i][j]

    i, j  = max_i, max_j
    while i >= 0 and j >= 0:
        if matrix[i][j] == '1':
            i -= 1
            j -= 1
        else:
            break

    return (max_i - i) * (max_j - j)

m = [
 ["1","0","1","1","1"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"],
 ["1","0","0","1","0"]]
print(maximalSquare(m))

m2 = [
 ["0","0","0","1"],
 ["1","1","0","1"],
 ["1","1","1","1"],
 ["0","1","1","1"],
 ["0","1","1","1"]]
print(maximalSquare(m2))