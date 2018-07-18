from intervalUtil import *;

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda i: i.end)
        #   printIntervals(intervals)
        removed = [ False ] * len(intervals)
        for i in range(len(intervals)-1):
            if removed[i]:
                continue
            for j in range(i+1, len(intervals)):
                if removed[j]:
                    continue
                if intervals[j].start < intervals[i].end:
                    removed[j] = True
        return removed.count(True)
function = Solution().eraseOverlapIntervals

ary1=[[1,100],[11,22],[1,11],[2,12]]
print(execute(ary1, function))
