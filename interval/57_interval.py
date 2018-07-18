# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def print_func(intervals):
            print([(int.start, int.end) for int in intervals])

        def isOverlap(int1, int2):
            return int1.start < int2.end and int2.start < int1.end

        def mergeOverlap(int1, int2):
            return Interval(min(int1.start, int2.start), max(int1.end, int2.end))
        start = -1
        end = -1
        for i, interval in enumerate(intervals):
            if isOverlap(interval, newInterval):
                start = i
                intervals[i] = mergeOverlap(interval, newInterval)
                if i < len(intervals) - 1:
                    j = i + 1
                    while j < len(intervals) and isOverlap(intervals[i], intervals[j]):
                        intervals[i] = mergeOverlap(intervals[i], intervals[j])
                        j += 1
                    end = j
                break
        if start >= 0:
            print_func(intervals)
            ans = intervals[:start+1] + intervals[end:]
            print_func(ans)
            return ans
        else:
            return intervals
s = Solution()
ary = [[1,3],[6,9]]
int1 = [ Interval(el[0], el[1]) for el in ary ]
new1 = Interval(2, 5)
s.insert(int1, new1)
ary2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
int2 = [ Interval(el[0], el[1]) for el in ary2 ]
new2 = Interval(4,9)
s.insert(int2, new2)