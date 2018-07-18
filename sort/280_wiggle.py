class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        # if len(nums) == 3:
        #     nums[1], nums[2] = nums[2], nums[1]
        mid = len(nums) // 2 + len(nums) % 2
        i = 1
        j = mid
        if j % 2 == 1:
            j += 1

        while i < mid:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 2
            j += 2
        print(nums)
        # return nums


s = Solution()
s.wiggleSort([1,1,1,1]    )
s.wiggleSort([3, 5, 2, 1, 6, 4])
s.wiggleSort([3,2,1])
s.wiggleSort([1,1,1,1,2]) #expected [1,1,1,2,1]