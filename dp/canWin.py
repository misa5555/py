class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # (sum, possibleNums, turn)
        nums = list(range(maxChoosableInteger + 1, 0, -1))

        def dfs(SUM, nums, turn):
            if not nums and SUM < desiredTotal:
                return 'even'

            for n in nums:
                if n + SUM >= desiredTotal:
                    return turn
                _nums = nums[:]
                _nums.remove(n)
                result = dfs(n + SUM, _nums, turn + 1)

                if result == 'even':
                    return False
                elif result % 2 == 0:
                    return True
                elif result == 1:
                    return False

        return dfs(0, nums, 0)



s = Solution()
print(s.canIWin(3, 4))
print(s.canIWin(12, 49))