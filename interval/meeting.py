from intervalUtil import *;

# ary = [[10, 12], [1,3]]
# intervals = generateIntervals(ary)
# printIntervals(intervals)
# sortedInt = sorted(intervals, key=lambda i: i.start)
# printIntervals(sortedInt)
class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        def isOverlapped(a, b):
            return a.start < b.end and b.start < a.end

        sortedIntervals = sorted(intervals, key=lambda i: i.start)
        for i in range(len(intervals) - 1):
            if isOverlapped(sortedIntervals[i], sortedIntervals[i+1]):
                return False
        return True

    def minMeetingRooms_(self, intervals):
        if len(intervals) <= 1:
            return len(intervals)

        intervals = sorted(intervals, key=lambda i: i.start)
        # printIntervals(intevals)
        meetingRooms = 1
        ans = 1
        for i in range(len(intervals)):
            roomCount = 1
            for j in range(0, i):
                if intervals[j].end > intervals[i].start:
                    roomCount += 1
            ans = max(ans, roomCount)
        return ans


    def minMeetingRooms(self, intervals):
        if len(intervals) <= 1:
            return len(intervals)

        # intervals = sorted(intervals, key=lambda i: i.start)
        # printIntervals(intervals)
        meetingRooms = 1
        ans = 1
        for i in range(len(intervals)):
            roomCount = 1
            for j in range(len(intervals)):
                if i == j:
                    continue
                if intervals[j].start <= intervals[i].start and intervals[j].end > intervals[i].start:
                    roomCount += 1
            ans = max(ans, roomCount)
        return ans
s = Solution()
def execute(ary):
    intervals = generateIntervals(ary)
    print(s.minMeetingRooms(intervals))

execute([[0, 30],[5, 10],[15, 20]])
execute([[5,8],[6,8]])
execute([[2,11],[6,16],[11,16]])
