class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        """
        if not s:
            return []
        dp = {}
        def dfs(i):
            if dp.get(i):
                return dp[i]
            if i == -1:
                return [""]
            result = []
            found = False
            for w in wordDict:
                if i-len(w)+1 >= 0 and i < len(s) and s[i-len(w)+1:i+1] == w:
                    past = dfs(i - len(w))
                    if past:
                        found = True
                    result += [t + ' ' + w if t else w for t in past]
            if not found:
                result = []
            dp[i] = result
            return result
        ans = dfs(len(s)-1)
        # print(ans)
        return ans

s = Solution()
# print(s.wordBreak("", ["a"]))
# print(s.wordBreak("a", []))
# print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
# print(s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
s1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
d = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# print(s.wordBreak(s1, d))
s2 = "aaaaaaa"
d2 = ["aaaa","aaa"]
print(s.wordBreak(s2, d2))
