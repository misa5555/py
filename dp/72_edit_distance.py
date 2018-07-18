class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j] => minDistance(word1[0:i], word2[0:j])
        # dp[0][j] => minDistance("", word2[0:j]) => len(word2[0:j])
        # 0 <= i <= len(word), 0 <= j <= len(word2)
        dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for j in range(len(word2) + 1):
            dp[0][j] = len(word2[0:j])

        for i in range(len(word1) + 1):
            dp[i][0] = len(word1[0:i])
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

        # print(dp)
        return dp[-1][-1]
s = Solution()
s.minDistance("horse", "ros")
s.minDistance("intention", "execution")