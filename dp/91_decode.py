class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        from string import ascii_lowercase
        data = [ ch for ch in ascii_lowercase ]

        dp = [-1] * (len(s) + 1)
        dp[0] = 1
        i = 1
        while i <= len(s):
            if i - 1 >= 0 and s[i] != "0":
               dp[i] = dp[i-1]
            if i - 2 >= 0 and 1 <= int(s[i-1:i+1]) <= 26:
               dp[i] += dp[i-2]
            if i == len(s):
                return dp[i]
            i += 1
s = Solution()
print(s.numDecodings("12"))