class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        from queue import PriorityQueue
        Counter(nums)
        q = PriorityQueue()
        for n in nums:
            q.get()
