class Solution:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """

        def matchMaker(stage):
            if stage == 0:
                return f"({','.join(list(range(1, n + 1)))})"
            previous = matchMaker(stage - 1)
            mid = len(previous) // 2
            result = []
            for i in range(mid):
                result.append((previous[i], previous[len(previous) - i - 1]))
            return result

        from math import log2
        ans = matchMaker(log2(n))[0]

        return ans

s= Solution()
# ans = s.findContestMatch(8)
ans = s.findContestMatch(16)
print(ans)