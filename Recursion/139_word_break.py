class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        # s = "leetcode",
        # dict = ["leet", "code"].
        #
        # Return true because "leetcode" can be segmented as "leet code".
        if len(wordDict) == 0:
            return False
        checker = set(wordDict)
        dp = [False] * len(s)
        i = 0
        while i < len(s):
            j = i
            while j >= 0:
                if j == 0 or (j >= 1 and dp[j-1] == True):
                    if s[j:i+1] in checker:
                        dp[i] = True
                        break
                j -= 1
            i += 1

        print(dp)
        return dp[-1]
s = Solution()
s.wordBreak("leetcode", ["leet", "code"])
s.wordBreak("aaaaaaa", ["aaaa","aaa"])