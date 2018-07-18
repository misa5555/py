class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = {}
        def makeable(candidates, target, is_end):
            if is_end and dp.get(target):
                return dp.get(target)

            result = []
            if target == 0:
                return [[]]
            if target < 0:
                return False
            if len(candidates) >= 1 and candidates[0] > target:
                return False

            for i, c in enumerate(candidates):
                tmp = makeable(candidates[:i+1], target - c, i == len(candidates))
                if tmp != False:
                    result += [ _ + [c] for _ in tmp ]
            dp[target] = result
            return result

        ans = makeable(candidates, target, False)
        # print(ans)
        if not ans:
            return []
        return ans

s = Solution()

# s.combinationSum([1, 2], 2)
s.combinationSum([1, 2], 4)
s.combinationSum([2, 3, 6, 7], 7)
# s.combinationSum([7], 7)
