class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        n, tgt = maxChoosableInteger, desiredTotal
        sums = sum(range(1, n + 1))
        if sums < tgt: return False
        if sums == tgt: return n & 1 == 1
        dp = dict()
        unused = [True] * n

        def dfs(st, tgt):
            if st in dp: return dp[st]
            for i in range(n - 1, -1, -1):
                if unused[i]:
                    if i + 1 >= tgt:
                        dp[st] = True
                        return True
                    unused[i] = False
                    if not dfs(st | (1 << i), tgt - i - 1):
                        dp[st] = True
                        unused[i] = True
                        return True
                    unused[i] = True
            dp[st] = False
            return False

        return dfs(0, tgt)


class Solution:
    def canIWin(self, choose, total):
        if choose * (choose + 1) / 2 < total: return False
        memo = {}

        def dp(cur, used):
            if used in memo:
                return memo[used]
            else:
                for i in range(choose, 0, -1):
                    if not used & (1 << i):
                        if cur + i >= total:
                            memo[used] = True
                            return True
                        if not dp(cur + i, used | (1 << i)):
                            memo[used] = True
                            return True
                memo[used] = False
                return False

        return dp(0, 1)

