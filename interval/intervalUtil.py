class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def generateIntervals(ary):
    ints = []
    for el in ary:
        ints.append(Interval(el[0], el[1]))
    return ints

def printIntervals(intervals):
    print([(itv.start, itv.end) for itv in intervals])


def isOverlapped(a, b):
    return a.start <= b.end and b.start <= a.end

def mergeArray(a, b):
    return Interval(min(a.start, b.start), max(a.end, b.end))

def execute(ary, function):
    intervals = generateIntervals(ary)
    ans = function(intervals)
    return ans
