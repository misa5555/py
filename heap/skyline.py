class Solution:
    def _getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        #[[2,9,10], [3 7 15], [5 12 12], [15 20 10], [19 24 8]]
        import collections
        turning_point = {}
        for b in buildings:
            to_update = b[2]
            turning_point[b[0]] = (b[1], b[2])
            turning_point[b[1]] = (b[1], 0)

        edges = collections.OrderedDict(sorted(turning_point.items()))
        #edges {2: (9, 10), 3: (7, 15), 5:(12, 12), 7:(7, -1), 9: 'e', 12: 'e'...}
        from queue import PriorityQueue
        height_queue = PriorityQueue()
        result = []
        for edge, end_height in edges.items():
            end, height = end_height
            tmp = float('-inf')
            while not height_queue.empty():
                hq = height_queue.get()
                if hq[1] > edge:
                    height_queue.put(hq)
                    tmp = -hq[0]
                    break
            if end_height[1] > 0:
                height_queue.put((-height, end))
            new_height = max(height, tmp)
            if not result or (result and result[-1][1] != new_height):
                result.append((edge, new_height))
        print(result)
        return result

    def getSkyline(self, buildings):
s = Solution()
# s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
s.getSkyline([[2,4,7],[2,4,5],[2,4,6]])