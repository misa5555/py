class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tmp_sum = nums[i] + nums[l] + nums[r]
                if tmp_sum == 0:
                    result.add((nums[i], nums[l] , nums[r]))
                    l += 1
                    r -= 1
                elif tmp_sum > 0:
                    r -= 1
                else:
                    l += 1

        tmp = list(result)
        return [list(t) for t in tmp]
s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0,0,0]))
print(s.threeSum([-2,0,0,2,2]))

