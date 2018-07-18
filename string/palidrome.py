class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1 = 0
        p2 = len(s) - 1
        if len(s) < 2:
            return True
        import string
        numlist = list(map(str, range(10)))
        while p2 > p1:
            s1 = s[p1].lower()
            s2 = s[p2].lower()
            if not s1 in string.ascii_lowercase and not s1 in numlist:

                p1 += 1
                continue
            if not s2 in string.ascii_lowercase and not s2 in numlist:
                p2 -= 1
                continue
            if s1 != s2:
                return False
            else:
                p1 += 1
                p2 -= 1
        return True
s = Solution()
a1 = s.isPalindrome("A man, a plan, a canal: Panama")
print(a1)

a2 = s.isPalindrome("race a car")
print(a2)

a3 = s.isPalindrome(".,")
print(a3)