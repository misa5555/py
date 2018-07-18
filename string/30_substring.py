class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        def isValid(s, l):
            ws = Counter(words)
            i = 0
            while i + l - 1 < len(s):
                if s[i:i+l] in ws:
                    ws[s[i:i+l]] -= 1
                    if ws[s[i:i+l]] < 0:
                        return False
                    i += l
                else:
                    return False
            for k, v in ws.items():
                if v != 0:
                    return False
            return True


        l = len(words[0])
        l_sum = sum([len(w) for w in words])
        i = 0
        result = []
        for j in range(len(s)):
            if j - i + 1 < l_sum:
                continue
            print(isValid(s[i:j+1], l))
            if isValid(s[i:j+1], l):
                result.append(i)
            i += 1
        return result
s = Solution()
# s.findSubstring("barfoothefoobarman", ["foo","bar"])
print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))

