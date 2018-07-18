class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def parse(trange):
            if trange[0] == trange[1]:
                return [str(trange[0])]
            else:
                return [trange[0] + "->" + trange[1]]

        if len(nums) == 1:
            return nums
        ans = []
        tmp_range = (nums[0], nums[0])
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                tmp_range = (tmp_range[0], nums[i])
            else:
                ans.append(parse(tmp_range))
                tmp_range = (nums[i], nums[i])
        ans.append(parse(tmp_range))
        return ans
s = Solution()
s.summaryRanges([0,1,2,4,5,7])
s.summaryRanges([0,2,3,4,6,8,9])