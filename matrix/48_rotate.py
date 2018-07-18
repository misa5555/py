class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        return list(map(list, map(reversed, list(zip(*matrix)))))

s = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(s.rotate(matrix))