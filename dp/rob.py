class Solution:
    def _rob(self, nums):
        last, now = 0, 0
        for i in nums: last, now = now, max(last + i, now)
        return now

    def rob(self, nums):
        if len(nums) <= 2:
            return 0
        if len(nums) == 3:
            return max(nums)
        from_zero = self._rob(nums)
        from_one = self._rob(nums[1:-1])
        ans = max(from_zero, from_one + nums[-1])
        return ans
