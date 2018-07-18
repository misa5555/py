class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def search_peak(lohi):
            lo, hi = lohi
            if lo > hi or lo < 0 or hi > len(nums) - 1:
                return -1
            mid = (lo + hi) // 2

            before_el, after_el = float('-inf'), float('-inf')
            if mid - 1 >= 0:
                before_el = nums[mid-1]
            if mid + 1 <= len(nums) - 1:
                after_el = nums[mid+1]

            if before_el < nums[mid] > after_el:
                return mid
            else:
                first_part = search_peak((0, mid-1))
                latter_part = search_peak((mid+1, len(nums)-1))
                if first_part != -1:
                    return first_part
                elif latter_part != -1:
                    return latter_part
                else:
                    return -1

        a = search_peak((0, len(nums)-1))
        return a

s = Solution()
print(s.findPeakElement([1,2,3]))
print(s.findPeakElement([1, 2, 3, 1])) # 2
print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4])) # 1 or 5
print(s.findPeakElement([2,1]))