class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif l <= mid - 1 and nums[l] <= nums[mid - 1]:
                if nums[l] <= target <= nums[mid - 1]:
                    r = mid - 1
                else:
                    l = mid + 1
                continue
            elif mid + 1 <= r and nums[mid + 1] <= nums[r]:
                if nums[mid + 1] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                continue
            else:
                break
        return -1
s = Solution()
print(s.search([3,4,5,6,7,8,1,2], 2))