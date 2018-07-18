class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            else:
                j = i
                while j < len(s) and s[j] != ' ':
                    j += 1
                result = j - i
                i = j
        return result
s = Solution()

print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("b   a    "))