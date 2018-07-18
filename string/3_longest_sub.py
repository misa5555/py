class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        ans = 0
        used = {}
        while i < len(s) - 1:
            j = i + 1
            tracker = set(s[i])
            while j < len(s):
                if j == len(s) - 1:
                    ans = max(ans, j - i + 1)
                    return ans
                if s[j] in tracker:
                    ans = max(ans, j - i)
                    i = j
                    break
                else:
                    tracker.add(s[j])
                    j += 1
        # return ans
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring("aab"))
