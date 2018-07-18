class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        def is_vowel(ch):
            return ch.lower() in ["a", "e", "o", "i", "u"]

        lo, hi = 0, len(s) - 1

        while lo < hi:
            while lo < hi and not is_vowel(s[lo]):
                lo += 1

            while lo < hi and not is_vowel(s[hi]):
                hi -= 1

            s = list(s)
            s[lo], s[hi] = s[hi], s[lo]
            s = ''.join(s)
            lo += 1
            hi -= 1

        return s

s = Solution()
s.reverseVowels()