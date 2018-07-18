class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        """
        min_len = min(len(w) for w in wordDict if w)
        max_len = max(len(w) for w in wordDict if w)

        wordDict = set(wordDict)

        result = []
        def traverse(st, so_far):
            if not st:
                if len(so_far) >= 1 and so_far[0] == " ":
                    print(so_far)
                    result.append(so_far[1:])
                    return 1
                return -1
            for i in range(min_len, max_len+1):
                tmp = so_far
                if st[0:i] in wordDict:
                    tmp += " " + st[0:i]
                    traverse(st[i:], tmp)
            return -1
        traverse(s, "")
        return result
s = Solution()
print(s.wordBreak("", ["a"]))
# print(s.wordBreak("a", []))
print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
s1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
d = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(s.wordBreak(s1, d))