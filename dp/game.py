class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def play(s):

            if not s in cache:
                can = any( s[i:i+2] == '++' and not play(s[:i] + '-' + s[i+2:]) for i in range(len(s)))
                cache[s] = can

            return cache[s]

        cache = {}
        minus = '-' * len(s)
        cache[minus] = False
        return play(s)
s = Solution()
print(s.canWin('++++'))
print(s.canWin("++++++"))