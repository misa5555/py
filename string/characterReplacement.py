class Solution:
    def _characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # s = "AABABBA", k = 1 => ans: 4

        start = 0
        end = start
        skip = k
        ans = 0
        while start < len(s) and end < len(s):
            if s[end] == s[start]:
                end += 1
            else:
                if skip > 0:
                    end += 1
                    skip -= 1
                else:
                    ans = max(ans, end - start)
                    start = end
                    end = start
                    skip = k
        ans = max(ans, end - start)
        return ans
    def characterReplacement(self, s, k):

s = Solution()
print(s.characterReplacement("AABABBA", 1))
print(s.characterReplacement("ABAB", 2))
print(s.characterReplacement("BAAA", 0))
print(s.characterReplacement("BAAA", 2))
