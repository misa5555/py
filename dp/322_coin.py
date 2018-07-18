class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [0] + [-1] * amount
        for co in coins:
            dp[co] = 1
        def helper(amt):
            if amt == 0:
                return 0
            if dp[amt] != -1:
                return dp[amt]

            if amt < 0 or amt < min(coins):
                return -1
            result = amt
            for c in coins:
                tmp = helper(amt - c)
                if tmp != -1:
                    result = min(tmp, result + 1)
            dp[amt] = result
            return result

        ans = helper(amount)
        return ans
s = Solution()
s.coinChange([1, 2, 5], 11)