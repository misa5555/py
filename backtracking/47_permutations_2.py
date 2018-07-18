class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import Counter
        result = []
        def helper(freq, sub_ary, total):
            if total == 0:
                print(sub_ary)
                result.append(sub_ary)
                return
            for num in freq:
                if freq[num] > 0:
                    tmp = freq.copy()
                    tmp[num] -= 1
                    helper(tmp, [num] + sub_ary, total- 1)

        ans = helper(Counter(nums), [], len(nums))
        return result
s = Solution()
s.permuteUnique([1,1,2])