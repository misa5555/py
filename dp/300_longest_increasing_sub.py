class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]
        for i in range(1, len(nums)):
            tmp = dp
            for j, n in enumerate(dp):
                if j == 0:
                    tmp[j] = min(dp[j], nums[i])
                    continue
                else:
                    if nums[i] > dp[j-1] and nums[i] < dp[j]:
                        tmp[j] = nums[i]
            if dp[-1] < nums[i]:
                tmp.append(nums[i])
            dp = tmp

        print(dp)
        return len(dp)
s = Solution()
s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
s.lengthOfLIS([3,4,-1,5,8,2,3,7,9,10])


