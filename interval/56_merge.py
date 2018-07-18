# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        def merge(it1, it2):
            return Interval(min(it1.start, it2.start), max(it1.end, it2.end))

        def is_overlap(a, b):
            return a.start <= b.end and b.start <= a.end
        intervals = sorted(intervals, key=lambda i: i.start)

        result = []
        i = 0
        while i < len(intervals) - 1:
            j = i + 1
            while j < len(intervals) and is_overlap(intervals[i], intervals[j]):
                intervals[i] = merge(intervals[i], intervals[j])
                j += 1
            result.append(intervals[i])
            i = j

        ans=result + intervals[i:]
        return ans

a = [[1,3],[2,6],[8,10],[15,18]]
a = [[2,3],[4,5],[6,7],[8,9],[1,10]]
int = [ Interval(el[0], el[1]) for el in a ]
s = Solution()
s.merge(int)