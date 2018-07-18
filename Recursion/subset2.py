import copy;
class Solution:
    def subsetsWithDup(self, nums):
        ans = []
        nums.sort()
        def helper(nums, ans):
            if len(nums) == 1:
                result = [[], [nums[0]]]
                ans += result
                return result

            previous_ans = helper(nums[:-1], ans)
            if nums[-1] == nums[-2]:
                previous_ans_copy = copy.deepcopy(previous_ans)
                if len(previous_ans_copy[0]) == 0:
                    previous_ans_copy.pop(0)
            else:
                previous_ans_copy = copy.deepcopy(ans)
            new_element = []
            for ary in previous_ans_copy:
                ary.append(nums[-1])
                new_element.append(ary)
            ans += new_element

            return new_element

        ans = []
        helper(nums, ans)
        return ans
s = Solution()
print(s.subsetsWithDup([1,2,3]))
print(s.subsetsWithDup([1,2,2]))
print(s.subsetsWithDup([2,2,2]))
print(s.subsetsWithDup([5,5,5,5]))
print(s.subsetsWithDup([5,5,5,5,5]))
