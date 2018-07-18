class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [True] + [False for i in s]
        words = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in words:
                    dp[i] = True and dp[j]
                    if dp[i]:
                        break
        if not dp[len(s)]:
            return []

        maxLen = max(map(len, wordDict))

        def construct(s, words, dp, maxLen, cache, idx):
            if cache[idx]:
                return cache[idx]
            for i in range(idx - 1, max(idx - maxLen - 1, -1), -1):
                if s[i:idx] in words and dp[i]:
                    if i == 0:
                        cache[idx].append(s[:idx])
                    else:
                        for w in construct(s, words, dp, maxLen, cache, i):
                            cache[idx].append(w + " " + s[i:idx])
            return cache[idx]

        cache = [[] for i in dp]
        construct(s, words, dp, maxLen, cache, len(s))
        return cache[len(s)]