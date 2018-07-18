# code

dp = [0] + [-1] * cap


def calc(vals, weis, cap):
    value_store = {}
    for i, w in enumerate(weis):
        value_store[w] = vals[i]

    for i in range(1, cap):
        dp[i] = max([dp[i - w] + value_store[w] if i - w >= 0 else -1 for w in weis]) +

    return dp[cap]

calc()