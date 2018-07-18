class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e


class Solution(object):

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def isOverlapped(a, b):
            return a.start <= b.end and b.start <= a.end

        def mergeArray(a, b):
            return Interval(min(a.start, b.start), max(a.end, b.end))

        if len(intervals) == 0:
            return [newInterval]

        result = []
        found = False
        finalPoint = 0
        i = 0
        newIntervalPushed = False
        for i, interval in enumerate(intervals):
            if isOverlapped(interval, newInterval):
                newInterval = mergeArray(interval, newInterval)
            else:
                if interval.start > newInterval.start:
                    result.append(newInterval)
                    newIntervalPushed = True
                    break
                else:
                    result.append(interval)
                    continue
        if not newIntervalPushed:
            result.append(newInterval)
        else:
            result += intervals[i:]
        return result

s = Solution()
ary1 = [[1,3],[6,9]]
ary2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
ary3 = [[0,3]]
def generateIntervals(ary):
    intervals = []
    for el in ary:
        intervals.append(Interval(el[0], el[1]))
    return intervals

intervals1 = generateIntervals(ary1)
intervals2 = generateIntervals(ary2)
result1 = s.insert(intervals1, Interval(2,5))
def printResult(ary):
    for el in ary:
        print([el.start, el.end])
    print("============= ")
printResult(result1)
ary2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
result2 = s.insert(intervals2, Interval(4,9))
printResult(result2)
#[1,2],[3,10],[12,16].
result3 = s.insert(generateIntervals([[1,5]]), Interval(2,3))
printResult(result3)

result4 = s.insert(generateIntervals([[1,5]]), Interval(2,7))
printResult(result4)
