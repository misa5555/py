from heapq import heappush, heappop, heapreplace, heapify
from queue import PriorityQueue
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.counter = 0
        self.q = PriorityQueue()

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.counter += 1
        self.q.put(num)

    def findMedian(self):
        """
        :rtype: float
        """


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()