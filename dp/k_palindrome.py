def kpalindrome(s, k):
    length = len(s)
    MAX = float('inf')
    dp = [[MAX for _ in range(length)] for _ in range(length)]
    for i in range(length):
        dp[i][i] = 0
        if i + 1 < length:
            dp[i][i + 1] = 0 if s[i] == s[i + 1] else 1
        if i + 2 < length:
            dp[i][i + 2] = 0 if s[i] == s[i+2] else 2


    for l in range(4, length+ 1):
        for i in range(length-l + 1):
            if i + l - 1 < length:
                dp[i][i+l-1] = min([dp[i+1][i+l-2] if s[i] == s[i+l-1] else MAX, dp[i][i+l-2] + 1, dp[i+1][i+l-1] + 1])

    return dp[0][-1] <= k
print(kpalindrome("abrarbra", 7))
print(kpalindrome("adbcdbacdb", 2))