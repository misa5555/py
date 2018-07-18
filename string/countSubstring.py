# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if i == j or (j - i == 1 and s[i] == s[j]) or (s[i] == s[j] and dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    ans += 1
        return ans

s = Solution()
a1 = s.countSubstrings("abc")
print(a1)

a2 = s.countSubstrings("aaa")
print(a2)