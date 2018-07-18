class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        tmap = Counter(t)
        smap = Counter()
        i = 0
        count = 0
        min_len = float('inf')
        ans = ''
        for j in range(len(s)):
            smap[s[j]] += 1
            if tmap[s[j]] > 0 and smap[s[j]] <= tmap[s[j]]:
                count += 1

            if count == len(t):
                while tmap[s[i]] == 0 or smap[s[i]] > tmap[s[i]]:
                    if smap[s[i]] > tmap[s[i]]:
                        smap[s[i]] -= 1
                    i += 1
                len_window = j - i + 1
                if len_window < min_len:
                    min_len = len_window
                    ans = s[i:j+1]
        return ans
s = Solution()
s.minWindow("this is a test string", "tist")






