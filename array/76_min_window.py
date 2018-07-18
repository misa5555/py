class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # S = "ADOBECODEBANC", T = "ABC"
        from collections import Counter
        freq = Counter(t)
        count = len(t)
        l, r = 0, 0
        min_len = len(s) + 1
        ans = ''
        while r < len(s):
            if s[r] in freq:
                freq[s[r]] -= 1
                count -= 1

            r += 1

            while count == 0:
                if min_len > r - l:
                    min_len = r - l
                    ans = s[l:r]
                if s[l] in freq:
                    freq[s[l]] += 1
                    count += 1

                l += 1
        print(ans)
        return ans
s = Solution()
s.minWindow("ADOBECODEBANC", "ABC")
s.minWindow("a", "a")