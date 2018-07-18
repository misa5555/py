class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def rotateSide(matrix, s, l):
            #p1 = [(s,s), (s,s+1), ....(s, s+l-1)]
            p1 = [ (s, s + _l) for _l in range(l)]
            #p2 = [(s, s+l), (s+1, s+l)...(s+l-1, s+l)]
            p2 = [ (s + _l, s + l) for _l in range(l)]
            #p3 = [(s+l, s+l), (s+l,s+l-1), .....(s+l, s+1)]
            p3 = [(s + l, s + _l) for _l in reversed(range(1, l+1))]
            #p4 = [(s+l, s), (s+l-1, s), ...(s+1, s)]
            p4 = [(s + _l, s) for _l in reversed(range(1, l+1))]
            tmp = matrix[s][s:s+l]
            print(matrix)
            # copy p4 to p1, p3 to p4, p2 to p3, p1(tmp) to p2
            for i in range(l):
                matrix[p1[i][0]][p1[i][1]] = matrix[p4[i][0]][p4[i][1]]
            for i in range(l):
                matrix[p4[i][0]][p4[i][1]] = matrix[p3[i][0]][p3[i][1]]
            for i in range(l):
                matrix[p3[i][0]][p3[i][1]] = matrix[p2[i][0]][p2[i][1]]
            for i in range(l):
                matrix[p2[i][0]][p2[i][1]] = tmp[i]

        length = len(matrix) - 1
        start = 0
        while length >= 1:
            rotateSide(matrix, start, length)
            length -= 2
            start += 1
        print(matrix)




s = Solution()
matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
matrix = [
[5, 1, 9,11],
[2, 4, 8,10],
[13,3, 6, 7],
[15,14,12,16]]
s.rotate(matrix)
