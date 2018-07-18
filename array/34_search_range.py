class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0: return [-1, -1]
        # look for left hand
        start, end = -1, -1
        left, right = 0, len(nums) - 1
        min_right = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                if min_right == -1: min_right = mid
                if mid >= 1 and nums[mid-1] != target or mid == 0:
                    start = mid
                    break
                else:
                    right = mid - 1
        if start == -1:
            return [-1, -1]

        max_right = len(nums) - 1
        while min_right <= max_right:
            mid = (min_right + max_right) // 2
            if (mid + 1 < len(nums) and nums[mid] == target and nums[mid+1] != target) or mid == len(nums) - 1:
                end = mid
                break
            elif nums[mid] == target:
                min_right = mid + 1
            elif nums[mid] > target:
                max_right = mid - 1

        print([start, end])
        return [start, end]

s=Solution()
s.searchRange([5, 7, 7, 8, 8, 10], 8)
s.searchRange([5, 7, 7, 8, 10], 8)
s.searchRange([], 0)
s.searchRange([1], 0)
s.searchRange([2,2], 2)
s.searchRange( [1,4,4], 4)
s.searchRange([1,1,2],1)
s.searchRange([1,2,3,3,3,3,4,5,9],3)
s.searchRange([2,2], 3)
s.searchRange([0,0,0,1,2,3], 0)