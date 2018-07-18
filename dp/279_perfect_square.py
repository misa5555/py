class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        nums = [x ** 2 for x in range(1, int(math.sqrt(n)) + 1)]

        dp = [0] * (n + 1)
        for j in nums:
            dp[j] = 1
        for i in range(2, n+1):
            if dp[i] == 1:
                continue
            for j in nums:
                if i - j >= 0:
                    if dp[i-j] == 1:
                        dp[i] = 2
                        break
                    else:
                        if dp[i] == 0:
                            dp[i] = dp[i-j] + 1
                        else:
                            dp[i] = min(dp[i], dp[i-j] + 1)
        print(dp)
        return dp[-1]
s = Solution()
# print(s.numSquares(1))
# print(s.numSquares(12))
print(s.numSquares(7927))
