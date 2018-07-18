class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        stack = []
        def isOpen(p):
            return p == "{" or p == "[" or p == "("
        def isSameKind(a, b):
            return (ord(b) - ord(a)) <= 2

        for p in s:
            if isOpen(p):
                stack.append(p)
            else:
                if len(stack) > 0:
                    supposedOpen = stack.pop()
                    if not isSameKind(supposedOpen, p):
                        return False
                else:
                    return False
        print(stack)
        return len(stack) == 0
s = Solution()
ans = s.isValid("()[]{}")
print(ans)