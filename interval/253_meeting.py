# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        import heapq
        q = []
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals)):
            if q and intervals[i].start >= q[0]:
                heapq.heapreplace(q, intervals[i].end)
            else:
                heapq.heappush(q, intervals[i].end)

        return len(q)


s = Solution()
ary = [[0, 30],[5, 10],[15, 20]]
ary1 = [[13,15],[1,13]]
ary2 = [[4,18],[1,35],[12,45],[25,46],[22,27]]
int2 = [ Interval(el[0], el[1]) for el in ary ]
def print_ans(ary):
    int2 = [Interval(el[0], el[1]) for el in ary]
    print(s.minMeetingRooms(int2))
print_ans(ary)
print_ans(ary1)
print_ans(ary2)
print_ans([[15,16],[10,15],[16,25]])