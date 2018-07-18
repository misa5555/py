class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) == 1:
            return [nums]
        ans = []
        for i, n in enumerate(nums):
            ans += [ x + [n] for x in self.permute(nums[0:i] + nums[i+1:])]
        # print(ans)
        return ans

s = Solution()
s.permute([1])
s.permute([1,2])
a = s.permute([1,2,3])
print(a)
