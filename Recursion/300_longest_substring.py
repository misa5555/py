class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [10, 9, 2, 5, 3, 7, 101, 18]
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i, n in enumerate(nums):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])

        print(dp)
        return max(dp)

s = Solution()
s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
s.lengthOfLIS([3,4,-1,0,6,2,3])
s.lengthOfLIS([1,3,6,7,9,4,10,5,6])