class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import defaultdict
        from collections import Counter


        lo, hi = 0, 0
        if len(t) == 1:
            return ["", t][t in s]
        if len(t) > len(s):
            return ""
        # set to st ore matched characters so far
        idx = []
        chr_counter = defaultdict(int)
        min_window = s
        while hi < len(s):
            if s[hi] in set(t):
                chr_counter[s[hi]] += 1
                idx.append(hi)
                if compare_hist(chr_counter, t):
                    while len(idx) >= 2:
                        min_window = [min_window, s[lo:hi+1]][len(min_window) > len(s[lo:hi+1])]
                        to_remove = idx.pop(0)
                        lo = idx[0]
                        chr_counter[s[to_remove]] -= 1
                        if chr_counter[s[to_remove]] == 0:
                            chr_counter.pop(to_remove, None)
                        lo += 1
            hi += 1
        return min_window
s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
# print(s.minWindow("a", "a"))
# print(s.minWindow("aa", "a"))
# print(s.minWindow("aa", "aa"))
# print(s.minWindow("ab", "a"))
# print(s.minWindow("a", "aa"))
# print(s.minWindow("bba", "ba"))
