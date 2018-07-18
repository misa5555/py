class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        tipping_point = 0
        for i in reversed(range(1, length)):
            if nums[i] > nums[i-1]:
                tipping_point = i
                break

        if tipping_point > 0:
            pivot = nums[tipping_point - 1]
            closet_bigger_pivot = nums[tipping_point]
            idx_to_exchange = tipping_point
            for j in range(tipping_point, length):
                if nums[j] > pivot and nums[j] < closet_bigger_pivot:
                    closet_bigger_pivot = nums[j]
                    idx_to_exchange = j
            nums[tipping_point - 1], nums[idx_to_exchange] = nums[idx_to_exchange], nums[tipping_point - 1]
        for i in range(length - tipping_point):
            for j in range(tipping_point, length - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        print(nums)
        return nums

s= Solution()
s.nextPermutation([1,2,9,3,1])
s.nextPermutation([2,3,1])
s.nextPermutation([1,2,3])
s.nextPermutation([3,2,1])
s.nextPermutation([1,1,5])