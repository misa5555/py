class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0, p2 = 0, len(nums) - 1
        for i, n in enumerate(nums):
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1

        for j, n in reversed(list(enumerate(nums))):
            if n == 2:
                nums[p2], nums[j] = nums[j], nums[p2]
                p2 -= 1

        print(nums)
        return nums

s = Solution()
s.sortColors([1,2,0])
s.sortColors([0,0,1,0,2,1,2])
s.sortColors([0,0,1,0,2, 0, 1])
s.sortColors([1,1,0,1,2,0,2])
