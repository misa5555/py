class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #s = "mississippi"
        #p = "mis*is*p*."
        #"a*a*a*a*a*a*a*a*a*a*a*a*b"
        i = 0
        regex = []
        while i < len(p):
            if i < len(p) - 1 and p[i+1] == "*":
                if not regex or (regex and regex[-1] != p[i:i+2]):
                    regex.append(p[i:i+2])
                i += 2
            else:
                regex.append(p[i])
                i += 1

        from collections import defaultdict
        import string
        dp = defaultdict(list)
        dp[-1] = [-1]
        for i, sym in enumerate(regex):
            if sym in string.ascii_lowercase:
                dp[i] = list(set([j + 1 for j in dp[i-1] if j + 1 < len(s) and s[j+1] == sym]))
            elif sym == ".": # but not ".*"
                dp[i] = [idx + 1 for idx in dp[i-1]]
            else: # when sym is "a*"
                if len(sym) < 2:
                    return False
                matcher_str = sym[0]
                dp[i] = dp[i-1].copy()
                for prev in dp[i-1]:
                    tmpp = prev + 1
                    while tmpp < len(s) and (s[tmpp] == matcher_str or matcher_str == "."):
                        dp[i].append(tmpp)
                        tmpp += 1
        if len(s) - 1 in dp[len(regex)-1]:
            return True

        return False

s = Solution()
print(s.isMatch("aa", "a"))
print(s.isMatch("aa", "a*"))
print(s.isMatch("ab", ".*"))
print(s.isMatch("aab", "c*a*b"))
print(s.isMatch("mississippi", "mis*is*p*."))
print(s.isMatch("", "c*"))
print(s.isMatch("ab", ".*c"))

print(s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b"))



