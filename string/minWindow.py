class Solution:
    # or example,
    # S = "ADOBECODEBANC"
    # T = "ABC"
    # Minimum
    # window is "BANC".

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tracker = {}
        re_starting_point = 0
        min_len = 0
        index = []
        ans = ""
        for i, ch in enumerate(s):
            if ch in t:
                index.append(ch)
                tracker[ch] = i
                if len(tracker) == len(t):
                    re_starting_point = i + 1
                    ans = s[tracker[index[0]]:tracker[index[-1]]+1]
                    break
        print(ans)
        if len(tracker) < len(t):
            return ""
        elif re_starting_point == len(s) + 1:
            start = index[0]
            end = index[-1]
            return s[start:end+1]
        for j in range(re_starting_point, len(s)):
            if s[j] in t:

                index.append(s[j])
                tracker[s[j]] = j
                print(index)
                print(tracker)
                if index[0] == s[j]:
                    index.pop(0)
                    start = tracker[index[0]]
                    end = tracker[index[-1]]
                    if end - start + 1 < len(ans):
                        ans = s[start:end+1]

        return ans



s = Solution()
ans = s.minWindow("ADOBECODEBANC", "ABC")
print(ans)