class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]0
        Input:
        [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

        Output:
        [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        """
        re = []
        people.sort(key=lambda x: (-x[0], x[1]))
        i = 0
        while i < len(people):
            crt_height = people[i][0]
            j = i
            while j < len(people) and people[j][0] == crt_height:
                re.insert(people[j][1], people[j])
                j += 1
            i = j
        print(re)
        return re
s = Solution()
s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])


s = Solution()
s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
