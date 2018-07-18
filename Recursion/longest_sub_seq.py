#!/bin/python3

import sys

def longestCommonSubsequence(a, b):
    # Complete this function
    dp = [ [ 0 for x in range(len(b))] for y in range(len(a)) ]
    result = 0
    used = [False] * len(b)
    for i in range(len(a)):
        for j in range(len(b)):
            prev = max([0, dp[i-1][j]][i >= 1], [0, dp[i][j-1]][j >= 1])
            if a[i] == b[j]:
                if not used[j]:
                    dp[i][j] = prev + 1
                    used[j] = prev + 1
                else:
                    if used[j] - 1 > prev + 1:
                        dp[i][j] = used[j] - 1
                    else:
                        dp[i][j] = prev + 1
                        used[j] = prev + 1
                result = max(result, prev + 1)
            else:
                dp[i][j] = prev
    print(used)
    print(dp)
    print(result)
    return result

# longestCommonSubsequence('ABCDGH', 'AEDFHR')
longestCommonSubsequence('AGGTAB', 'GXTXAYB')
# if __name__ == "__main__":
#     n, m = input().strip().split(' ')
#     n, m = [int(n), int(m)]
#     a = list(map(int, input().strip().split(' ')))
#     b = list(map(int, input().strip().split(' ')))
#     result = longestCommonSubsequence(a, b)
#     print (" ".join(map(str, result)))


