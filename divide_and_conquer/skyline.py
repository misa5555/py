class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        import heapq
        from itertools import chain
        from collections import defaultdict
        # [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]
        #[[2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0]]
        # checking_points: [2, 3, 5, 7, 9, 12, 15..]
        checking_points = sorted(list(chain(*[ node[0:2] for node in buildings ])))
        SEH = defaultdict(list)
        for el in buildings:
            SEH[el[0]].append((el[1], el[2]))

        # SEH = {node[0]: (node[1], node[2]) for i, node in enumerate(buildings)}
        HR = []
        ans = []
        for p in checking_points:
            if p in SEH:
                while SEH[p]:
                    EH = SEH[p].pop()
                    heapq.heappush(HR, (-EH[1], -EH[0]))
            while HR and (p > -HR[0][1] or p == -HR[0][1]):
                heapq.heappop(HR)
            tmp = 0
            if HR:
                tmp = -HR[0][0]
            if not ans or ans[-1][1] != tmp:
                ans.append((p, tmp))

        return ans

s = Solution()
s.getSkyline([ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ])
s.getSkyline([[2,4,7],[2,4,5],[2,4,6]])