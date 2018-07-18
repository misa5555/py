# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        def helper(left, right):
            if s[left] == s[right]:
                if left - 1 >= 0 and right + 1 < len(s):
                   return helper(left - 1, right + 1)
                else:
                    return (left, right)
            else:
                return (left + 1, right - 1)
        ans = 0
        result = ''
        def length(tuple):
            return tuple[1] - tuple[0] + 1

        for i in range(len(s)-1):
            tmp = helper(i, i+1)
            if length(tmp) > ans:
                result = s[tmp[0]:tmp[1]+1]
                ans = length(tmp)
            if i + 2 < len(s):
                tmp = helper(i, i+2)
                if length(tmp) > ans:
                    result = s[tmp[0]:tmp[1]+1]
                    ans = length(tmp)

        return result

s = Solution()
ans1 = s.longestPalindrome("babad")
ans2 = s.longestPalindrome("baabad")
print(ans1)
print(ans2)

