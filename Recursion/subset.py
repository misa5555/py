import copy;
class Solution:
    def _subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # def helper(nums):
        #     if not nums:
        #         return None
        #     if len(nums) == 1:
        #         return ["", str(nums[0])]
        #
        #     last_result = self.subsets(nums[:-1])
        #     ans = last_result.copy()
        #     target = str(nums[-1])
        #     for el in last_result:
        #         new_element = el + target
        #         if not new_element in ans:
        #             ans.append(new_element)
        #     return ans

        def subsets(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            def helper(nums):
                if not nums:
                    return None
                if len(nums) == 1:
                    return [[], [nums[0]]]

                last_result = self.subsets(nums[:-1])
                last_result_copy = copy.deepcopy(last_result)
                target = nums[-1]
                last_target = nums[-2]
                ans = []
                for el in last_result_copy:
                    if target != last_target:
                        el.append(target)
                        ans.append(el.copy())
                    else:
                        if len(el) >= 1 and el[-1] == target:
                            el.append(target)
                            ans.append(el.copy())
                last_result += ans
                return last_result
            nums.sort()
            return helper(nums)

s = Solution()
# print(s.subsets([1,2,3]))
print(s.subsets([1,2,2]))
