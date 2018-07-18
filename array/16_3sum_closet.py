class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if sum(nums[0:3]) < target:
            return nums[0:3]
        if sum(nums[-3:]) > target:
            return nums[-3:]
        closet = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            t_sum = nums[i] + nums[l] + nums[r]
            if abs(t_sum - target) < abs(closet - target):
                closet = t_sum
            while l < r:
                if t_sum == target:
                    return (nums[i], nums[l], nums[r])
                elif t_sum < target:
                    l += 1
                else:
                    r -= 1
