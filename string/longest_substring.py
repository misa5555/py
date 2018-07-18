class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        # index checker
        checker = {}
        ans = 0
        while i < len(s):
            j = i
            checker = {}
            while j < len(s):
                if s[j] in checker:
                    break
                checker[s[j]] = j
                j += 1
            ans = max(j-i, ans)
            i += 1
        return ans
s = Solution()
re1 = s.lengthOfLongestSubstring("abcabcbb")
re2 = s.lengthOfLongestSubstring("bbbbbbb")
re3 = s.lengthOfLongestSubstring("pwwkew")
re4 = s.lengthOfLongestSubstring("dvdf")


print(re1)
print(re2)
print(re3)
print(re4)
