class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from queue import PriorityQueue

        q = PriorityQueue()
        # need find m-th smallest element
        m = len(nums) - k + 1
        for n in nums:
            q.put(n)

        for i in range(m-1):
            q.get()

        return q.get()
s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2))